# Binary Trees

If you have ever done family history, you're familiar with the concept of a family tree. The tree allows you to quickly navigate through your ancestors. It is a wonderful tool
for furthering the lords work, but oddly enough, is also a wonderful tool when used in programming as well!

## What is a Binary Tree?

---

A binary tree is a data structure that places data on either the right or left side of a particular root element. If the value being inserted is less than the root value, it goes to the left. If the value is greater than the root, it falls on the right. Assuming the root's value is roughly the average of all values in the structure, this will result in a balanced binary tree.

## How it works

---

To understand how binary trees work, we need to understand a new concept called recursion.

### Recursion

---

Recursion is the programming principle of iterating a function on an increasingly smaller data set.

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

### Examples

    Coming Soon...
