from typing import Optional


class Node:
    """
    Provide necessary documentation
    """
    def __init__(self, data=None, next=None):
        """
        Provide necessary documentation
        """
        self.data = data
        self.next = next


from typing import Optional


class Node:
    """
    This class describes Node objects to act as elements of the LinkedList
    Attributes:
        -> data - stored associated data
        -> next - link to next node
    """

    def __init__(self, data=None, next=None):
        """
        Initialises the Node with given attributes
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    This class implements LinkedList using Node objects
    Methods:
        -> insert_at_end - inserts node with data at the end of the list
        -> status - displays all elements of the lisT
    Attributes
        -> self.head - contains first node of LinkedList, None if list empty
    """

    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        new = Node(data, None)
        current = self.head
        if current is None:
            self.head = new
        else:
            while current.next is not None:
                current = current.next
            current.next = new

    def status(self):
        """
        It prints all the elements of list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)
        
        

# Do not edit the following code      
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedList
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status()
