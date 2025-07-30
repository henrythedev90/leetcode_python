import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists into one sorted linked list using a min heap
    """
    if not lists:
        return None
    
    # Create a min heap to store the first node from each list
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    # Create a dummy node to build the result list
    dummy = ListNode(-1)
    tail = dummy
    
    # Process nodes from the heap
    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        
        # Add the next node from the same list to the heap
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

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

def linked_list_to_list(head):
    """Convert a linked list to a Python list"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def print_linked_list(head):
    """Print a linked list in a readable format"""
    values = linked_list_to_list(head)
    print(" -> ".join(map(str, values)) if values else "Empty list")

# Test cases
def test_mergeKLists():
    print("=" * 50)
    print("TESTING mergeKLists FUNCTION")
    print("=" * 50)
    
    # Test case 1: Normal case with 3 sorted lists
    print("\nTest 1: Normal case with 3 sorted lists")
    list1 = create_linked_list([1, 4, 5])
    list2 = create_linked_list([1, 3, 4])
    list3 = create_linked_list([2, 6])
    lists1 = [list1, list2, list3]
    
    print("List 1:", end=" ")
    print_linked_list(list1)
    print("List 2:", end=" ")
    print_linked_list(list2)
    print("List 3:", end=" ")
    print_linked_list(list3)
    
    result1 = mergeKLists(lists1)
    print("Merged:", end=" ")
    print_linked_list(result1)
    
    expected1 = [1, 1, 2, 3, 4, 4, 5, 6]
    actual1 = linked_list_to_list(result1)
    print(f"Expected: {expected1}, Got: {actual1}")
    print(f"Pass: {actual1 == expected1}")
    
    # Test case 2: Empty lists
    print("\nTest 2: Empty lists")
    lists2 = []
    result2 = mergeKLists(lists2)
    print("Input: []")
    print("Merged:", end=" ")
    print_linked_list(result2)
    
    expected2 = []
    actual2 = linked_list_to_list(result2) if result2 else []
    print(f"Expected: {expected2}, Got: {actual2}")
    print(f"Pass: {actual2 == expected2}")
    
    # Test case 3: Lists with empty lists
    print("\nTest 3: Lists with empty lists")
    list3_1 = create_linked_list([1, 2, 3])
    list3_2 = None
    list3_3 = create_linked_list([4, 5, 6])
    lists3 = [list3_1, list3_2, list3_3]
    
    print("List 1:", end=" ")
    print_linked_list(list3_1)
    print("List 2: None")
    print("List 3:", end=" ")
    print_linked_list(list3_3)
    
    result3 = mergeKLists(lists3)
    print("Merged:", end=" ")
    print_linked_list(result3)
    
    expected3 = [1, 2, 3, 4, 5, 6]
    actual3 = linked_list_to_list(result3)
    print(f"Expected: {expected3}, Got: {actual3}")
    print(f"Pass: {actual3 == expected3}")
    
    # Test case 4: Single list
    print("\nTest 4: Single list")
    list4 = create_linked_list([1, 2, 3, 4, 5])
    lists4 = [list4]
    
    print("List:", end=" ")
    print_linked_list(list4)
    
    result4 = mergeKLists(lists4)
    print("Merged:", end=" ")
    print_linked_list(result4)
    
    expected4 = [1, 2, 3, 4, 5]
    actual4 = linked_list_to_list(result4)
    print(f"Expected: {expected4}, Got: {actual4}")
    print(f"Pass: {actual4 == expected4}")
    
    # Test case 5: All empty lists
    print("\nTest 5: All empty lists")
    lists5 = [None, None, None]
    
    print("Input: [None, None, None]")
    result5 = mergeKLists(lists5)
    print("Merged:", end=" ")
    print_linked_list(result5)
    
    expected5 = []
    actual5 = linked_list_to_list(result5) if result5 else []
    print(f"Expected: {expected5}, Got: {actual5}")
    print(f"Pass: {actual5 == expected5}")
    
    # Test case 6: Lists with different lengths
    print("\nTest 6: Lists with different lengths")
    list6_1 = create_linked_list([1, 3, 5, 7, 9])
    list6_2 = create_linked_list([2, 4])
    list6_3 = create_linked_list([6, 8, 10])
    lists6 = [list6_1, list6_2, list6_3]
    
    print("List 1:", end=" ")
    print_linked_list(list6_1)
    print("List 2:", end=" ")
    print_linked_list(list6_2)
    print("List 3:", end=" ")
    print_linked_list(list6_3)
    
    result6 = mergeKLists(lists6)
    print("Merged:", end=" ")
    print_linked_list(result6)
    
    expected6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    actual6 = linked_list_to_list(result6)
    print(f"Expected: {expected6}, Got: {actual6}")
    print(f"Pass: {actual6 == expected6}")
    
    # Test case 7: Negative numbers
    print("\nTest 7: Negative numbers")
    list7_1 = create_linked_list([-5, -3, -1])
    list7_2 = create_linked_list([-4, -2, 0])
    list7_3 = create_linked_list([-6, -4, -2])
    lists7 = [list7_1, list7_2, list7_3]
    
    print("List 1:", end=" ")
    print_linked_list(list7_1)
    print("List 2:", end=" ")
    print_linked_list(list7_2)
    print("List 3:", end=" ")
    print_linked_list(list7_3)
    
    result7 = mergeKLists(lists7)
    print("Merged:", end=" ")
    print_linked_list(result7)
    
    expected7 = [-6, -5, -4, -4, -3, -2, -2, -1, 0]
    actual7 = linked_list_to_list(result7)
    print(f"Expected: {expected7}, Got: {actual7}")
    print(f"Pass: {actual7 == expected7}")
    
    # Test case 8: Large lists
    print("\nTest 8: Large lists")
    list8_1 = create_linked_list([1, 4, 7, 10, 13])
    list8_2 = create_linked_list([2, 5, 8, 11, 14])
    list8_3 = create_linked_list([3, 6, 9, 12, 15])
    lists8 = [list8_1, list8_2, list8_3]
    
    print("List 1:", end=" ")
    print_linked_list(list8_1)
    print("List 2:", end=" ")
    print_linked_list(list8_2)
    print("List 3:", end=" ")
    print_linked_list(list8_3)
    
    result8 = mergeKLists(lists8)
    print("Merged:", end=" ")
    print_linked_list(result8)
    
    expected8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    actual8 = linked_list_to_list(result8)
    print(f"Expected: {expected8}, Got: {actual8}")
    print(f"Pass: {actual8 == expected8}")
    
    # Test case 9: Duplicate values
    print("\nTest 9: Duplicate values")
    list9_1 = create_linked_list([1, 1, 2, 2])
    list9_2 = create_linked_list([1, 2, 3, 3])
    list9_3 = create_linked_list([2, 3, 4, 4])
    lists9 = [list9_1, list9_2, list9_3]
    
    print("List 1:", end=" ")
    print_linked_list(list9_1)
    print("List 2:", end=" ")
    print_linked_list(list9_2)
    print("List 3:", end=" ")
    print_linked_list(list9_3)
    
    result9 = mergeKLists(lists9)
    print("Merged:", end=" ")
    print_linked_list(result9)
    
    expected9 = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4]
    actual9 = linked_list_to_list(result9)
    print(f"Expected: {expected9}, Got: {actual9}")
    print(f"Pass: {actual9 == expected9}")
    
    # Test case 10: Single element lists
    print("\nTest 10: Single element lists")
    list10_1 = create_linked_list([5])
    list10_2 = create_linked_list([2])
    list10_3 = create_linked_list([8])
    list10_4 = create_linked_list([1])
    lists10 = [list10_1, list10_2, list10_3, list10_4]
    
    print("List 1:", end=" ")
    print_linked_list(list10_1)
    print("List 2:", end=" ")
    print_linked_list(list10_2)
    print("List 3:", end=" ")
    print_linked_list(list10_3)
    print("List 4:", end=" ")
    print_linked_list(list10_4)
    
    result10 = mergeKLists(lists10)
    print("Merged:", end=" ")
    print_linked_list(result10)
    
    expected10 = [1, 2, 5, 8]
    actual10 = linked_list_to_list(result10)
    print(f"Expected: {expected10}, Got: {actual10}")
    print(f"Pass: {actual10 == expected10}")

if __name__ == "__main__":
    test_mergeKLists()
