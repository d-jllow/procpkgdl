import pandas as pd
import os

# Read the Excel file
excel_file = 'pylinux_processed.xlsx'
df = pd.read_excel(excel_file)

# Create a dictionary to hold the packages for each user
user_packages = {}

# Loop through the rows and assign packages to users
for _, row in df.iterrows():
    package = row['Package']
    user = row['User']
    
    # If the user doesn't exist in the dictionary, create an entry
    if user not in user_packages:
        user_packages[user] = []
    
    # Add the package to the user's list
    user_packages[user].append(package)

# Create directories and write the requirements.txt files
for user, packages in user_packages.items():
    # Create directory for the user
    os.makedirs(user, exist_ok=True)
    
    # Write the requirements.txt file for the user
    with open(f'{user}/requirements_pylinux.txt', 'w') as f:
        for package in packages:
            f.write(f'{package}\n')

print("Requirements files generated successfully.")
