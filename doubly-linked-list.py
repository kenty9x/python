class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

class Dlinked:
    def __init__(self):
        self.head = None
    
    #Add to the first item:
    def push(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    #Add item after one existing item
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("This node does not exist")
            return
        
        new_node = Node(data=new_data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    #Add item to the last one:
    def append(self, new_data):
        new_node = Node(data=new_data)
        last = self.head
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

list1=Dlinked()
e1=Node("Node1")
list1.head = e1



