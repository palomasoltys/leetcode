class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# DFS TRAVERSING


def pre_order_traverse(node):
    if node is None:
        return

    print(node.val)
    pre_order_traverse(node.left)
    pre_order_traverse(node.right)


def in_order_traverse(node):
    if node is None:
        return
    in_order_traverse(node.left)
    print(node.val)
    in_order_traverse(node.right)


def pos_order_traverse(node):
    if node is None:
        return
    pos_order_traverse(node.left)
    pos_order_traverse(node.right)
    print(node.val)


# Create a simple tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Pre order Travese: ")
pre_order_traverse(root)  # 1 2 4 5 3

print("In order traverse: ")
in_order_traverse(root)  # 4 2 5 1 3

print("Pos order traverse: ")
pos_order_traverse(root)  # 4 5 2 3 1

# EXERCISES
# 1. Write a function to count the total number of nodes in a binary tree using any traversal method.


def total_number_of_nodes(node):
    if node is None:
        return 0
    left_node = total_number_of_nodes(node.left)
    right_node = total_number_of_nodes(node.right)

    return left_node + right_node + 1


print("total number os nodes: ")
print(total_number_of_nodes(root))

# 2. Write a function to find the maximum value in a binary tree using any traversal method.


def max_value(node):
    if node is None:
        return 0
    left = max_value(node.left)
    right = max_value(node.right)

    return max(left, right, node.val)


print("Max value: ")
print(max_value(root))

# 3. Write a function that return true if the target exists in the given binary tree otherwise false


def target_exist(node, target):
    if node is None:
        return

    if node.val == target:
        return True

    left = target_exist(node.left, target)
    right = target_exist(node.right, target)

    return left or right


print("Target exists? ")
print(target_exist(root, 4))

# 4. Write a function that returns the sum of all values in the given binary tree


def sum_tree(node):

    if node is None:
        return 0

    left = sum_tree(node.left)
    right = sum_tree(node.right)

    return left + right + node.val


print("Sum of all values are: ")
print(sum_tree(root))

# 5. Write a function that returns the sum of all even values in the given binary tree


def sum_even_numbers(node):
    if node is None:
        return 0

    left = sum_even_numbers(node.left)
    right = sum_even_numbers(node.right)

    if node.val % 2 == 0:
        return node.val + left + right
    else:
        return left + right


print("The sum of all even values are: ")
print(sum_even_numbers(root))
