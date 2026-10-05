---
name: read-android-emails
description: Read and process emails from Android email applications like Gmail or Outlook using official APIs, IMAP/POP3, or ADB/Notification listener hooks. Use when user requests reading, fetching, or analyzing emails from an Android device or Android email app.
---

# Read Android Emails

Guide and execute email extraction from Android email clients using API integration, IMAP/POP3 protocols, or ADB and notification inspection on Android devices.

## Summary

This skill provides step-by-step methods and reusable scripts to read emails from Android email applications (such as Gmail, Outlook, or K-9 Mail) through official cloud APIs, direct IMAP access, or local Android integration (ADB / Termux / Notification Listener).

## When to Use

- Reading or summarizing recent emails from a mobile or Android email application.
- Automating email fetching on Android devices via Termux, ADB, or Python.
- Setting up email extraction for Gemma models or local LLMs on Android.

## Steps

### Method 1: Gmail API Integration (Recommended for Android / Google Accounts)

1. Enable the Gmail API in Google Cloud Console and generate client credentials (`credentials.json`).

2. Authenticate using OAuth 2.0 to generate a user token (`token.json`).

3. Query messages using the Google API Client Library for Python:
   - Request list of messages: `service.users().messages().list(userId='me', q='is:unread').execute()`
   - Fetch message details: `service.users().messages().get(userId='me', id=msg_id).execute()`

4. Verify success: Check that message body and header metadata are returned in JSON format.

### Method 2: Direct IMAP Access (Universal for Email Apps)

1. Obtain an App Password from the email provider (e.g., Gmail, Outlook, Yahoo).

2. Connect using Python's built-in `imaplib` library:
   - Server: `imap.gmail.com` (Gmail) or `outlook.office365.com` (Outlook), Port `993` (SSL).

3. Search and fetch unseen emails:
   - `mail.search(None, 'UNSEEN')`
   - Extract `From`, `Subject`, and text payload.

4. Verify success: Confirm incoming emails are parsed cleanly into plain text.

### Method 3: ADB / On-Device Inspection (For Local Android UI / Notifications)

1. Enable Developer Options and USB Debugging (or Wireless Debugging) on the Android device.

2. Dump active notifications for email apps using ADB:
   - `adb shell dumpsys notification | grep -A 10 -i com.google.android.gm`

3. Parse notification titles and body text representing incoming emails.

4. Verify success: Check ADB console output for email subject lines and snippets.

## Gotchas

- **2-Factor Authentication:** Standard passwords will fail with IMAP; an App Password or OAuth token is required.

- **Background Restraints:** Android OS power management may restrict Termux or background scripts from running continuously.

- **Privacy & Permissions:** ADB access requires explicit USB debugging authorization on the device.
