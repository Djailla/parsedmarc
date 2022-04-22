from parsedmarc.mail.mailbox_connection import MailboxConnection
from parsedmarc.mail.graph import MSGraphConnection
from parsedmarc.mail.gmail import GmailConnection
from parsedmarc.mail.imap import IMAPConnection

__all__ = ["MailboxConnection",
           "MSGraphConnection",
           "GmailConnection",
           "IMAPConnection"]
