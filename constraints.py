# constraints.py

def validate_string(value, name):
    if not isinstance(value, str):
        raise ValueError(f"{name} must be a string")

def validate_set(value, name):
    if not isinstance(value, set):
        raise ValueError(f"{name} must be a set")

def validate_column_exists(df, column_name):
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' is missing from the DataFrame")
