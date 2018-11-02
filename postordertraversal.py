# left, right, root

# Given
# a
# binary
# tree, find
# the
# length
# of
# the
# longest
# path
# where
# each
# node in the
# path
# has
# the
# same
# value.This
# path
# may or may
# not
# pass
# through
# the
# root.
#
# 5
# / \
#     4
# 5
# /  \ \
#     1
# 1
# 5
#
# # Return 2
#
# 4
# / \
#     2
# 5
# 2
# 0
# /  \ \
#     5
# 5
# 1
# 0
# 0
#
# 1
# 2
# 2

# Return
# 2
# result = 0
# postorder(None)


def postorder(node):
    if node == None:
        return 0

    if node.left == None and node.right == None:
        return 0

    # Key Takeaway:
    left = postorder(node.left)  # 2
    right = postorder(node.right)  # 2

    if node.left == node.root:
        left += 1
    else:
        left = 0

    if node.right == node.root:
        right += 1
    else:
        right = 0

    result = max(result, left + right)

    return left + right

    # visit(node) # use resL, resR


class Node:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None


def traverse(tree):
    if self.left == None and self.right == None:
        return 0
    elif node.left:
        traverse(self.left)
    else:
        traverse(self.right)
