import json
from datetime import datetime
import os

file_path = "Data/TaskData.json"
os.makedirs(os.path.dirname(file_path), exist_ok=True)

def get_current_timestamp():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def get_user_input():
    new_data = {}
    new_data["id"] = int(input("Please enter task id: "))
    new_data["description"] = input("Please enter description name: ")
    new_data["status"] = input("Please enter task status(todo, in-progress or done): ")
    new_data["createdAt"] = get_current_timestamp()
    new_data["updatedAt"] = new_data["createdAt"]
    return new_data
def load_data():
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    except json.JSONDecodeError:
        data = []
    return data

def save_data(data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def main():
    data = load_data()
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            new_data = get_user_input()
            data.append(new_data)
            save_data(data)
            print("Task added successfully.")
        elif choice == "2" or choice.lower() == "q":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()