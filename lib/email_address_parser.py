# your code goes here!
import re

class EmailAddressParser:
    """Parses a string to extract all valid email addresses."""

    def __init__(self, text):
        self.text = text

    def parse(self):
        # Regular expression pattern for simple email matching
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

        # Find all matches in the text
        emails = re.findall(email_pattern, self.text)

        # Remove duplicates by converting to set, then sort alphabetically
        return sorted(set(emails))
