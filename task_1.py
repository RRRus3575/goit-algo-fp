class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def merge_sort(head):
    if not head or not head.next:
        return head

    def get_middle(head):
        if not head:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = sorted_merge(left, right)
    return sorted_list

def sorted_merge(a, b):
    if not a:
        return b
    if not b:
        return a

    if a.value <= b.value:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)
    return result

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.value <= l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2

    return dummy.next

def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")


list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))

print("Реверсований список:")
reversed_list = reverse_list(list1)
print_list(reversed_list)

list3 = ListNode(3, ListNode(1, ListNode(4, ListNode(2))))
print("Відсортований список:")
sorted_list = merge_sort(list3)
print_list(sorted_list)

list1 = ListNode(1, ListNode(3, ListNode(5)))  
print("Об'єднаний список:")
merged_list = merge_two_sorted_lists(list1, list2)
print_list(merged_list)
