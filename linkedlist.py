# This program is to implement a linkedlist in python

class Node:
    """ This is to represent and element in the linkedlist  it holds data and pointer to the next element"""
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    """This is to hold all the elements of the linked list"""
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def prepend(self, data):
        current = Node(data)
        current.next = self.head
        self.head = current
        self.length = self.length + 1
    
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        # print(end="\n")
        # print(data, end=" Not Found !!")
        return None
    
    def display(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
            
    def delete(self,data):
        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
                
            
        if current == None:
            print(data,end=" Not found !!\n")
            
        elif prev == None and current.data == data: # or you could still say if self.head.data == data
            self.head = current.next        
            self.length = self.length - 1
            print(data, end=" Deleted !!\n")
            
        elif current.data == data:
            prev.next = current.next
            self.length = self.length - 1
            print(end="\n")
            print(data, end=" Deleted !!\n")
               
        # elif current == None:
        #     print(data,end=" Not found")
    
    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        self.length = self.length + 1
    
    def insert(self, data, pos):
        new_node = Node(data)
        current = self.head
        count = 0
        prev = None

        while current:
            
            prev = current
            current = current.next
            count = count + 1
            if pos < 0 :
                print("Postion cannot be negative")
                break
            elif pos == 0:
                self.prepend(data)
                break
            elif count == pos:
                prev.next = new_node
                new_node.next = current
                self.length += 1
                break 
        
        if pos > count:
            self.append(data)
            
            
            
        
            
    
    
list1 = LinkedList()
list1.prepend(2)
list1.prepend(9)
list1.append(5)
list1.append(2)
list1.insert(0,1)
list1.display()
print(end="\n")
list1.display()
print(end="\n")
print(list1.search(5))
print("\nThe length of the list is ",list1.length)


