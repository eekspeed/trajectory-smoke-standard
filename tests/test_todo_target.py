import unittest

from src.todo_target import todo_target


class TodoTargetTest(unittest.TestCase):
    def test_target(self):
        self.assertEqual(todo_target(), "done")
