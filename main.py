import os
import pandas as pd
import logging
from functions import generate_email, find_special_character_names
from constraints import validate_column_exists

# Set up logging
log_file_path = os.path.join('Script', 'data_processing.log')
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
logging.basicConfig(filename=log_file_path,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Create a DataFrame
df_all = pd.DataFrame('Input/Test Files.xlsx')

# Shuffle the DataFrame
df_shuffled = df.sample(frac=1).reset_index(drop=True)

# Save to a JSON file
df_shuffled.to_json('shuffled_names.json', orient='records', lines=False)

print("Shuffled names saved to shuffled_names.json")

# Assuming the .xlsx file is in a 'Data' folder within your project directory
file_path = os.path.join('Input', 'Test Files.xlsx')

try:
    # Read the Excel file using pandas
    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip()  # Clean up column names
    logging.info(f"Excel file '{file_path}' read successfully.")
    print("Original Data:")
    print(df.head())
except Exception as e:
    logging.error(f"Failed to read Excel file: {e}")
    raise

try:
    # Check for required columns
    validate_column_exists(df, 'Student Name')
    validate_column_exists(df, 'Email Address')
    logging.info("Required columns ('Student Name', 'Email Address') exist in the data.")

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
    logging.info("Email addresses generated and added to the DataFrame.")

except ValueError as e:
    logging.error(f"Error in processing: {e}")
    print(f"Error: {e}")
except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
    print(f"Unexpected Error: {e}")

try:
    # Check for required columns
    validate_column_exists(df, 'Gender')
    logging.info("Column 'Gender' exists in the data.")

    # Separate male and female students based on 'Gender' column
    males = df[df['Gender'].str.upper() == 'M']
    females = df[df['Gender'].str.upper() == 'F']

    # Print the number of male and female students
    print(f"\nNumber of Male Students: {len(males)}")
    print(f"Number of Female Students: {len(females)}")
    logging.info(f"Separated students into {len(males)} males and {len(females)} females.")

    # Ensure output folder exists
    os.makedirs('Output', exist_ok=True)

    # Save the lists to separate files
    males_file_path = os.path.join('Output', 'Male_Students.xlsx')
    females_file_path = os.path.join('Output', 'Female_Students.xlsx')

    males.to_excel(males_file_path, index=False)
    females.to_excel(females_file_path, index=False)

    print(f"\nMale students saved to: {males_file_path}")
    print(f"Female students saved to: {females_file_path}")
    logging.info(f"Male and Female student lists saved to Excel files.")

    # Display lists of male and female students
    print("\nList of Male Students:")
    for index, row in males.iterrows():
        print(f"Student Name: {row['Student Name']}")
    logging.info("Displayed list of male students.")

    print("\nList of Female Students:")
    for index, row in females.iterrows():
        print(f"Student Name: {row['Student Name']}")
    logging.info("Displayed list of female students.")

except ValueError as e:
    logging.error(f"Error in processing: {e}")
    print(f"Error: {e}")
except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
    print(f"Unexpected Error: {e}")

# Find and display names with special characters
try:
    special_char_names = find_special_character_names(df)
    print("\nNames with Special Characters:")
    for index, row in special_char_names.iterrows():
        print(f"Student Name: {row['Student Name']}")
    logging.info("Displayed list of students with special characters in their names.")
except Exception as e:
    logging.error(f"Error while finding special character names: {e}")

# File paths for saving CSV and TSV files
csv_file_path = os.path.join('Output', 'Student_Data.csv')
tsv_file_path = os.path.join('Output', 'Student_Data.tsv')

# Save the DataFrame as a CSV file
try:
    df.to_csv(csv_file_path, index=False)
    print(f"\nData saved as CSV file at: {csv_file_path}")
    logging.info(f"Data saved as CSV file at: {csv_file_path}")
except Exception as e:
    logging.error(f"Failed to save CSV file: {e}")

# Save the DataFrame as a TSV file
try:
    df.to_csv(tsv_file_path, index=False, sep='\t')
    print(f"Data saved as TSV file at: {tsv_file_path}")
    logging.info(f"Data saved as TSV file at: {tsv_file_path}")
except Exception as e:
    logging.error(f"Failed to save TSV file: {e}")
