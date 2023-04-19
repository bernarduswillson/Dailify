import os
path = "src/databases/JournalTXT/journal-2020-12-12.txt"

# Create the directories if they don't exist
os.makedirs(os.path.dirname(path), exist_ok=True)

# Open the file for writing
with open(path, "w") as file:
    file.write("Hello, world!")