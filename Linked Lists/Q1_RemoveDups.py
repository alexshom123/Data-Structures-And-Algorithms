
# Question 1 - Remove Dups : Write a code to remove duplicates from an unsorted linked list. 
# NOTE: I generate a random LL, so may need to re run code if the generated LL does not contain dupes

from LinkedListQuestionsBase import LinkedList

def removeDups(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])
        # Append to set if already visited and destroy the node
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll


# Trial
customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
removeDups(customLL)
print(customLL)
