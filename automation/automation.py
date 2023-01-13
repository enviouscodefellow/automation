import pytest
import re

# Open the file and read its contents
with open("assets/potential-contacts.txt", "r") as file:
    data = file.read()

# Use regular expressions to find all email addresses and phone numbers
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", data)
phones = re.findall(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", data)

# Remove all non-digit characters
phones = [re.sub(r"[^\d]", "", phone) for phone in phones]

# Remove all numbers with a 0 or 1
phones = list(filter(lambda x: not re.match(r"^[01]", x),phones))

# Transform phone numbers to xxx-yyy-zzzz format
phones = [re.sub(r"(\d{3})(\d{3})(\d{4})", r"\1-\2-\3", phone) for phone in phones]

# Add area code 206 to phone numbers with missing area code
phones = [re.sub(r"(\d{3})(\d{3})(\d{4})", r"206-\1-\2-\3", phone) if len(phone)<=7 else phone for phone in phones]

# Remove duplicates
emails = list(set(emails))
phones = list(set(phones))

# Sort the emails and phone numbers in ascending order
emails.sort()
phones.sort()

# Write the emails and phone numbers to separate files
with open("assets/email_addresses.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

with open("assets/phone_numbers.txt", "w") as file:
    for phone in phones:
        file.write(phone + "\n")
