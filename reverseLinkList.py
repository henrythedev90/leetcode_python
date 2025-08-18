from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev

def hasCycle(head: Optional[ListNode]) -> bool:

    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def create_cycle_linked_list(values, cycle_start_index):
    """
    Create a linked list with a cycle starting at the specified index
    cycle_start_index: 0-indexed position where the cycle starts
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    # Create all nodes
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    # Create cycle if cycle_start_index is valid
    if 0 <= cycle_start_index < len(values):
        cycle_node = head
        for _ in range(cycle_start_index):
            cycle_node = cycle_node.next
        current.next = cycle_node  # Point last node to cycle start
    
    return head

def linked_list_to_list(head):
    """Convert a linked list to a Python list (only works for acyclic lists)"""
    result = []
    current = head
    visited = set()
    
    while current:
        if current in visited:
            break  # Stop if we detect a cycle
        visited.add(current)
        result.append(current.val)
        current = current.next
    
    return result

def print_linked_list(head):
    """Print a linked list in a readable format"""
    values = linked_list_to_list(head)
    print(" -> ".join(map(str, values)) if values else "Empty list")

# Test cases for reverseLinkedList
def test_reverseLinkedList():
    # Test case 1: Normal linked list
    print("Test 1: Normal linked list")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print("Original:", end=" ")
    print_linked_list(head1)
    
    reversed1 = reverseLinkedList(head1)
    print("Reversed:", end=" ")
    print_linked_list(reversed1)
    
    expected1 = [5, 4, 3, 2, 1]
    result1 = linked_list_to_list(reversed1)
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Pass: {result1 == expected1}")
    print()
    
    # Test case 2: Single node
    print("Test 2: Single node")
    head2 = create_linked_list([42])
    print("Original:", end=" ")
    print_linked_list(head2)
    
    reversed2 = reverseLinkedList(head2)
    print("Reversed:", end=" ")
    print_linked_list(reversed2)
    
    expected2 = [42]
    result2 = linked_list_to_list(reversed2)
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Pass: {result2 == expected2}")
    print()
    
    # Test case 3: Empty list
    print("Test 3: Empty list")
    head3 = create_linked_list([])
    print("Original: Empty list")
    
    reversed3 = reverseLinkedList(head3)
    print("Reversed:", end=" ")
    print_linked_list(reversed3)
    
    expected3 = []
    result3 = linked_list_to_list(reversed3)
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Pass: {result3 == expected3}")
    print()
    
    # Test case 4: Two nodes
    print("Test 4: Two nodes")
    head4 = create_linked_list([10, 20])
    print("Original:", end=" ")
    print_linked_list(head4)
    
    reversed4 = reverseLinkedList(head4)
    print("Reversed:", end=" ")
    print_linked_list(reversed4)
    
    expected4 = [20, 10]
    result4 = linked_list_to_list(reversed4)
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"Pass: {result4 == expected4}")
    print()
    
    # Test case 5: Large list
    print("Test 5: Large list")
    head5 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("Original:", end=" ")
    print_linked_list(head5)
    
    reversed5 = reverseLinkedList(head5)
    print("Reversed:", end=" ")
    print_linked_list(reversed5)
    
    expected5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    result5 = linked_list_to_list(reversed5)
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"Pass: {result5 == expected5}")
    print()
    
    # Test case 6: All same values
    print("Test 6: All same values")
    head6 = create_linked_list([5, 5, 5, 5, 5])
    print("Original:", end=" ")
    print_linked_list(head6)
    
    reversed6 = reverseLinkedList(head6)
    print("Reversed:", end=" ")
    print_linked_list(reversed6)
    
    expected6 = [5, 5, 5, 5, 5]
    result6 = linked_list_to_list(reversed6)
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"Pass: {result6 == expected6}")
    print()
    
    # Test case 7: Negative numbers
    print("Test 7: Negative numbers")
    head7 = create_linked_list([-1, -2, -3, -4, -5])
    print("Original:", end=" ")
    print_linked_list(head7)
    
    reversed7 = reverseLinkedList(head7)
    print("Reversed:", end=" ")
    print_linked_list(reversed7)
    
    expected7 = [-5, -4, -3, -2, -1]
    result7 = linked_list_to_list(reversed7)
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"Pass: {result7 == expected7}")
    print()
    
    # Test case 8: Mixed positive and negative
    print("Test 8: Mixed positive and negative")
    head8 = create_linked_list([1, -2, 3, -4, 5])
    print("Original:", end=" ")
    print_linked_list(head8)
    
    reversed8 = reverseLinkedList(head8)
    print("Reversed:", end=" ")
    print_linked_list(reversed8)
    
    expected8 = [5, -4, 3, -2, 1]
    result8 = linked_list_to_list(reversed8)
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"Pass: {result8 == expected8}")
    print()
    
    # Test case 9: Palindrome-like structure
    print("Test 9: Palindrome-like structure")
    head9 = create_linked_list([1, 2, 3, 2, 1])
    print("Original:", end=" ")
    print_linked_list(head9)
    
    reversed9 = reverseLinkedList(head9)
    print("Reversed:", end=" ")
    print_linked_list(reversed9)
    
    expected9 = [1, 2, 3, 2, 1]
    result9 = linked_list_to_list(reversed9)
    print(f"Expected: {expected9}, Got: {result9}")
    print(f"Pass: {result9 == expected9}")
    print()
    
    # Test case 10: Large numbers
    print("Test 10: Large numbers")
    head10 = create_linked_list([1000, 2000, 3000, 4000, 5000])
    print("Original:", end=" ")
    print_linked_list(head10)
    
    reversed10 = reverseLinkedList(head10)
    print("Reversed:", end=" ")
    print_linked_list(reversed10)
    
    expected10 = [5000, 4000, 3000, 2000, 1000]
    result10 = linked_list_to_list(reversed10)
    print(f"Expected: {expected10}, Got: {result10}")
    print(f"Pass: {result10 == expected10}")
    print()

# Test cases for hasCycle
def test_hasCycle():
    print("=" * 50)
    print("TESTING hasCycle FUNCTION")
    print("=" * 50)
    
    # Test case 1: No cycle
    print("\nTest 1: No cycle")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print("List: 1 -> 2 -> 3 -> 4 -> 5")
    result1 = hasCycle(head1)
    expected1 = False
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Pass: {result1 == expected1}")
    
    # Test case 2: Cycle at beginning
    print("\nTest 2: Cycle at beginning")
    head2 = create_cycle_linked_list([1, 2, 3, 4, 5], 0)
    print("List: 1 -> 2 -> 3 -> 4 -> 5 -> 1 (cycle at node 1)")
    result2 = hasCycle(head2)
    expected2 = True
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Pass: {result2 == expected2}")
    
    # Test case 3: Cycle in middle
    print("\nTest 3: Cycle in middle")
    head3 = create_cycle_linked_list([1, 2, 3, 4, 5], 2)
    print("List: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle at node 3)")
    result3 = hasCycle(head3)
    expected3 = True
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Pass: {result3 == expected3}")
    
    # Test case 4: Cycle at end
    print("\nTest 4: Cycle at end")
    head4 = create_cycle_linked_list([1, 2, 3, 4, 5], 4)
    print("List: 1 -> 2 -> 3 -> 4 -> 5 -> 5 (cycle at node 5)")
    result4 = hasCycle(head4)
    expected4 = True
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"Pass: {result4 == expected4}")
    
    # Test case 5: Empty list
    print("\nTest 5: Empty list")
    head5 = create_linked_list([])
    print("List: Empty")
    result5 = hasCycle(head5)
    expected5 = False
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"Pass: {result5 == expected5}")
    
    # Test case 6: Single node (no cycle)
    print("\nTest 6: Single node (no cycle)")
    head6 = create_linked_list([42])
    print("List: 42")
    result6 = hasCycle(head6)
    expected6 = False
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"Pass: {result6 == expected6}")
    
    # Test case 7: Two nodes (no cycle)
    print("\nTest 7: Two nodes (no cycle)")
    head7 = create_linked_list([1, 2])
    print("List: 1 -> 2")
    result7 = hasCycle(head7)
    expected7 = False
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"Pass: {result7 == expected7}")
    
    # Test case 8: Two nodes with cycle
    print("\nTest 8: Two nodes with cycle")
    head8 = create_cycle_linked_list([1, 2], 0)
    print("List: 1 -> 2 -> 1 (cycle)")
    result8 = hasCycle(head8)
    expected8 = True
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"Pass: {result8 == expected8}")
    
    # Test case 9: Large cycle
    print("\nTest 9: Large cycle")
    head9 = create_cycle_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
    print("List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 4 (cycle at node 4)")
    result9 = hasCycle(head9)
    expected9 = True
    print(f"Expected: {expected9}, Got: {result9}")
    print(f"Pass: {result9 == expected9}")
    
    # Test case 10: Self-loop
    print("\nTest 10: Self-loop")
    head10 = create_cycle_linked_list([1], 0)
    print("List: 1 -> 1 (self-loop)")
    result10 = hasCycle(head10)
    expected10 = True
    print(f"Expected: {expected10}, Got: {result10}")
    print(f"Pass: {result10 == expected10}")

if __name__ == "__main__":
    test_reverseLinkedList()
    test_hasCycle()