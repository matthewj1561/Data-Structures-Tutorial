
"""
Student Problem

Implement a function in the BST class that allows allows for an element to be 
deleted from the structure.
"""




class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root == None:
          self.root = BST.Node(data)
        else: 
          self._insert(data, self.root) #Starting at the root node

    def delete(self, data):
      if self.root == None:
        self.root = BST.Node(data)
      else:
        self._deleteNode(self.root, data)

    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data < node.data:
          if node.left is None:
            node.left = BST.Node(data)
          else:
            self._insert(data, node.left)
        else:
          if node.right is None:
            node.right = BST.Node(data)
          else:
            self._insert(data, node.right)
    def minValueNode(self,node):
      current = node
  
      # loop down to find the leftmost leaf
      while(current.left is not None):
          current = current.left
  
      return current
  
  # Given a binary search tree and a data, this function
  # delete the data and returns the new root
 
 
    def _deleteNode(self, root, data):

      # Base Case
      if root is None:
        return root

      # If the data to be deleted
      # is smaller than the root's
      # data then it lies in  left subtree
      if data < root.data:
        root.left = self._deleteNode(root.left, data)

      # If the kye to be delete
      # is greater than the root's data
      # then it lies in right subtree
      elif(data > root.data):
        root.right = self._deleteNode(root.right, data)

      # If data is same as root's data, then this is the node
      # to be deleted
      else:

          # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = self.minValueNode(root.right)

        # Copy the inorder successor's
        # content to this node
        root.data = temp.data

        # Delete the inorder successor
        root.right = self._deleteNode(root.right, temp.data)

      return root


         
    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
        the root of the BST.           
        """
        yield from self._traverse_forward(self.root)

        
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
          yield from self._traverse_forward(node.left)
          yield node.data
          yield from self._traverse_forward(node.right)
 
tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(10)
tree.insert(1)
#5, 3, 7, 10, 1

tree.delete(10)
tree.delete(5)

for n in tree:
    print(n)
#1, 3, 7

