import email
import imaplib
import sys
from email.header import decode_header


def connect_and_fetch_yahoo(
    email_address: str, app_password: str, max_emails: int = 5
) -> list[dict]:
    """Connects to Yahoo IMAP using an App Password and fetches unread emails."""
    imap_host = "imap.mail.yahoo.com"
    imap_port = 993

    try:
        mail = imaplib.IMAP4_SSL(imap_host, imap_port)
        # Yahoo App Password (16 characters, spaces optional)
        mail.login(email_address, app_password.replace(" ", ""))
        mail.select("INBOX")
    except imaplib.IMAP4.error as e:
        print(f"Authentication failed: {e}")
        return []

    # Search for unread messages
    status, response = mail.search(None, "UNSEEN")
    if status != "OK" or not response[0]:
        print("No unread emails found.")
        mail.logout()
        return []

    email_ids = response[0].split()
    fetched_emails = []

    # Fetch up to max_emails
    for e_id in email_ids[-max_emails:]:
        status, data = mail.fetch(e_id, "(RFC822)")
        if status != "OK":
            continue

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                # Decode subject
                raw_subject = msg.get("Subject", "")
                decoded_header = decode_header(raw_subject)[0]
                subject = decoded_header[0]
                if isinstance(subject, bytes):
                    encoding = decoded_header[1] or "utf-8"
                    subject = subject.decode(encoding, errors="ignore")

                sender = msg.get("From", "")
                date = msg.get("Date", "")

                # Extract plain text body
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        disposition = str(part.get("Content-Disposition"))
                        if (
                            content_type == "text/plain"
                            and "attachment" not in disposition
                        ):
                            payload = part.get_payload(decode=True)
                            if payload:
                                body = payload.decode("utf-8", errors="ignore")
                            break
                else:
                    payload = msg.get_payload(decode=True)
                    if payload:
                        body = payload.decode("utf-8", errors="ignore")

                fetched_emails.append({
                    "from": sender,
                    "subject": subject,
                    "date": date,
                    "body": body.strip(),
                })

    mail.logout()
    return fetched_emails


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "Usage: python fetch_yahoo_emails.py <YOUR_YAHOO_EMAIL>"
            " <16_CHAR_APP_PASSWORD>"
        )
        sys.exit(1)

    yahoo_email = sys.argv[1]
    app_password = sys.argv[2]

    emails = connect_and_fetch_yahoo(yahoo_email, app_password)

    print(f"Successfully retrieved {len(emails)} unread email(s):\n")
    for i, em in enumerate(emails, 1):
        print(f"[{i}] From: {em['from']}")
        print(f"    Subject: {em['subject']}")
        print(f"    Date: {em['date']}")
        print(f"    Body snippet: {em['body'][:200]}...\n")
