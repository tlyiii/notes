import os
import subprocess
from datetime import datetime

# Specify the path to your autonote.md file
file_path = r"C:\Users\Home\Desktop\Float_File\Projects\notes\autonote.md"

# Specify the path to the Git repository (where .git is located)
repo_path = r"C:\Users\Home\Desktop\Float_File\Projects\notes"

# Function to append note to autonote.md
def add_note_to_file(note):
    try:
        with open(file_path, 'a') as file:
            # Add a timestamp to the note
            file.write(f"\n- [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {note}")
        print(f"Note added to {file_path}.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")

# Function to commit and push changes to GitHub
def commit_and_push(note):
    try:
        # Change to the repository directory
        os.chdir(repo_path)
        
        # Add the changes
        subprocess.run(["git", "add", file_path], check=True)
        
        # Commit with a meaningful message
        commit_message = f"Added note: {note}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push to the GitHub repository
        subprocess.run(["git", "push"], check=True)

        print("Changes have been pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print(f"Error during Git operation: {e}")

# Main function to handle input and process note
def main():
    # Get the note input from the terminal
    note = input('Enter your note: ')
    
    # Add the note to autonote.md
    add_note_to_file(note)
    
    # Commit and push the changes
    commit_and_push(note)

if __name__ == "__main__":
    main()
