# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            self.head = newNode
            newNode.next = current
        else:
            self.head = newNode

        print("Inserted node with value at the beginning of list: %s" % str(data))

    # insertion method for the linked list
    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

        print("Inserted node with value at the end of list: %s" % str(data))

    # delete the first occurrence of key in linked list
    def deleteNode(self, key):

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                print("Deleting node with value: %s" % str(key))
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                print("Deleting node with value: %s" % str(key))
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp is None:
            print("Node with value %s not Found for deletion!" % str(key))
            return

        # Unlink the node from linked list
        prev.next = temp.next

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # print method for the linked list
    def printlinkedlist(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # Recursive function to print linked list in reverse order
    def printreverse(self, temp):
        if temp:
            self.printreverse(temp.next)
            print(temp.data)
        else:
            return


# Singly Linked List with insertion and print methods
l = LinkedList()
l.insert_at_end(3)
l.insert_at_end(4)
l.insert_at_begining(7)
l.insert_at_end(5)
l.insert_at_begining(6)

# print list
print("This is the linked list currently:")
l.printlinkedlist()

l.deleteNode(4)
l.deleteNode(1)

# print list
print("This is the linked list currently:")
l.printlinkedlist()

# print list in reverse order
print("Link List Nodes in reverse order are as following:")
l.printreverse(l.head)

# reverse the linked list
l.reverse()

# print reversed linked list
print("This is the revesed linked list:")
l.printlinkedlist()
