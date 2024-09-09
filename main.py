import os
import pandas as pd
import re

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns

# Assuming the .xlsx file is in a 'Data' folder within your project directory
file_path = os.path.join('Data', 'Test Files.xlsx')

# Read the Excel file using pandas
df = pd.read_excel(file_path)

# Display the first few rows of the data
print("Original Data:")
print(df.head())

# Function to clean names (remove special characters and spaces)
def clean_name(name):
    return re.sub(r'[^A-Za-z]', '', name)

# Function to split full name into first and last names, ignoring the middle name
def split_name(full_name):
    # Split the name by spaces
    parts = full_name.split()

    if len(parts) == 1:
        # If only one name is available, treat it as both first and last name
        first_name = parts[0]
        last_name = ''
    elif len(parts) == 2:
        # If there are two parts, treat the first as first name and second as last name
        first_name, last_name = parts
    else:
        # Ignore the middle name: take the first part as first name, and the last part as last name
        first_name = parts[0]
        last_name = parts[-1]

    return first_name, last_name

# Function to generate email address based on names
def generate_email(full_name, existing_emails):
    # Split the full name into first and last name
    first_name, last_name = split_name(full_name)

    # Clean the names to remove special characters
    first_name_clean = clean_name(first_name)
    last_name_clean = clean_name(last_name)

    # If no last name is provided, use the first name only
    if not last_name_clean:
        email = first_name_clean.lower()
    else:
        # Use the first letter of the first name and the entire last name
        email = f"{first_name_clean[0].lower()}{last_name_clean.lower()}"

    # Ensure the email is unique
    base_email = email
    count = 1
    while email in existing_emails:
        email = f"{base_email}{count}"
        count += 1

    # Add to the list of existing emails to track uniqueness
    existing_emails.add(email)

    # Return the email with the desired domain
    return f"{email}@gmail.com"

# Assuming the Excel file has 'Student Name' and 'Email Address' columns
if 'Student Name' in df.columns and 'Email Address' in df.columns:
    # Set to keep track of unique email addresses
    existing_emails = set()

    # Generate email addresses and add them to the existing 'Email Address' column
    df['Email Address'] = df.apply(
        lambda row: generate_email(row['Student Name'], existing_emails),
        axis=1
    )

    # Display the updated DataFrame with email addresses
    print("\nData with Emails:")
    for index, row in df.iterrows():
        print(f"Student Name: {row['Student Name']} - Email address: {row['Email Address']}")

    # Optionally, save the DataFrame with updated email addresses back to an Excel file
    output_file_path = os.path.join('Data', 'Test Files with Emails.xlsx')
    df.to_excel(output_file_path, index=False)
    print(f"\nUpdated data saved to: {output_file_path}")
else:
    print("The required columns 'Student Name' or 'Email Address' are missing from the file.")
