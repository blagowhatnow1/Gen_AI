# tasks.py

tasks = []

def add_task(task):
    if not task.strip():  # Check if the task is empty or contains only whitespace
        return "Error: Task cannot be empty."
    tasks.append(task)
    return f"Task '{task}' added."

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        return f"Task '{task}' removed."
    else:
        return "Task not found."

def list_tasks():
    return tasks

def reset_tasks():
    global tasks
    tasks = []
