# Linked Lists

Stacks are a powerful tool, but as previously discussed, we can't change any elements that are not at the end of the array. Doing so would result in a O(n) operation. The linked list is the solution to this problem.

## What is a Linked List?

---

A Linked List is a unique type of data structure that allows us to add and remove elements from array without having to shift elements in a O(n) operation. The type of linked list we will be referring to is called a doubly linked list.

![A Doubly Linked List](images/linkedList.jpg)

## How it works

---

In a linked list, you do not have to have elements stored in contiguous memory. Instead, all we need to do is have each element point to the previous and next element in the array. A linked list starts out with a head and ends with a tail. We always have access to these two elements. To find an element in an array, we can search forward from the head or backwards from the tail n amount of times until we reach the desired element.

An empty shell of a linked list can be made using classes in python.

```python
class LinkedList:


    class Node:


        def __init__(self, data):
            """
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None
```

To see a basic use of this code, we first need to make a head and tail of the linked list.

Initializing the linked lists

```python
LL = LinkedList()
```

Adding the head

```python
LL.head = Node(1)
LL.head.next = LL.tail
```

Adding the tail

```python
LL.tail = Node(3)
LL.tail.prev = LL.head
```

Adding an element after the head

```python
newNode = Node(2)
LL.head.next = newNode
newNode.prev = LL.head
LL.tail.prev = newNode
newNode.next = LL.tail
```

## Why use it?

---

Since linked lists are basically a collection of pointers, adding and removing elements in a linked list is a very efficient operation.

## Limitations

---

Linked lists are not contiguous in memory, and thus we do not have the O(1) look-up time we have in a normal array. We must actually traverse the list until we find the element, which can be expensive.

## Time Complexity

---

If we are accessing a linked list at the head or tail, we have an immiediete O(1) lookup. If we have a element in the middle, it will take O(n) time to reach the element.
However, modifying an element after it is found is only an O(1) operation.

## Problems

---

1. An implementation of a linked list in python.

    ```python
    class LinkedList:
        """
        Implement the LinkedList data structure.  The Node class below is an
        inner class.  An inner class means that its real name is related to
        the outer class.  To create a Node object, we will need to
        specify LinkedList.Node
        """

        class Node:
            """
            Each node of the linked list will have data and links to the
            previous and next node.
            """

            def __init__(self, data):
                """
                Initialize the node to the data provided.  Initially
                the links are unknown so they are set to None.
                """
                self.data = data
                self.next = None
                self.prev = None

        def __init__(self):
            """
            Initialize an empty linked list.
            """
            self.head = None
            self.tail = None

        def insert_head(self, value):
            """
            Insert a new node at the front (i.e. the head) of the
            linked list.
            """
            # Create the new node
            new_node = LinkedList.Node(value)

            # If the list is empty, then point both head and tail
            # to the new node.
            if self.head is None:
            self.head = new_node
            self.tail = new_node
            # If the list is not empty, then only self.head will be
            # affected.
            else:
            new_node.next = self.head
                # Connect new node to the previous head
            self.head.prev = new_node
                # Connect the previous head to the new node
            self.head = new_node
                # Update the head to point to the new node

        def remove_head(self):
            """
            Remove the first node (i.e. the head) of the linked list.
            """
            # If the list has only one item in it, then set head and tail
            # to None resulting in an empty list.
            if self.head == self.tail:
                pass
            # If the list has more than one item in it, then only self.head
            # will be affected.
            elif self.head is not None:
                self.head.next.prev = None
                self.head = self.head.next
                # Disconnect the second node from the first node
                # Update the head to point to the second node

        def insert_after(self, value, new_value):
            """
            Insert 'new_value' after the first occurance of 'value' in
            the linked list.
            """
            # Search for the node that matches 'value' by starting at the
            # head of the list.
            curr = self.head
            while curr is not None:
                if curr.data == value:
                    # If the location of 'value' is at the end of the list,
                    # then we will affect the self.tail.
                    if curr == self.tail:
                        new_node = LinkedList.Node(new_value)
                        # Connect the new node to the current tail
                        new_node.prev = self.tail
                        # Connect the current tail to the new node
                        self.tail.next = new_node
                        # Set the tail to the new node
                        self.tail = new_node
                    # For any other location of 'value', need to create a
                    # new node and reconenct the links to insert.
                    else:
                        new_node = LinkedList.Node(new_value)
                        # Connect new node to the node containing 'value'
                        new_node.prev = curr
                        # Connect new node to the node after 'value'
                        new_node.next = curr.next
                        # Connect node after 'value' to the new node
                        curr.next.prev = new_node
                        # Connect the node containing 'value' to the new node
                        curr.next = new_node
                    return # We can exit the function after we insert
                curr = curr.next # Go to the next node to search for 'value'

        def __iter__(self):
            """
            Iterate foward through the Linked List
            """
            curr = self.head  # Start at the begining since this is a forward iteration.


        def __str__(self):
            """
            Return a string representation of the linked list.
            """
            output = "linkedlist["
            first = True
            curr = self.head
            while curr is not None:
                if first:
                    first = False
                else:
                    output += ", "
                output += str(curr.data)
                curr = curr.next
            output += "]"
            return output
    ```

2. Your task

    You are given the head of a linked list. You must determine if the list is a palindrome, as in it can be reversed and still be the same list.

    Example:

    Input: head = [1,2,2,1]

    Output: true

    Use this format to start your program:

    ```python
    class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    class Solution:
        def isPalindrome(self, head: Optional[ListNode]) -> bool:

    ```

    A solution can be found [here](py_files/linkedlistsol.py)
