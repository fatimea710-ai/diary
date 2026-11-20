from datetime import datetime
import diary_manager

def get_diary_date():
    while True:
        try:
            user_input = input("Enter date (mm dd yyyy): ").split()

            if len(user_input) != 3:
                print("Please enter month, day, and year.")
                continue

            month = int(user_input[0])
            day = int(user_input[1])
            year = int(user_input[2])

            return datetime(year, month, day)

        except ValueError:
            print("Invalid date. Please try again.")

def main():
    diary_file ="diaries.txt"

    while True:
        print(f"\n1. Create a dated diary entry")
        print(f"2. See all entries made") 
        print(f"3. Find a diary entry by the date")
        print(f"4. Switch the diary file")
        print(f"5. Exit")

        choice = input ("Choose: ")

        if choice == "1": 
            print(f"Make your diary entry")
            user_input = input(" mm dd yyyy: ").split()
            month = int(user_input[0])
            day = int(user_input[1])
            year = int(user_input[2]) 

            day = get_diary_date()
            date = day.strftime("%m/%d/%Y")
            entry = input("Write your diary entry: ")
            diary_manager.save_entry(diary_file, date, entry) 

        
        elif choice == "2":
            diary_manager.see_entries(diary_file)

        elif choice == "3": 
            print("Find a diary entry by the date")
            user_input = input(" mm dd yyyy: ").split()
            month = int(user_input[0])
            day = int(user_input[1])
            year = int(user_input[2])

            search_date = get_diary_date().strftime("%m/%d/%Y")
            diary_manager.find_entry(diary_file, search_date)

        elif choice == "4":
            diary_file = input("Enter the name of your diary: ")

        elif choice == "5": 
            break 

        else:
            print(f"Invalid, please try again.")




        
if __name__ == "__main__" :
            main()