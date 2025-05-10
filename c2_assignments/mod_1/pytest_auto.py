import pytest
from tasks import add_task, remove_task, list_tasks, reset_tasks

@pytest.fixture(autouse=True)
def setup():
    # Automatically reset tasks before each test
    reset_tasks()

def test_add_task():
    result = add_task("Buy groceries")
    assert "Buy groceries" in list_tasks()
    assert result == "Task 'Buy groceries' added."

def test_add_empty_task():
    result = add_task("")
    assert "" not in list_tasks()
    assert result == "Error: Task cannot be empty."

def test_add_whitespace_task():
    result = add_task("   ")
    assert "   " not in list_tasks()
    assert result == "Error: Task cannot be empty."

def test_add_duplicate_task():
    add_task("Buy groceries")
    result = add_task("Buy groceries")
    assert list_tasks().count("Buy groceries") == 2
    assert result == "Task 'Buy groceries' added."

def test_remove_task():
    add_task("Read a book")
    result = remove_task("Read a book")
    assert "Read a book" not in list_tasks()
    assert result == "Task 'Read a book' removed."

def test_remove_non_existent_task():
    result = remove_task("Go jogging")
    assert result == "Task not found."

def test_list_tasks():
    add_task("Buy groceries")
    add_task("Read a book")
    result = list_tasks()
    assert result == ["Buy groceries", "Read a book"]

def test_list_tasks_empty():
    result = list_tasks()
    assert result == []

def test_add_task_with_special_characters():
    task = "@#$%^&*()_+!"
    result = add_task(task)
    assert task in list_tasks()
    assert result == f"Task '{task}' added."

def test_add_task_with_long_string():
    task = "a" * 1000  # Very long task name
    result = add_task(task)
    assert task in list_tasks()
    assert result == f"Task '{task}' added."

def test_remove_task_with_similar_names():
    task1 = "Read a book"
    task2 = "Read a book tomorrow"
    add_task(task1)
    add_task(task2)
    result = remove_task(task1)
    assert task1 not in list_tasks()
    assert task2 in list_tasks()
    assert result == f"Task '{task1}' removed."

def test_remove_task_case_sensitivity():
    task = "Read a Book"
    add_task(task)
    result = remove_task("read a book")
    assert task in list_tasks()
    assert result == "Task not found."

def test_concurrent_modifications():
    tasks_to_add = ["Task 1", "Task 2", "Task 3"]
    for task in tasks_to_add:
        add_task(task)
    remove_task("Task 2")
    add_task("Task 4")
    expected_tasks = ["Task 1", "Task 3", "Task 4"]
    assert list_tasks() == expected_tasks

def test_add_task_returns_correct_message():
    task = "Complete assignment"
    result = add_task(task)
    assert result == f"Task '{task}' added."

def test_remove_task_returns_correct_message():
    task = "Complete assignment"
    add_task(task)
    result = remove_task(task)
    assert result == f"Task '{task}' removed."
