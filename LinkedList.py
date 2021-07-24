## LinkedList overview

## Lasha Suliashvili - 24-07-21

## Beginning

## create a Class about Elements

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

## create a linked list class
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next # we're going with last element.
            current.next = new_element 
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
        
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next ## position element move to position + 1
                    current.next = new_element ## and new_element insert at position n
                counter += 1;
                current = current.next
        elif position == 1:
            new_element.next = self.head
            self.head = new_element;

        return None
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None ## initialize for link previous element to currents next element.
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next;
            else:
                self.head = current.next;

        return None
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

print("excepted output : \n3\n3\n4\n2\n4\n3\n")

print("your output : \n")

# Test get_position
# Should print 3
print (ll.head.next.next.value)
# Should also print 3
print (ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print (ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print (ll.get_position(1).value)
# Should print 4 now
print (ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)
