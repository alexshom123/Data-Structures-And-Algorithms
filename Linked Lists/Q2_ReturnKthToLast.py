
# Question - 2: return nth element from the end of Linked List

from LinkedListQuestionsBase import LinkedList

def nthToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    # Set pointer 2 n nodes apart from pointer 1
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    # Pointer 2 will reach end before pointer 1, which will b n elements from last
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

# Trial
customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
# Try getting 3rd element from last
print(nthToLast(customLL, 3))
