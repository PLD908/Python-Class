import unittest
from datetime import datetime
import os
from task_manager import add_task, mark_complete, list_tasks, save_to_csv, load_from_csv

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tasks = []
        self.test_file = 'test_tasks.csv'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        # Test adding a new task
        task_id = add_task(self.tasks, "Test Task 1", "2024-12-31")
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0]['title'], "Test Task 1")
        
        # Test adding another task
        task_id_2 = add_task(self.tasks, "Test Task 2", "2024-12-31")
        self.assertEqual(len(self.tasks), 2)
        self.assertNotEqual(task_id, task_id_2)

    def test_mark_complete(self):
        # Test marking a task complete
        task_id = add_task(self.tasks, "Test Task", "2024-12-31")
        result = mark_complete(self.tasks, task_id)
        self.assertTrue(result)
        self.assertTrue(self.tasks[0]['completed'])
        
        # Test marking non-existent task
        result = mark_complete(self.tasks, 99999)
        self.assertFalse(result)

    def test_save_and_load(self):
        # Test saving and loading tasks
        add_task(self.tasks, "Test Task 1", "2024-12-31")
        add_task(self.tasks, "Test Task 2", "2024-12-31")
        
        # Save tasks
        save_to_csv(self.tasks, self.test_file)
        
        # Load tasks
        loaded_tasks = load_from_csv(self.test_file)
        
        # Verify loaded tasks match original
        self.assertEqual(len(loaded_tasks), len(self.tasks))
        self.assertEqual(loaded_tasks[0]['title'], self.tasks[0]['title'])
        self.assertEqual(loaded_tasks[1]['title'], self.tasks[1]['title'])

if __name__ == '__main__':
    unittest.main()