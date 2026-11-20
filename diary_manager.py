def save_entry(diary_file, date, entry):
    with open(diary_file, "a") as file:
        file.write(f"{date}: {entry}\n")
        print(f"Diary entry saved for {date}.")
        
def see_entries(diary_file):
    try:
        with open(diary_file, "r") as file:
            entries = file.readlines()
            if entries:
                print(f"Entries in {diary_file}:")
                for entry in entries:
                    print(entry.strip())
            else:
                print(f"No entries found in {diary_file}.")
    except FileNotFoundError:
        print(f"File {diary_file} not found.")

def find_entry(diary_file, search_date):
        with open(diary_file, "r") as file:
            entries = file.readlines()
            found_entries = [entry for entry in entries if entry.startswith(search_date)]
            if found_entries:
                print(f"Entries for {search_date}:")
                for entry in found_entries:
                    print(entry.strip())
            else:
                print(f"No entries found for {search_date}.")
            