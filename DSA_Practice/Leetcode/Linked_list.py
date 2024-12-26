class Node:
    def __init__(self, data=None, next = None) -> None:
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def insert_at_the_beginning(self, data):
        node = Node(data, self.head) # Since the head of the next element is the address of the first node
        self.head = node

    def insert_at_the_end(self, data):
        # If the Linked list is Null
        if self.head is None:
            self.head = Node(data, None)
            return
        
        # If the Linked list is not null, iterate through the Linked List and insert at the end
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert_in_the_middle(self, data):
        # If the Linked list is null
        if self.head is None:
            self.head = Node(data, None)
            return
        
        # If the linked list is not null
        itr = self.head
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_the_end(data)

    def get_length(self): # Get length of a Linked list
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count

    def remove_at_index(self, index): # Removing element at a particular index
        if index < 0 or index>=self.get_length(): # >= because index starts at 0 index
            raise Exception("Invalid Index")
        elif index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insert_at_index(self, index, data):
        if index < 0 or index>self.get_length(): # >= because index starts at 0 index
            raise Exception("Invalid Index")
        
        elif index == 0:
            self.insert_at_the_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1
        

    
    def print_ll(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
    
    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
        


    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
        
    

if __name__ == "__main__":
    # ll = LinkedList()
    # # ll.insert_at_the_beginning(5)
    # # ll.insert_at_the_beginning(18)
    # # ll.insert_at_the_end(20)
    # ll.insert_values(["Mini","Veer","Rama","Srini","Junk food"])
    # ll.print_ll()
    # print(ll.get_length())
    # ll.remove_at_index(4)
    # ll.print_ll()
    # ll.insert_at_index(4, "Panipuri")
    # ll.print_ll()
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_ll()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print_ll()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print_ll()
    ll.remove_by_value("figs")
    ll.print_ll()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print_ll()