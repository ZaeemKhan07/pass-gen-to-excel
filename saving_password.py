import pandas as pd
import os

def save_to_excel(nr_letters, nr_symbols, nr_numbers, password):
    """
    Saves the generated password and its details to an Excel file.

    Args:
        nr_letters (int): The number of letters in the password.
        nr_symbols (int): The number of symbols in the password.
        nr_numbers (int): The number of numbers in the password.
        password (str): The generated password.
    """
    file_name = 'passwords.xlsx'
    new_data = pd.DataFrame({
        'How many letters would you like in your password?': [nr_letters],
        'How many symbols would you like?': [nr_symbols],
        'How many numbers would you like?': [nr_numbers],
        'Your password is:': [password]
    })

    if os.path.exists(file_name):
        existing_data = pd.read_excel(file_name)
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        updated_data.to_excel(file_name, index=False, engine='openpyxl')
        print(f"Password saved to {file_name}")
    else:
        new_data.to_excel(file_name, index=False, engine='openpyxl')
        print(f"Created {file_name} and saved the password.")