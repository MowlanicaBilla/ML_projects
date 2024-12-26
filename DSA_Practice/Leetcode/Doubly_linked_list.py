class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_Linked_list:
    def __init__(self) -> None:
        self.head = None

    def insert_at_the_beginning(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
    
    def insert_at_the_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
    

    # def print_backward(self):
    # # Print linked list in reverse direction. Use node.prev for this.

if __name__ == "__main__":
    dll = Doubly_Linked_list()
    dll.insert_at_the_beginning(["banana"])
    dll.print_forward()
    dll.insert_at_the_end(["fig"])
    dll.print_forward()