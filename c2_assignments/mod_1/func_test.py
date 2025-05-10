# func_test.py

import unittest
from tasks import add_task, remove_task, list_tasks, reset_tasks

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        reset_tasks()  # Reset tasks before each test

    def test_add_task(self):
        result = add_task("Buy groceries")
        self.assertIn("Buy groceries", list_tasks())
        self.assertEqual(result, "Task 'Buy groceries' added.")

    def test_add_empty_task(self):
        result = add_task("")
        self.assertNotIn("", list_tasks())
        self.assertEqual(result, "Error: Task cannot be empty.")

    def test_add_duplicate_task(self):
        add_task("Buy groceries")
        result = add_task("Buy groceries")
        self.assertEqual(len(list_tasks()), 2)  # Assuming duplicates are allowed
        self.assertEqual(result, "Task 'Buy groceries' added.")

    def test_remove_task(self):
        add_task("Read a book")
        result = remove_task("Read a book")
        self.assertNotIn("Read a book", list_tasks())
        self.assertEqual(result, "Task 'Read a book' removed.")

    def test_remove_non_existent_task(self):
        result = remove_task("Go jogging")
        self.assertEqual(result, "Task not found.")

    def test_list_tasks(self):
        add_task("Buy groceries")
        add_task("Read a book")
        result = list_tasks()
        self.assertEqual(result, ["Buy groceries", "Read a book"])

    def test_list_tasks_empty(self):
        result = list_tasks()
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
