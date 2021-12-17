class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    #Traversing a Linked List
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    
    #Update the new nodes to the first:
    def AtBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    #Update the new nodes to the last:
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode

    #Update the new nodes between two existing nodes:
    def Inbetween(self, middle, newdata):
        if middle is None:
            print("The mentioned node is missing")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle.nextval
        middle.nextval = NewNode

    #Removing an item
    def RemoveItem(self, Removekey):
        Headval = self.headval
        if Headval is not None:
            if Headval.dataval == Removekey:
                self.headval = Headval.nextval
                Headval = None
                return
        while(Headval is not None):
            if Headval.dataval == Removekey:
                break
            prev = Headval
            Headval = Headval.nextval

        if Headval == None:
            return
        
        prev.nextval = Headval.nextval
        Headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list1.AtBeginning("Sun")
list1.AtEnd("Fri")
list1.Inbetween(list1.headval.nextval.nextval.nextval, "Thu")
list1.RemoveItem("Tue")
list1.listprint()