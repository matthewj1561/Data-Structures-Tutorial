# Stacks

Picture the following scenario. You, an avid football fan, have gotten the unique opportunity to view this year's SuperBowl. You watch the game on the edge of your seat,
continually being drawn in by the battle between the two teams. Suddenly, the quarterback is sacked. Though the play is over, the opposing team continues to pile on top of the downed quarterback. Soon, there is a large pile of bodies in the middle of the field. Eventually, the pile begins to disperse, the top-most player getting off first. The quarterback, who is at the bottom of the heap, only emerges after everyone of the previous attackers get up. Though a bit of a stretch, this is a real world example of a stack.
![football](images/football.jpg)

## What is a stack?

---

In programming terms, a stack is a data structure that utilizes a languages built-in array functionality. A stack only allows data to be removed and inserted at the very end
of the array. This is what causes the stack to be commonly referred to as "Last in, First out" or LIFO.

<img src="images/stack.jpeg"
     alt="Balanced Tree"
     style="width: 350px;" />

## How it works

---
In python, we can use a list to represent a stack.
```python
stack = []
```

To add an element to a stack, we use a **push** operation. In our sports example, every time a player jumped onto the dogpile, they performed a push operation. 
```python
stack.append(3)
stack.append(5)
stack.append(9)
print(stack)
---
[5,5,9]
```

Now we only have access to the last element in the list. We cannot access any element in the middle, or else we would be sacrificing the stack's benefits. We can access the last item like so:
```python
stack[len(stack) - 1]
```

When we remove an element from the top of the heap, we call this a **pop** operation. Each player who climbed off the pile was performing a pop operation. The python example can be executed as follows:
```python
stack.pop()
```

## Why use it?

---

The stack is a powerful tool because of the nature of the push and pop operations. If we always know where the last item add resides (the end of the stack), then we can always get that element very quickly. The stack offers the functionality for an "undo" button, because we always know what was last put in.

## Limitations

---

The stack excels when you need to keep track of the last item you added. Any other use case renders the stack very ineffective. If you needed to access the first item in the list, you would need to pop all of the other elements in front of it. This is a very expensive operation, and also gets rid of all your other data.

## Time Complexity

---

Stacks have very good performance. Since the only operations are pushing and popping off the end of the stack, than we can say that the stack operates in O(1) time. This occurs regardless of the size of the stack.

## Problems
---
Example Problem

A functional use of a stack

Print out the first item in a stack.
```python
stack = [3, 6, 8, 4, 9, 6, 3, 26]

iterations = len(stack) - 1
for i in range(0, iterations):
    stack.pop()

print(stack[len(stack) - 1])

---
3
```
Your task is to create a program that can do the following:
- Take in a string from a user
- Print the given string in a the format of a list
- Based on user input, remove the last element of that array in whatever order the user desires

A solution to this problem can be found here:

[Stack Problem 2 Solution](py_files/stacks2.py)

