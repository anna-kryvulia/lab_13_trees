class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    if node == None:
        return []
    l = [node.value]
    n = node
    queue = [n]
    while queue:
        n = queue.pop(0)
        if n:
            if n.left:
                l.append(n.left.value)
                queue.append(n.left)
            if n.right:
                l.append(n.right.value)
                queue.append(n.right)
        else:
            break
    return l
