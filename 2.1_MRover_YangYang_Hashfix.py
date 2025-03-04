#Script to fix broken game mod hashes for Male Rover and YangYang in WWMI.
#Author: dROY
#Date: 04-03-2025

import os
import re
import shutil
import keyboard
import time  # Import time module to add delays

# Define variables for the old and new hash values
OLD_HASH_1_MROVER = "d53c2cc7"
NEW_HASH_1_MROVER = "c9db8418"
OLD_HASH_2_MROVER = "f8375eb4"
NEW_HASH_2_MROVER = "3ab7c4d1"
OLD_HASH_3_MROVER = "6e2f48ba"
NEW_HASH_3_MROVER = "a4be44e5"
OLD_HASH_4_YY = "8ac49d65"
NEW_HASH_4_YY = "249200ff"

# Create a dictionary to store the old hash and new hash pairs
replacements = {
    OLD_HASH_1_MROVER: NEW_HASH_1_MROVER,
    OLD_HASH_2_MROVER: NEW_HASH_2_MROVER,
    OLD_HASH_3_MROVER: NEW_HASH_3_MROVER,
    OLD_HASH_4_YY: NEW_HASH_4_YY
}

def replace_hex_values(file_path):
    """
    Function to replace old hex values with new ones in a given file.
    It reads the file, performs replacements, and writes the modified content back to the file.
    """
    # Open the file to read its content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Loop through each hash pair in the replacements dictionary and perform the substitution
    for old, new in replacements.items():
        content = re.sub(old, new, content)
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Updated: {file_path}")
    # Add a small delay after modifying each file to make it less suspicious
    time.sleep(0.5)  # Sleep for 1 second

def create_backup_file(file_path):
    """
    Function to create a backup of the original file.
    The backup file will have the prefix 'DISABLED_backup_' added to its name.
    """
    # Get the directory of the original file
    file_dir = os.path.dirname(file_path)
    # Create the backup file path with a modified name
    backup_file_name = f"DISABLED_backup_{os.path.basename(file_path)}"
    backup_path = os.path.join(file_dir, backup_file_name)
    
    # Copy the original file to the backup location
    shutil.copy(file_path, backup_path)
    print(f"Backup created: {backup_path}")
    # Add a small delay after creating each backup
    time.sleep(0.5)  # Sleep for 1 second

def scan_and_replace(directory):
    """
    Function to scan the directory for 'mod.ini' files and replace hex values in them.
    It will also create backups of the files before making modifications.
    """
    # Walk through the directory and subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file is 'mod.ini' (case-insensitive comparison)
            if file.lower() == "mod.ini":
                file_path = os.path.join(root, file)
                # Create a backup of the file
                create_backup_file(file_path)
                # Replace hex values in the file
                replace_hex_values(file_path)
                # Add a delay after processing each file to slow down the script
                time.sleep(2)  # Sleep for 2 seconds between files

if __name__ == "__main__":
    # Get the current working directory as the target directory
    target_directory = os.getcwd()
    # Scan the target directory and replace hex values in 'mod.ini' files
    scan_and_replace(target_directory)
    
    # Print completion message and wait for user input to exit
    print("Scan complete.")
    print("Press 'Enter' to exit.")
    keyboard.wait("enter")
    print('Thanks for using my tool!')
