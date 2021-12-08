# A compeleted implementation of a binary tree. 
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




