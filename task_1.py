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
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.value <= l2.value:
        result = l1
        result.next = merge_two_sorted_lists(l1.next, l2)
    else:
        result = l2
        result.next = merge_two_sorted_lists(l1, l2.next)
    return result


list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))

print("Реверсований список:")
reversed_list = reverse_list(list1)
while reversed_list:
    print(reversed_list.value, end=" -> ")
    reversed_list = reversed_list.next
print("None")

list3 = ListNode(3, ListNode(1, ListNode(4, ListNode(2))))
print("Відсортований список:")
sorted_list = merge_sort(list3)
while sorted_list:
    print(sorted_list.value, end=" -> ")
    sorted_list = sorted_list.next
print("None")

print("Об'єднаний список:")
merged_list = merge_two_sorted_lists(list1, list2)
while merged_list:
    print(merged_list.value, end=" -> ")
    merged_list = merged_list.next
print("None")
