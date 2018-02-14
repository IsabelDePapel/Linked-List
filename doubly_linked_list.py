class Node:
    """Basic Node class for doubly linked list."""

    def __init__(self, value):
        self._value = value
        self._prev_node = None
        self._next_node = None

    # getters and setters
    @property
    def value(self):
        return self._value

    @property
    def prev_node(self):
        return self._prev_node

    @property
    def next_node(self):
        return self._next_node

    @prev_node.setter
    def prev_node(self, prev_node):
        self._prev_node = prev_node

    @next_node.setter
    def next_node(self, next_node):
        self._next_node = next_node


class DoublyLinkedList:
    """Doubly Linked List class."""

    def __init__(self):
        self._head = None

    def __str__(self):
        s = ''
        current = self._head

        while current:
            s += str(current.value)
            s += ' -> '
            current = current.next_node
        return s[:-4]

    # space and time same as singly LL
    def insert(self, value):
        """Insert new node with given value at the head of the linked list."""
        new_node = Node(value)

        if self._head:
            new_node.next_node = self._head
            self._head.prev_node = new_node

        self._head = new_node

    # space and time same as singly LL
    def search(self, value):
        """Search for the given value. Returns True if found; else False."""
        current = self._head

        while current:
            if current.value == value:
                return True
            current = current.next_node

        return False

    # space and time same as singly LL
    def find_max(self):
        """Return the max value in the list; returns None if list is empty."""
        # if list is empty
        if not self._head:
            return None

        current = self._head
        max_so_far = float('-Inf')

        while current:
            if current.value > max_so_far:
                max_so_far = current.value
            current = current.next_node

        return max_so_far

    # space and time same as singly LL
    def find_min(self):
        """Return the min value in the list; returns None if list is empty."""
        if not self._head:
            return None

        current = self._head
        min_so_far = float('Inf')

        while current:
            if current.value < min_so_far:
                min_so_far = current.value
            current = current.next_node

        return min_so_far

    # space and time same as singly LL
    def length(self):
        len_list = 0
        current = self._head

        while current:
            len_list += 1
            current = current.next_node

        return len_list

    # space and time same as singly LL
    def find_nth_from_beginning(self, n):
        """
        Return value of nth node in the list.

        Raises error if n is not in list range.
        """
        current = self._head
        counter = 0

        while current:
            if counter == n:
                return current.value

            counter += 1
            current = current.next_node

        raise IndexError

    # space and time same as singly LL
    def insert_ascending(self, value):
        """
        Insert new node with the given value in ascending order.

        Assumes the list is already sorted.
        """
        new_node = Node(value)

        # if inserting at head of list
        if not self._head or value <= self._head.value:
            if self._head:
                new_node.next_node = self._head
                self._head.prev_node = new_node

            self._head = new_node
            return

        current = self._head

        while current.next_node:
            next_node = current.next_node

            if value <= next_node.value:
                new_node.next_node = next_node
                new_node.prev_node = current
                next_node.prev_node = new_node
                current.next_node = new_node
                return

            current = current.next_node

        # if item is added at end of list
        new_node.prev_node = current
        current.next_node = new_node

    # space and time same as singly LL
    def visit(self):
        """
        Print all values in the linked list.

        Prints empty string if list is empty.
        """
        current = self._head

        while current:
            print(current.value, end=' ')
            current = current.next_node

        print('')

    # same as singly LL
    def delete(self, value):
        """
        Delete the first node found with the specified value.

        Returns the deleted node if found; else None.
        """
        current = self._head

        while current:
            if current.value == value:
                current.prev_node.next_node = current.next_node
                current.next_node.prev_node = current.prev_node
                return current
            current = current.next_node

        return None

    # same as singly ll
    def reverse(self):
        """Reverse the linked list iteratively."""
        # if empty or 1 item in list
        if not self._head or not self._head.next_node:
            return

        current = self._head
        prev_node = None

        while current:
            next_node = current.next_node

            current.prev_node = next_node
            current.next_node = prev_node

            prev_node = current
            current = next_node

        self._head = prev_node

    # same as singly LL
    def find_middle_value(self):
        """
        Return value at middle node in list.

        If length is odd, returns middle node. If even, returns middle
        rounded down (e.g. length 10 will return element at index 4).

        Returns None if list is empty.
        """
        if not self._head:
            return None

        len_list = self.length()

        # if len is even, return lower indexed element
        if len_list % 2 == 0:
            return self.find_nth_from_beginning((len_list / 2) - 1)
        else:
            return self.find_nth_from_beginning(len_list // 2)

    # space: O(1) because it only needs vars to track current, length, and range
    # per python docs, amount of memory required for range object is
    # constant, no matter the size of the range it represents
    # time: O(k + n) where k is the length of the list and n is the desired index.
    # If n is the first element in the list, this is the same as O(2k)
    def find_nth_from_end(self, n):
        """
        Return value of nth node from end of list.

        Assumes last node is index 0. (e.g. 3rd from end is idx -4).

        Uses counter instead of length() to only iterate once through list.
        """
        current = self._head
        len_list = 0

        while current and current.next_node:
            len_list += 1
            current = current.next_node

        # add 1 to len list since loop only iterates through penultimate node
        len_list += 1

        # check n is in range
        if len_list - 1 < n:
            raise IndexError

        # iterate backward to find nth node
        for idx in range(n):
            current = current.prev_node
        return current.value

    # space and time same as singly LL
    def has_cycle(self):
        current = self._head
        visited = set()

        while current:
            if current in visited:
                return True

            visited.add(current)
            current = current.next_node

        return False

    def create_cycle(self):
        """Create a cycle for testing purposes."""
        # do nothing if empty list
        if not self._head:
            return

        current = self._head

        while current.next_node:
            current = current.next_node

        # cycle back to head
        current.next_node = self._head
        self._head.prev_node = current.next_node
