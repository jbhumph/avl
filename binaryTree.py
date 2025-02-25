class Node:
    def __init__(self, data, temp, tmax, tmin, prcpt):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        self.prcpt = prcpt
        self.temp = temp
        self.tmax = tmax
        self.tmin = tmin


def getHeight(node):
    # return node height
    if not node:
        return 0
    return node.height


def updateHeight(node):
    # updates height
    node.height = max(getHeight(node.left), getHeight(node.right)) + 1

def getPrcpt(node):
    return node.prcpt

def getTemp(node):
    return node.temp


def getBalance(node):
    # returns balance of tree
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)


def leftRotate(z):
    y = z.right
    t2 = y.left
    # Perform rotation
    y.left = z
    z.right = t2
    # Update heights
    updateHeight(z)
    updateHeight(y)
    return y


def rightRotate(z):
    y = z.left
    t3 = y.right
    # Perform rotation
    y.right = z
    z.left = t3
    # Update heights
    updateHeight(z)
    updateHeight(y)
    return y


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 1

    def insert(self, data, temp, tmax, tmin, prcpt):
        self.root = self._insert(self.root, data, temp, tmax, tmin, prcpt)

    def _insert(self, node, data, temp, tmax, tmin, prcpt):
        if not node:
            return Node(data, temp, tmax, tmin, prcpt)
        if data < node.data:
            node.left = self._insert(node.left, data, temp, tmax, tmin, prcpt)
        elif data > node.data:
            node.right = self._insert(node.right, data, temp, tmax, tmin, prcpt)
        else:
            return node

        updateHeight(node)
        balance = getBalance(node)

        if balance > 1 and data < node.left.data:
            return rightRotate(node)
        if balance < -1 and data > node.right.data:
            return leftRotate(node)
        if balance > 1 and data > node.left.data:
            node.left = leftRotate(node.left)
            return rightRotate(node)
        if balance < -1 and data < node.right.data:
            node.right = rightRotate(node.right)
            return leftRotate(node)

        return node

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if not node:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if not node.left or not node.right:
                temp = node.left if node.left else node.right
                if temp is None:
                    node = None
                else:
                    node = temp
            else:
                temp = self.getMinValueNode(node.right)
                node.data = temp.data
                node.right = self._delete(node.right, temp.data)
        if not node:
            return node

        updateHeight(node)
        balance = getBalance(node)

        if balance > 1 and getBalance(node.left) >= 0:
            return rightRotate(node)
        if balance > 1 and getBalance(node.left) < 0:
            node.left = leftRotate(node.left)
            return rightRotate(node)
        if balance < -1 and getBalance(node.right) <= 0:
            return leftRotate(node)
        if balance < -1 and getBalance(node.right) > 0:
            node.right = rightRotate(node.right)
            return leftRotate(node)

        return node

    def getMinValueNode(self, node):
        # Returns the node with the smallest value found in that tree
        if node is None or node.left is None:
            return node
        return self.getMinValueNode(node.left)

    def preOrder(self, node):
        if not node:
            return
        print(node.data, end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)

    def get_root(self):
        return self.root

    def get_size(self):
        return self.size

    def print_tree(self, node):
        if node is None:
            return
        self.print_tree(node.left)
        print(str(node.data) + " " + str(node.temp) + " " + str(node.prcpt))
        self.print_tree(node.right)

    def setArray(self, node, arr):
        if node is None:
            return
        self.setArray(node.left, arr)
        arr.append([node.data, node.temp, node.tmax, node.tmin, node.prcpt])
        self.setArray(node.right, arr)