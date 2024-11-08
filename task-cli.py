#!/usr/bin/env python3

# Importing the required modules
import os
import sys
import json
from datetime import datetime

try:
    from tabulate import tabulate
except ModuleNotFoundError:
    print(
        "The 'tabulate' module is not installed. Please install it by running 'pip install tabulate'."
    )
    sys.exit(1)

# Defining the file path
file_path = "database.json"

# Checking if the file exists or not
if not os.path.exists(file_path):
    with open(file_path, "w") as db:
        json.dump({}, db)


# This function will read the database
def read_db():
    """Reads and returns the task data from the JSON database file.

    Returns:
        dict: Dictionary containing all tasks."""

    with open(file_path, "r") as db:
        return json.load(db)


# This function will write the database
def write_db(data):
    """Writes task data to the JSON database file.

    Args:
        data (dict): Dictionary containing all tasks to be saved."""
        
    with open(file_path, "w") as db:
        return json.dump(data, db, indent=4)


# This function is for adding tasks
def create_task(task):
    """Creates a new task and saves it to the database.

    Args:
        task (str): Description of the task to be added."""
        
    task_dict = dict()
    database = read_db()

    id = 1 if not database else int(list(database)[-1]) + 1
    task_dict["description"] = task
    task_dict["id"] = id
    task_dict["status"] = "todo"
    task_dict["createdAt"] = datetime.now().isoformat()
    task_dict["updatedAt"] = datetime.now().isoformat()

    if task_dict["description"]:
        database[id] = task_dict
    else:
        print("A task cannot have an empty description")
        return

    write_db(database)

    print(f"Task added successfully (ID: {id})")


def update_task(task_id, new_description):
    """Updates an existing task's description or status.

    Args:
        task_id (int): ID of the task to be updated.
        new_description (str): New description or status ("mark-in-progress" or "mark-done").
    """
    database = read_db()
    if str(task_id) in database:
        task = database[str(task_id)]
        if new_description == "mark-in-progress" or new_description == "mark-done":
            if new_description == "mark-in-progress":
                task["status"] = "in-progress"
            else:
                task["status"] = "done"
        else:
            task["description"] = new_description
        task["updatedAt"] = datetime.now().isoformat()
        database[str(task_id)] = task
        write_db(database)
        print(f"Task with (ID: {task_id}) updated successfully")
    else:
        print(f"Task with (ID: {task_id}) does not exist")


def delete_task(task_id):
    """Deletes a task from the database by its ID.

    Args:
        task_id (int): ID of the task to be deleted."""
    database = read_db()
    if str(task_id) in database:
        del database[str(task_id)]
        write_db(database)
        print(f"Task with (ID: {task_id}) has been deleted successfully.")
    else:
        print(f"Task with (ID: {task_id}) does not exist")


def print_data(data):
    """
    Prints task data in a table format.

    Args:
        data (list): List of task dictionaries to display.
    """
    table = tabulate(
        data,
        headers="keys",
        tablefmt="grid",
        colalign=(
            "left",
            "left",
            "center",
            "left",
            "right",
        ),
    )
    print(table)


def list_tasks(list="all"):
    """
    Lists tasks based on their status.

    Args:
        status (str, optional): Filter for task status. Options are "all", "done", "todo", "in-progress".
    """
    tasks = read_db().values()
    if list == "all":
        print_data(tasks)
    elif list == "done":
        done_tasks = [task for task in tasks if task.get("status") == "done"]
        if done_tasks:
            print_data(done_tasks)
        else:
            print("You don't have any completed task")
    elif list == "in-progress":
        in_progress_tasks = [
            task for task in tasks if task.get("status") == "in-progress"
        ]
        if in_progress_tasks:
            print_data(in_progress_tasks)
        else:
            print("There are no tasks in progress")
    elif list == "todo":
        todo_tasks = [task for task in tasks if task.get("status") == "todo"]
        if todo_tasks:
            print_data(todo_tasks)
        else:
            print("There is no any todo task, add tasks")


def main():
    """Main function to handle command-line arguments and execute appropriate actions."""
    try:
        if len(sys.argv) < 2:
            print("Please provide a valid command")
            return

        command = sys.argv[1]

        if command == "update":
            if len(sys.argv) < 4:
                print("Usage: update <task_id> <new_description>")
            else:
                update_task(sys.argv[2], sys.argv[3])
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Usage: delete <task_id>")
            else:
                delete_task(sys.argv[2])
        elif command == "mark-in-progress" or command == "mark-done":
            if len(sys.argv) < 3:
                print(f"Usage: {command} <task_id>")
            else:
                update_task(sys.argv[2], command)
        elif command == "add":
            if len(sys.argv) < 3:
                print("Usage: add <task_description>")
            else:
                create_task(sys.argv[2])
        elif command == "list":
            status = sys.argv[2] if len(sys.argv) > 2 else "all"
            list_tasks(status)
        else:
            print("Invalid command. Use add, update, delete, or list")
    except IndexError:
        print("Input a correct argument to perform an action")


if __name__ == "__main__":
    main()
