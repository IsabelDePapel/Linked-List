class Node:
    """Basic Node class to use in singly linked list."""

    def __init__(self, value):
        self._value = value
        self._next_node = None

    # getters and setters
    # only next has a setter
    @property
    def value(self):
        return self._value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        self._next_node = next_node


class LinkedList:
    """Singly linked list class composed of Nodes."""

    def __init__(self):
        self._head = None

    def __str__(self):
        s = ''
        current = self._head

        while current:
            s += str(current.value)
            s += ' -> '  # 4 chars long
            current = current.next_node
        return s[:-4]

    # space: O(1) because it only needs a variable for the new node
    # time: O(1) because it's inserting at the beginning of the list
    # so the amount of work it does is finite and independent of input size
    def insert(self, value):
        """Insert new node with given value at the head of the linked list."""
        new_node = Node(value)

        # if list isn't empty
        if self._head:
            new_node.next_node = self._head

        self._head = new_node

    # space: O(1) because it only needs vars to track current and return value
    # time: O(n) because in the worst case, it has to iterate through the
    # entire list to find the value
    def search(self, value):
        """Search for the given value. Returns True if found; else False."""
        current = self._head

        # iterate through nodes
        while current:
            if current.value == value:
                return True
            current = current.next_node

        return False

    # space: O(1) because memory needed doesn't depend on input size
    # time: O(n) because it has to iterate through the entire list to find
    # the max value
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

    # same as above for space and time
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

    # space: O(1) because it only needs variables to track current and length
    # time: O(n) because it has to iterate through the entire list to find
    # the length
    def length(self):
        len_list = 0
        current = self._head

        while current:
            len_list += 1
            current = current.next_node

        return len_list

    # space: O(1) because it only needs vars to track current and counter
    # time: O(n) where n is the index of the node you want to get
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

    # space: O(1) because memory required is independent of input size
    # time: O(n) because in the worst case, you have to insert the node at
    # the end of the list, which requires iterating through the whole list
    def insert_ascending(self, value):
        """
        Insert new node with the given value in ascending order.

        Assumes the list is already sorted.
        """
        new_node = Node(value)

        # if new node will be first item in list
        if not self._head or value <= self._head.value:
            # check list isn't empty
            if self._head:
                new_node.next_node = self._head

            self._head = new_node
            return

        previous = self._head
        current = previous.next_node

        while current:
            if value <= current.value:
                new_node.next_node = current
                previous.next_node = new_node
                return

            previous = current
            current = current.next_node

        # if value is max item in list
        previous.next_node = new_node

    # space: O(1) because you only need a var to track current node
    # time: O(n) because you have to iterate through all the nodes in the list
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

    # space: O(1) because memory needed is independent of input
    # time: O(n) because in the worst case, the value isn't in the list and
    # you have to iterate through the entire list
    def delete(self, value):
        """
        Delete the first node found with the specified value.

        Returns the deleted node if found; else None.
        """
        # if list is empty
        if not self._head:
            return None

        # if head is the value to delete
        if self._head.value == value:
            deleted = self._head
            self._head = deleted.next_node
            return deleted

        previous = self._head
        current = previous.next_node

        while current:
            if value == current.value:
                previous.next_node = current.next_node
                return current

            previous = current
            current = current.next_node

        return None

    # space: O(1) because you only need to track previous, current, and next
    # time: O(n) because you need to iterate through the entire list to reverse it
    def reverse(self):
        """Reverse the linked list iteratively."""
        # if list is empty or len 1
        if not self._head or not self._head.next_node:
            return

        previous = None
        current = self._head

        while current:
            next_node = current.next_node
            current.next_node = previous

            previous = current
            current = next_node

        self._head = previous

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

        # if even get lower indexed element
        if len_list % 2 == 0:
            return self.find_nth_from_beginning((len_list / 2) - 1)
        else:  # return middle element
            return self.find_nth_from_beginning(len_list // 2)

    # space: O(1) because memory is independent of input
    # time: O(2k), where k is the length of the linked list,
    # (which simplifies to O(k) because you need to iterate once to
    # calculate the length, and once more to retrieve the desired value)
    def find_nth_from_end(self, n):
        """
        Return value of nth node from end of list.

        Assumes last node is index 0. (e.g. 3rd from end is idx -4)
        """
        len_list = self.length()

        if len_list - 1 < n:
            raise IndexError

        return self.find_nth_from_beginning((len_list - 1) - n)

    # space: O(n) because worst case you'll add every element in the
    # list to the set visited
    # time: O(n) because worst case there is no cycle and you have to
    # iterate through the entire list to confirm
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


empty_list = LinkedList()
empty_list.visit()

medium_list = empty_list
medium_list.insert(2)
medium_list.insert(4)
medium_list.visit()
