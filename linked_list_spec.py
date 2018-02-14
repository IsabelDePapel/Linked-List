import unittest
import linked_list
import doubly_linked_list as dll


class TestNodeClass(unittest.TestCase):
    """Test basic Node class functionality."""

    def setUp(self):
        self.node = linked_list.Node(2)

    def test_value(self):
        self.assertEqual(self.node.value, 2, 'must respond to .value')

    def test_default_next_node(self):
        self.assertIsNone(self.node.next_node, '.next_node must init as None')

    def test_set_next_node(self):
        new_val = 3
        new_node = linked_list.Node(new_val)
        self.node.next_node = new_node
        next_node = self.node.next_node

        self.assertEqual(next_node, new_node, 'incorrect next node')
        self.assertEqual(next_node.value, new_val, 'node val must be ' + str(new_val))


class TestLinkedListClass(unittest.TestCase):
    """Test singly linked list."""

    def setUp(self):
        self.empty_list = linked_list.LinkedList()

        self.small_list = linked_list.LinkedList()
        self.small_list.insert(2)  # list of [2]

        self.medium_list = linked_list.LinkedList()
        self.medium_list.insert(0)
        self.medium_list.insert(-2)
        self.medium_list.insert(10)  # list of [10, -2, 0]

        self.large_list = linked_list.LinkedList()
        self.large_list.insert(20)
        self.large_list.insert(5)
        self.large_list.insert(-3)
        self.large_list.insert(4)
        self.large_list.insert(-3)  # list of [-3, 4, -3, 5, 20]

    def test_insert(self):
        self.assertEqual(str(self.empty_list), '')
        self.assertEqual(str(self.small_list), '2')
        self.assertEqual(str(self.medium_list), '10 -> -2 -> 0')

    def test_length(self):
        self.assertEqual(self.empty_list.length(), 0, 'list must be empty')
        self.assertEqual(self.medium_list.length(), 3, 'incorrect length')
        self.assertEqual(self.large_list.length(), 5, 'incorrect length')

    def test_search(self):
        self.assertFalse(self.empty_list.search(2), 'empty list doesn\'t have 2')
        self.assertTrue(self.small_list.search(2), 'small list has 2')
        self.assertFalse(self.small_list.search(-2))

        self.assertTrue(self.large_list.search(5), 'large list has 2 5s')
        self.assertFalse(self.large_list.search(0))

    def test_find_max(self):
        self.assertIsNone(self.empty_list.find_max())
        self.assertEqual(self.small_list.find_max(), 2)
        self.assertEqual(self.medium_list.find_max(), 10)
        self.assertEqual(self.large_list.find_max(), 20)

    def test_find_min(self):
        self.assertIsNone(self.empty_list.find_min())
        self.assertEqual(self.small_list.find_min(), 2)
        self.assertEqual(self.medium_list.find_min(), -2)
        self.assertEqual(self.large_list.find_min(), -3)

    def test_find_nth_from_beginning(self):
        # check that raises error when index out of range
        with self.assertRaises(IndexError):
            self.empty_list.find_nth_from_beginning(0)
            self.medium_list.find_nth_from_beginning(5)

        self.assertEqual(self.small_list.find_nth_from_beginning(0), 2)
        self.assertEqual(self.medium_list.find_nth_from_beginning(0), 10)
        self.assertEqual(self.medium_list.find_nth_from_beginning(1), -2)
        self.assertEqual(self.medium_list.find_nth_from_beginning(2), 0)
        self.assertEqual(self.large_list.find_nth_from_beginning(4), 20)

    def test_insert_ascending(self):
        lst = self.empty_list
        lst.insert(5)
        self.assertEqual(lst.find_nth_from_beginning(0), 5)

        # test insertion in middle
        lst.insert(4)
        lst.insert(2)  # list of [2, 4, 5]
        lst.insert_ascending(3)
        self.assertEqual(lst.find_nth_from_beginning(1), 3)

        # test insertion at beginning
        lst.insert_ascending(-2)
        self.assertEqual(lst.find_nth_from_beginning(0), -2)

        # test insertion at end
        lst.insert_ascending(10)  # list is [-2, 2, 3, 4, 5, 10]
        self.assertEqual(lst.find_nth_from_beginning(5), 10)

    def test_delete(self):
        self.assertIsNone(self.empty_list.delete(10))

        self.assertEqual(self.small_list.delete(2).value, 2)
        self.assertEqual(self.small_list.length(), 0)

        prev_len = self.medium_list.length()
        self.assertEqual(self.medium_list.delete(0).value, 0)
        self.assertEqual(self.medium_list.length(), prev_len - 1)

        prev_len = self.large_list.length()
        self.assertEqual(self.large_list.delete(-3).value, -3)
        self.assertEqual(self.large_list.length(), prev_len - 1)
        self.assertNotEqual(self.large_list.find_nth_from_beginning(0), -3)

    def test_reverse(self):
        self.empty_list.reverse()
        self.assertEqual(str(self.empty_list), '')

        self.small_list.reverse()
        self.assertEqual(str(self.small_list), '2')

        self.large_list.reverse()
        self.assertEqual(str(self.large_list), '20 -> 5 -> -3 -> 4 -> -3')

    def test_find_nth_from_end(self):
        with self.assertRaises(IndexError):
            self.empty_list.find_nth_from_end(0)
            self.small_list.find_nth_from_end(5)

        self.assertEqual(self.large_list.find_nth_from_end(0), 20)
        self.assertEqual(self.large_list.find_nth_from_end(3), 4)
        self.assertEqual(self.large_list.find_nth_from_end(4), -3)

    def test_has_cycle(self):
        self.assertFalse(self.empty_list.has_cycle())
        self.empty_list.create_cycle()
        self.assertFalse(self.empty_list.has_cycle())

        self.assertFalse(self.small_list.has_cycle())
        self.small_list.create_cycle()
        self.assertTrue(self.small_list.has_cycle())


class TestDoubleNodeClass(unittest.TestCase):
    """
    Test node class for doubly linked list.

    Only tests features different from node class in singly linked list.
    """
    def setUp(self):
        self.node = dll.Node(3)

    def test_default_prev_node(self):
        self.assertIsNone(self.node.prev_node)

    def test_set_prev_node(self):
        new_val = 4
        new_node = dll.Node(new_val)
        self.node.prev_node = new_node
        prev_node = self.node.prev_node

        self.assertEqual(prev_node, new_node)
        self.assertEqual(prev_node.value, new_val)


class TestDoublyLinkedListClass(unittest.TestCase):
    """
    Test doubly linked list.

    Only tests features/implementations different from singly linked list.
    """
    def setUp(self):
        self.empty_list = dll.DoublyLinkedList()

        self.small_list = dll.DoublyLinkedList()
        self.small_list.insert(2)  # list of [2]

        self.medium_list = dll.DoublyLinkedList()
        self.medium_list.insert(0)
        self.medium_list.insert(-2)
        self.medium_list.insert(10)  # list of [10, -2, 0]

        self.large_list = dll.DoublyLinkedList()
        self.large_list.insert(20)
        self.large_list.insert(5)
        self.large_list.insert(-3)
        self.large_list.insert(4)
        self.large_list.insert(-3)  # list of [-3, 4, -3, 5, 20]

    def test_insert(self):
        lst = self.empty_list
        lst.insert(2)
        lst.insert(4)
        self.assertEqual(str(lst), '4 -> 2')

    def test_insert_ascending(self):
        lst = self.empty_list
        lst.insert(4)
        lst.insert(2)
        lst.insert_ascending(3)
        self.assertEqual(lst.find_nth_from_beginning(1), 3)

        lst.insert_ascending(4)  # lst will be [2, 3, 4, 4]
        self.assertEqual(lst.find_nth_from_beginning(3), 4)

    def test_delete(self):
        self.assertIsNone(self.empty_list.delete(2))

        prev_len = self.medium_list.length()
        self.assertEqual(self.medium_list.delete(-2).value, -2)
        self.assertEqual(self.medium_list.length(), prev_len - 1)
        self.assertEqual(str(self.medium_list), '10 -> 0')

    def test_reverse(self):
        self.small_list.reverse()
        self.assertEqual(str(self.small_list), '2')

        self.medium_list.reverse()
        self.assertEqual(str(self.medium_list), '0 -> -2 -> 10')

    def test_find_nth_from_end(self):
        with self.assertRaises(IndexError):
            self.empty_list.find_nth_from_end(2)

        self.assertEqual(self.large_list.find_nth_from_end(0), 20)
        self.assertEqual(self.large_list.find_nth_from_end(4), -3)
        self.assertEqual(self.large_list.find_nth_from_end(1), 5)

    def test_has_cycle(self):
        lst = self.large_list
        self.assertFalse(lst.has_cycle())

        lst.create_cycle()
        self.assertTrue(lst.has_cycle())


if __name__ == '__main__':
    unittest.main()
