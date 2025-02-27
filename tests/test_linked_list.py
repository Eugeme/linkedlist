import unittest
from linked_list import LinkedList
import io
import sys

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.llist = LinkedList()

    def test_insert_at_beginning(self):
        self.llist.insert_at_beginning(10)
        self.assertEqual(self.llist.head.data, 10)

        self.llist.insert_at_beginning(20)
        self.assertEqual(self.llist.head.data, 20)
        self.assertEqual(self.llist.head.next.data, 10)

    def test_insert_at_end(self):
        self.llist.insert_at_end(10)
        self.assertEqual(self.llist.head.data, 10)

        self.llist.insert_at_end(20)
        current = self.llist.head
        while current.next:
            current = current.next
        self.assertEqual(current.data, 20)

    def test_insert_at_index(self):
        self.llist.insert_at_end(10)
        self.llist.insert_at_end(20)
        self.llist.insert_at_index(15, 1)

        current = self.llist.head
        self.assertEqual(current.data, 10)
        self.assertEqual(current.next.data, 15)
        self.assertEqual(current.next.next.data, 20)

    def test_remove_at_index(self):
        self.llist.insert_at_end(10)
        self.llist.insert_at_end(20)
        self.llist.insert_at_end(30)

        self.llist.remove_at_index(1)
        current = self.llist.head
        self.assertEqual(current.data, 10)
        self.assertEqual(current.next.data, 30)

    def test_print_linked_list(self):
        self.llist.insert_at_end(10)
        self.llist.insert_at_end(20)
        self.llist.insert_at_end(30)

        captured_output = io.StringIO()
        sys.stdout = captured_output

        self.llist.print_linked_list()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "10\n20\n30")

if __name__ == "__main__":
    unittest.main()