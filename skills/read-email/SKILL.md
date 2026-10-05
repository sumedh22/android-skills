---
name: read-yahoo-emails
description: Connect to Yahoo Mail IMAP server using Python and a user-supplied App Password to read, fetch, and process unread Yahoo emails for Gemma processing.
---

# Read Yahoo Emails via IMAP

Connect to Yahoo Mail using Python's standard `imaplib` library and a Yahoo App Password to fetch emails.

## Summary

This skill uses a standalone Python script to authenticate with Yahoo Mail (`imap.mail.yahoo.com:993`) using a user-provided 16-character Yahoo App Password and retrieve unread or recent messages.

## When to Use

- Fetching Yahoo emails directly using an App Password.
- Reading Yahoo Mail inbox contents programmatically in Python on Android (Termux) or desktop.
- Preparing Yahoo email text for Gemma or local LLM summarization.

## Steps

1. **Obtain Yahoo App Password:**
   - Log in to your Yahoo Account Security settings.
   - Select **Generate App Password**, enter an app name (e.g., "Gemma Email Reader"), and copy the 16-character key.

2. **Run Python IMAP Script:**
   - Pass your Yahoo email address and the 16-character App Password to `fetch_yahoo_emails.py`.

3. **Parse Output:**
   - Retrieve structured email metadata (`From`, `Subject`, `Date`) and text body payloads for consumption by Gemma.

## Gotchas

- **Authentication Failure:** Standard Yahoo account passwords will be rejected. A generated App Password is required.
- **Port & Security:** Yahoo requires SSL connections over port `993`.
