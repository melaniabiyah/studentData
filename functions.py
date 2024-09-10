# utils.py
import re
from constraints import validate_string, validate_set, validate_column_exists


def clean_name(name):
    validate_string(name, "Name")
    return re.sub(r'[^A-Za-z]', '', name)


def split_name(full_name):
    validate_string(full_name, "Full name")
    parts = full_name.split()

    if len(parts) == 1:
        first_name = parts[0]
        last_name = ''
    elif len(parts) == 2:
        first_name, last_name = parts
    else:
        first_name = parts[0]
        last_name = parts[-1]

    return first_name, last_name


def generate_email(full_name, existing_emails):
    validate_string(full_name, "Full name")
    validate_set(existing_emails, "Existing emails")

    first_name, last_name = split_name(full_name)
    first_name_clean = clean_name(first_name)
    last_name_clean = clean_name(last_name)

    if not last_name_clean:
        email = first_name_clean.lower()
    else:
        email = f"{first_name_clean[0].lower()}{last_name_clean.lower()}"

    base_email = email
    count = 1
    while email in existing_emails:
        email = f"{base_email}{count}"
        count += 1

    existing_emails.add(email)
    return f"{email}@gmail.com"


def find_special_character_names(df):
    validate_column_exists(df, 'Student Name')
    return df[df['Student Name'].str.contains(r'[^A-Za-z\s]', regex=True)]
