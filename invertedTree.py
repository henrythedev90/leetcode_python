from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertedTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Invert a binary tree by swapping left and right children recursively
    """
    if not root:
        return None
    
    # Recursively invert left and right subtrees
    left_inverted = invertedTree(root.left)
    right_inverted = invertedTree(root.right)
    
    # Swap left and right children
    root.left = right_inverted
    root.right = left_inverted
    
    return root

# Helper functions for testing
def create_binary_tree(values, index=0):
    """Create a binary tree from a list of values (level-order traversal)"""
    if index >= len(values) or values[index] is None:
        return None
    
    root = TreeNode(values[index])
    root.left = create_binary_tree(values, 2 * index + 1)
    root.right = create_binary_tree(values, 2 * index + 2)
    
    return root

def level_order_traversal(root):
    """Convert binary tree to level-order list (including None for missing nodes)"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append(None)
        
        result.extend(level)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

def print_tree(root, level=0, prefix="Root: "):
    """Print binary tree in a readable format"""
    if not root:
        return
    
    print("  " * level + prefix + str(root.val))
    if root.left:
        print_tree(root.left, level + 1, "L--- ")
    if root.right:
        print_tree(root.right, level + 1, "R--- ")

# Test cases
def test_invertedTree():
    print("=" * 50)
    print("TESTING invertedTree FUNCTION")
    print("=" * 50)
    
    # Test case 1: Simple tree
    print("\nTest 1: Simple tree")
    values1 = [4, 2, 7, 1, 3, 6, 9]
    root1 = create_binary_tree(values1)
    
    print("Original tree:")
    print_tree(root1)
    print("Level order:", level_order_traversal(root1))
    
    inverted1 = invertedTree(root1)
    print("\nInverted tree:")
    print_tree(inverted1)
    print("Level order:", level_order_traversal(inverted1))
    
    expected1 = [4, 7, 2, 9, 6, 3, 1]
    actual1 = level_order_traversal(inverted1)
    print(f"Expected: {expected1}, Got: {actual1}")
    print(f"Pass: {actual1 == expected1}")
    
    # Test case 2: Empty tree
    print("\nTest 2: Empty tree")
    root2 = None
    print("Original tree: None")
    
    inverted2 = invertedTree(root2)
    print("Inverted tree:", "None" if inverted2 is None else "Not None")
    
    expected2 = []
    actual2 = level_order_traversal(inverted2) if inverted2 else []
    print(f"Expected: {expected2}, Got: {actual2}")
    print(f"Pass: {actual2 == expected2}")
    
    # Test case 3: Single node
    print("\nTest 3: Single node")
    values3 = [1]
    root3 = create_binary_tree(values3)
    
    print("Original tree:")
    print_tree(root3)
    print("Level order:", level_order_traversal(root3))
    
    inverted3 = invertedTree(root3)
    print("\nInverted tree:")
    print_tree(inverted3)
    print("Level order:", level_order_traversal(inverted3))
    
    expected3 = [1]
    actual3 = level_order_traversal(inverted3)
    print(f"Expected: {expected3}, Got: {actual3}")
    print(f"Pass: {actual3 == expected3}")
    
    # Test case 4: Left-skewed tree
    print("\nTest 4: Left-skewed tree")
    values4 = [1, 2, None, 3, None, None, None]
    root4 = create_binary_tree(values4)
    
    print("Original tree:")
    print_tree(root4)
    print("Level order:", level_order_traversal(root4))
    
    inverted4 = invertedTree(root4)
    print("\nInverted tree:")
    print_tree(inverted4)
    print("Level order:", level_order_traversal(inverted4))
    
    expected4 = [1, None, 2, None, None, None, 3]
    actual4 = level_order_traversal(inverted4)
    print(f"Expected: {expected4}, Got: {actual4}")
    print(f"Pass: {actual4 == expected4}")
    
    # Test case 5: Right-skewed tree
    print("\nTest 5: Right-skewed tree")
    values5 = [1, None, 2, None, None, None, 3]
    root5 = create_binary_tree(values5)
    
    print("Original tree:")
    print_tree(root5)
    print("Level order:", level_order_traversal(root5))
    
    inverted5 = invertedTree(root5)
    print("\nInverted tree:")
    print_tree(inverted5)
    print("Level order:", level_order_traversal(inverted5))
    
    expected5 = [1, 2, None, 3, None, None, None]
    actual5 = level_order_traversal(inverted5)
    print(f"Expected: {expected5}, Got: {actual5}")
    print(f"Pass: {actual5 == expected5}")
    
    # Test case 6: Complete binary tree
    print("\nTest 6: Complete binary tree")
    values6 = [1, 2, 3, 4, 5, 6, 7]
    root6 = create_binary_tree(values6)
    
    print("Original tree:")
    print_tree(root6)
    print("Level order:", level_order_traversal(root6))
    
    inverted6 = invertedTree(root6)
    print("\nInverted tree:")
    print_tree(inverted6)
    print("Level order:", level_order_traversal(inverted6))
    
    expected6 = [1, 3, 2, 7, 6, 5, 4]
    actual6 = level_order_traversal(inverted6)
    print(f"Expected: {expected6}, Got: {actual6}")
    print(f"Pass: {actual6 == expected6}")
    
    # Test case 7: Tree with missing nodes
    print("\nTest 7: Tree with missing nodes")
    values7 = [1, 2, 3, None, 4, None, 5]
    root7 = create_binary_tree(values7)
    
    print("Original tree:")
    print_tree(root7)
    print("Level order:", level_order_traversal(root7))
    
    inverted7 = invertedTree(root7)
    print("\nInverted tree:")
    print_tree(inverted7)
    print("Level order:", level_order_traversal(inverted7))
    
    expected7 = [1, 3, 2, 5, None, 4, None]
    actual7 = level_order_traversal(inverted7)
    print(f"Expected: {expected7}, Got: {actual7}")
    print(f"Pass: {actual7 == expected7}")
    
    # Test case 8: Large tree
    print("\nTest 8: Large tree")
    values8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    root8 = create_binary_tree(values8)
    
    print("Original tree (first few levels):")
    print_tree(root8)
    print("Level order:", level_order_traversal(root8))
    
    inverted8 = invertedTree(root8)
    print("\nInverted tree (first few levels):")
    print_tree(inverted8)
    print("Level order:", level_order_traversal(inverted8))
    
    expected8 = [1, 3, 2, 7, 6, 5, 4, 15, 14, 13, 12, 11, 10, 9, 8]
    actual8 = level_order_traversal(inverted8)
    print(f"Expected: {expected8}, Got: {actual8}")
    print(f"Pass: {actual8 == expected8}")
    
    # Test case 9: Tree with negative values
    print("\nTest 9: Tree with negative values")
    values9 = [-1, -2, -3, -4, -5]
    root9 = create_binary_tree(values9)
    
    print("Original tree:")
    print_tree(root9)
    print("Level order:", level_order_traversal(root9))
    
    inverted9 = invertedTree(root9)
    print("\nInverted tree:")
    print_tree(inverted9)
    print("Level order:", level_order_traversal(inverted9))
    
    expected9 = [-1, -3, -2, -5, -4]
    actual9 = level_order_traversal(inverted9)
    print(f"Expected: {expected9}, Got: {actual9}")
    print(f"Pass: {actual9 == expected9}")
    
    # Test case 10: Tree with zero values
    print("\nTest 10: Tree with zero values")
    values10 = [0, 0, 0, 1, 2, 3, 4]
    root10 = create_binary_tree(values10)
    
    print("Original tree:")
    print_tree(root10)
    print("Level order:", level_order_traversal(root10))
    
    inverted10 = invertedTree(root10)
    print("\nInverted tree:")
    print_tree(inverted10)
    print("Level order:", level_order_traversal(inverted10))
    
    expected10 = [0, 0, 0, 4, 3, 2, 1]
    actual10 = level_order_traversal(inverted10)
    print(f"Expected: {expected10}, Got: {actual10}")
    print(f"Pass: {actual10 == expected10}")

if __name__ == "__main__":
    test_invertedTree()
