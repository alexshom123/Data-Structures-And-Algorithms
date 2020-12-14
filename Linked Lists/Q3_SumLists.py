
# Question 4 - Sum Lists: given two lists, create a new list which is the addition of the two lists (e.g 2->2->2 & 5->5->5 = 7->7->7)

from LinkedListQuestionsBase import LinkedList

def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    # Sum two node value pairs
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        #add values mod 10 to get single digit, divide carry by 10
        ll.add(int(result % 10))
        carry = result / 10
    
    return ll

# Trial
llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)


llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)
print(llA)
print(llB)
print(sumList(llA, llB))
