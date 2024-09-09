import os
import pandas as pd
from functions import generate_email, find_special_character_names
from constraints import validate_column_exists

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Assuming the .xlsx file is in a 'Data' folder within your project directory
file_path = os.path.join('Data', 'Test Files.xlsx')

# Read the Excel file using pandas
df = pd.read_excel(file_path)

# Display the first few rows of the data
print("Original Data:")
print(df.head())

try:
    # Check for required columns
    validate_column_exists(df, 'Student Name')
    validate_column_exists(df, 'Email Address')

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

except ValueError as e:
    print(f"Error: {e}")

try:
    # Check for required columns
    validate_column_exists(df, 'Gender')

    # Separate male and female students based on 'Gender' column
    males = df[df['Gender'].str.upper() == 'M']
    females = df[df['Gender'].str.upper() == 'F']

    # Print the number of male and female students
    print(f"\nNumber of Male Students: {len(males)}")
    print(f"Number of Female Students: {len(females)}")

    # Save the lists to separate files
    males_file_path = os.path.join('Data', 'Male_Students.xlsx')
    females_file_path = os.path.join('Data', 'Female_Students.xlsx')

    males.to_excel(males_file_path, index=False)
    females.to_excel(females_file_path, index=False)

    print(f"\nMale students saved to: {males_file_path}")
    print(f"Female students saved to: {females_file_path}")

except ValueError as e:
    print(f"Error: {e}")

# Find and display names with special characters
special_char_names = find_special_character_names(df)
print("\nNames with Special Characters:")
for index, row in special_char_names.iterrows():
    print(f"Student Name: {row['Student Name']}")
