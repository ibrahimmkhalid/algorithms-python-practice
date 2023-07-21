class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def postorder(node):
    if node is None:
        return
    preorder(node.left)
    preorder(node.right)
    print(node.value, end=" ")

def inorder(node):
    if node is None:
        return
    preorder(node.left)
    print(node.value, end=" ")
    preorder(node.right)

def preorder(node):
    if node is None:
        return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)

def getHeight(node, height=0):
    if node is None:
        return height
    height += 1
    lheight = getHeight(node.left, height)
    rheight = getHeight(node.right, height)
    return lheight if rheight < lheight else rheight

class Trunk:
    def __init__(self, prev=None, str=None):
        self.prev = prev
        self.str = str

def showTrunks(p):
    if p is None:
        return
    showTrunks(p.prev)
    print(p.str, end='')

def printTree(root, prev=None, isRight=False): # inorder printing
    if root is None: # base case, do nothing
        return

    prev_str = '    ' # spaces from the left of the screen
    trunk = Trunk(prev, prev_str) # appending previous strings
    printTree(root.right, trunk, True) # recurse right side of the tree

    if prev is None: # root of the tree
        trunk.str = '———'
    elif isRight: # this is to the right of the previous node
        trunk.str = '.———'
        prev_str = '   |' # make space for the previous value
    else:
        trunk.str = '`———' # this is left of the previous node
        prev.str = prev_str

    showTrunks(trunk) # print the appropriate spacing and branches for the current node
    print(' ' + str(root.value))
    if prev:
        prev.str = prev_str
    trunk.str = '   |'
    printTree(root.left, trunk, False) #recurse left side of the tree

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(34)
tree.left.left.left = TreeNode(3847)
tree.left.left.right = TreeNode(329)
tree.right = TreeNode(4)
tree.right.left = TreeNode(32)
tree.right.left.left = TreeNode(23)
tree.right.left.right = TreeNode(66)
tree.right.right = TreeNode(33433)
tree.right.right.right = TreeNode(3847)
tree.right.right.right.left = TreeNode(343897234)
tree.right.right.right.right = TreeNode(384)

preorder(tree)
print()
inorder(tree)
print()
postorder(tree)
print()

print(getHeight(tree))

printTree(tree)
