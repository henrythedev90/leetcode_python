from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform level-order traversal (breadth-first search) on a binary tree
    Returns a list of lists, where each inner list represents one level
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result

# Helper functions for testing
def create_binary_tree(values, index=0):
    """Create a binary tree from a list of values (level-order traversal)"""
    if index >= len(values) or values[index] is None:
        return None
    
    root = TreeNode(values[index])
    root.left = create_binary_tree(values, 2 * index + 1)
    root.right = create_binary_tree(values, 2 * index + 2)
    
    return root

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
def test_levelOrder():
    print("=" * 50)
    print("TESTING levelOrder FUNCTION")
    print("=" * 50)
    
    # Test case 1: Simple tree
    print("\nTest 1: Simple tree")
    values1 = [3, 9, 20, None, None, 15, 7]
    root1 = create_binary_tree(values1)
    
    print("Tree structure:")
    print_tree(root1)
    
    result1 = levelOrder(root1)
    expected1 = [[3], [9, 20], [15, 7]]
    print(f"Expected: {expected1}")
    print(f"Got: {result1}")
    print(f"Pass: {result1 == expected1}")
    
    # Test case 2: Empty tree
    print("\nTest 2: Empty tree")
    root2 = None
    
    print("Tree structure: None")
    
    result2 = levelOrder(root2)
    expected2 = []
    print(f"Expected: {expected2}")
    print(f"Got: {result2}")
    print(f"Pass: {result2 == expected2}")
    
    # Test case 3: Single node
    print("\nTest 3: Single node")
    values3 = [1]
    root3 = create_binary_tree(values3)
    
    print("Tree structure:")
    print_tree(root3)
    
    result3 = levelOrder(root3)
    expected3 = [[1]]
    print(f"Expected: {expected3}")
    print(f"Got: {result3}")
    print(f"Pass: {result3 == expected3}")
    
    # Test case 4: Complete binary tree
    print("\nTest 4: Complete binary tree")
    values4 = [1, 2, 3, 4, 5, 6, 7]
    root4 = create_binary_tree(values4)
    
    print("Tree structure:")
    print_tree(root4)
    
    result4 = levelOrder(root4)
    expected4 = [[1], [2, 3], [4, 5, 6, 7]]
    print(f"Expected: {expected4}")
    print(f"Got: {result4}")
    print(f"Pass: {result4 == expected4}")
    
    # Test case 5: Left-skewed tree
    print("\nTest 5: Left-skewed tree")
    values5 = [1, 2, None, 3, None, None, None]
    root5 = create_binary_tree(values5)
    
    print("Tree structure:")
    print_tree(root5)
    
    result5 = levelOrder(root5)
    expected5 = [[1], [2], [3]]
    print(f"Expected: {expected5}")
    print(f"Got: {result5}")
    print(f"Pass: {result5 == expected5}")
    
    # Test case 6: Right-skewed tree
    print("\nTest 6: Right-skewed tree")
    values6 = [1, None, 2, None, None, None, 3]
    root6 = create_binary_tree(values6)
    
    print("Tree structure:")
    print_tree(root6)
    
    result6 = levelOrder(root6)
    expected6 = [[1], [2], [3]]
    print(f"Expected: {expected6}")
    print(f"Got: {result6}")
    print(f"Pass: {result6 == expected6}")
    
    # Test case 7: Tree with missing nodes
    print("\nTest 7: Tree with missing nodes")
    values7 = [1, 2, 3, None, 4, None, 5]
    root7 = create_binary_tree(values7)
    
    print("Tree structure:")
    print_tree(root7)
    
    result7 = levelOrder(root7)
    expected7 = [[1], [2, 3], [4, 5]]
    print(f"Expected: {expected7}")
    print(f"Got: {result7}")
    print(f"Pass: {result7 == expected7}")
    
    # Test case 8: Large tree
    print("\nTest 8: Large tree")
    values8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    root8 = create_binary_tree(values8)
    
    print("Tree structure (first few levels):")
    print_tree(root8)
    
    result8 = levelOrder(root8)
    expected8 = [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15]]
    print(f"Expected: {expected8}")
    print(f"Got: {result8}")
    print(f"Pass: {result8 == expected8}")
    
    # Test case 9: Tree with negative values
    print("\nTest 9: Tree with negative values")
    values9 = [-1, -2, -3, -4, -5]
    root9 = create_binary_tree(values9)
    
    print("Tree structure:")
    print_tree(root9)
    
    result9 = levelOrder(root9)
    expected9 = [[-1], [-2, -3], [-4, -5]]
    print(f"Expected: {expected9}")
    print(f"Got: {result9}")
    print(f"Pass: {result9 == expected9}")
    
    # Test case 10: Tree with zero values
    print("\nTest 10: Tree with zero values")
    values10 = [0, 0, 0, 1, 2, 3, 4]
    root10 = create_binary_tree(values10)
    
    print("Tree structure:")
    print_tree(root10)
    
    result10 = levelOrder(root10)
    expected10 = [[0], [0, 0], [1, 2, 3, 4]]
    print(f"Expected: {expected10}")
    print(f"Got: {result10}")
    print(f"Pass: {result10 == expected10}")
    
    # Test case 11: Tree with large numbers
    print("\nTest 11: Tree with large numbers")
    values11 = [1000, 2000, 3000, 4000, 5000]
    root11 = create_binary_tree(values11)
    
    print("Tree structure:")
    print_tree(root11)
    
    result11 = levelOrder(root11)
    expected11 = [[1000], [2000, 3000], [4000, 5000]]
    print(f"Expected: {expected11}")
    print(f"Got: {result11}")
    print(f"Pass: {result11 == expected11}")
    
    # Test case 12: Tree with mixed values
    print("\nTest 12: Tree with mixed values")
    values12 = [1, -2, 3, 0, 5, -6, 7]
    root12 = create_binary_tree(values12)
    
    print("Tree structure:")
    print_tree(root12)
    
    result12 = levelOrder(root12)
    expected12 = [[1], [-2, 3], [0, 5, -6, 7]]
    print(f"Expected: {expected12}")
    print(f"Got: {result12}")
    print(f"Pass: {result12 == expected12}")
    
    # Test case 13: Tree with only left children
    print("\nTest 13: Tree with only left children")
    values13 = [1, 2, None, 3, None, None, None, 4, None, None, None, None, None, None, None]
    root13 = create_binary_tree(values13)
    
    print("Tree structure:")
    print_tree(root13)
    
    result13 = levelOrder(root13)
    expected13 = [[1], [2], [3], [4]]
    print(f"Expected: {expected13}")
    print(f"Got: {result13}")
    print(f"Pass: {result13 == expected13}")
    
    # Test case 14: Tree with only right children
    print("\nTest 14: Tree with only right children")
    values14 = [1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4]
    root14 = create_binary_tree(values14)
    
    print("Tree structure:")
    print_tree(root14)
    
    result14 = levelOrder(root14)
    expected14 = [[1], [2], [3], [4]]
    print(f"Expected: {expected14}")
    print(f"Got: {result14}")
    print(f"Pass: {result14 == expected14}")
    
    # Test case 15: Tree with alternating structure
    print("\nTest 15: Tree with alternating structure")
    values15 = [1, 2, 3, None, 4, 5, None, None, None, 6, 7]
    root15 = create_binary_tree(values15)
    
    print("Tree structure:")
    print_tree(root15)
    
    result15 = levelOrder(root15)
    expected15 = [[1], [2, 3], [4, 5], [6, 7]]
    print(f"Expected: {expected15}")
    print(f"Got: {result15}")
    print(f"Pass: {result15 == expected15}")

if __name__ == "__main__":
    test_levelOrder()