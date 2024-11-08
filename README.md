# Task Tracker CLI

Task Tracker CLI is a simple command-line interface (CLI) application designed to help you manage your tasks efficiently. It allows you to add, update, delete, and track the status of tasks in a JSON file, making it easy to keep track of your to-dos, in-progress tasks, and completed tasks directly from your terminal.

This project is part of [roadmap.sh Task Tracker project](https://roadmap.sh/projects/task-tracker).

## Features

- Add new tasks with a description
- Update tasks to change their status or description
- Delete tasks by ID
- List all tasks or filter by their status (to-do, in-progress, or done)
- Simple and persistent storage in a JSON file
- User-friendly CLI interface with no external dependencies

## Prerequisites

- **Python 3** installed on your machine.

## Installation

1. Clone or download this repository.

2. (Optional) Install `tabulate` for enhanced display formatting in your terminal:
   ````pip install tabulate````
3. Make the script executable:
    ```chmod +x task_tracker.py```

## Usage

The application accepts commands as positional arguments, allowing you to manage your tasks from the command line.

1. ## Add a Task

Add a new task description
```python task-cli add "Your task description here"```

1. ## Update a Task

Update a task description
```python task-cli update <task_id> "New task description"```

Mark a task as in-progress:
```python task-cli update <task_id> mark-in-progress```

Mark a task as done:
```python task-cli update <task_id> mark-done```

1. ## Delete a Task

Delete a task by specifying its task ID.:
```python task-cli delete <task_id>```

1. ## List Tasks

List all tasks:
```python task-cli.py list```

List tasks by their status:
```python task-cli.py list todo```
```python task-cli.py list in-progress```
```python task-cli.py list done```


## File Structure

- task_cli.py : Main script to run the CLI application.
- database.json : JSON file that stores all tasks with their details.

## Error Handling

If the JSON file is missing or corrupted, the application will handle it gracefully by recreating a new file.
If tabulate is missing, the program will notify you to install it.

## Project Link

This project was inspired by the [roadmap.sh Task Tracker project](https://roadmap.sh/projects/task-tracker).

