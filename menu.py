import json
from datetime import datetime
import os

file_path = "Data/TaskData.json"
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Returns the current timestamp in a specific format
def get_current_timestamp():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Collects user input for creating or updating a task
def get_user_input():
    new_data = {}
    new_data["id"] = int(input("Please enter task id: "))
    new_data["description"] = input("Please enter description name: ")
    new_data["status"] = input("Please enter task status(todo, in-progress or done): ")
    new_data["createdAt"] = get_current_timestamp()
    new_data["updatedAt"] = new_data["createdAt"]
    return new_data

# Loads data from the file. If not found or empty, returns an empty list
def load_data():
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    except json.JSONDecodeError:
        data = []
    return data

# Saves data to the file in JSON format
def save_data(data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def main():
    data = load_data()  # Loads existing tasks data
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. List Tasks by Status")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Adds a new task after collecting input
            new_data = get_user_input()
            data.append(new_data)
            save_data(data)  # Saves the updated data to file
            print("Task added successfully.")
        elif choice == "2":
            # Updates an existing task by ID
            task_id = int(input("Please enter task id: "))
            for task in data:
                if task["id"] == task_id:
                    new_description = input("Please enter new description: ")
                    new_status = input("Please enter new status: ")

                    # Updates the task fields if the new input is not empty
                    task["description"] = new_description if new_description != "" else task["description"]
                    task["status"] = new_status if new_status != "" else task["status"]
                    task["updatedAt"] = get_current_timestamp()
                    task_found = True
                    print("Task updated successfully.")
                    break

            if task_found:
                save_data(data)  # Saves the updated data to file
            else:
                print("Task not found.")
        elif choice == "3":
            # Deletes a task by ID
            task_id = int(input("Please enter task id to delete: "))
            task_found = False

            for task in data:
                if task["id"] == task_id:
                    data.remove(task)  # Removes the task from the list
                    task_found = True
                    print("Task deleted successfully.")
                    break
            if task_found:
                save_data(data)  # Saves the updated data to file
            else:
                print("Task not found.")

        elif choice == "4":
            # Lists all tasks
            for task in data:
                print(task)

        elif choice == "5":
            # Lists tasks filtered by a specific status
            task_status = input("Please enter task status to show: ")
            for task in data:
                if task["status"] == task_status:
                    print(task)
        elif choice.lower() == "q":
            # Exits the program
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
