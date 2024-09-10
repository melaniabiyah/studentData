# Student Data Processing Project

## Project Overview

This project processes student data from an Excel file, performs computations such as generating unique email addresses, separating male and female students based on gender, and detecting special characters in names. The output data is saved as both CSV and TSV files, and all computations are logged for traceability.

## Features

- **Generate unique email addresses** based on student names.
- **Identify names with special characters** using regular expressions.
- **Separate male and female students** into different files.
- **Save data** in both CSV and TSV formats.
- **Log all computations** to a log file.

## Prerequisites
* Python 3.x
* Pandas
* Numpy (optional)
* TensorFlow (optional for stretch goals)
* Google Cloud API key
* LaBSE Model (for name similarity)

## File Structure

### Input
- `Data/Test Files.xlsx` - Contains student names and other data.

### Output
- `Data/Student_Data.csv` - Processed student data in CSV format.
- `Data/Student_Data.tsv` - Processed student data in TSV format.
- `Data/Male_Students.xlsx` - Contains details of male students.
- `Data/Female_Students.xlsx` - Contains details of female students.

### Scripts

- `main.py` - Main program file that orchestrates the data processing.
- `functions.py` - Contains helper functions like `generate_email` and `find_special_character_names`.
- `constraints.py` - Contains constraints functions like `validate_column_exists`.
- `log_file.log` - Logs all computations for tracking and debugging.

### Dependencies

The following Python packages are required for the project:

- `pandas`
- `transformers`
- `torch`
- `openpyxl`

You can install these dependencies via `requirements.txt` using the following command:

```bash
pip install -r requirements.txt
# studentData
