import unittest

from src.todo_target import todo_target


class TodoTargetTest(unittest.TestCase):
    def test_target(self):
        self.assertEqual(todo_target("todo"), "done")

    def test_callable(self):
        self.assertTrue(callable(todo_target))

    def test_passthrough(self):
        self.assertEqual(todo_target("already-done"), "already-done")
