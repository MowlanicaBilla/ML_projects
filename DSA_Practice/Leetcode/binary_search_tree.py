class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exists

        if data < self.data:
						# add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
						# add data in right subtree
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.in_order_traversal()
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete_using_min(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_using_min(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_using_min(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_using_min(min_val)
        
        return self
    
    def delete_using_max(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_using_max(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_using_max(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_using_max(max_val)
        
        return self


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    # countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    # country_tree = build_tree(countries)

    # print("UK is in the list? ", country_tree.search("UK"))
    # print("Sweden is in the list? ", country_tree.search("Sweden"))

    # numbers_tree = build_tree([88, 20, 12, 23, 14, 7, 27, 15])
    # print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    # print("Pre order traversal gives this sorted list:",numbers_tree.pre_order_traversal())
    # print("Post order traversal gives this sorted list:",numbers_tree.post_order_traversal())
    
    # numbers = [17, 4, 1, 20, 9, 23, 18, 34]

    # numbers = [15,12,7,14,27,20,23,88 ]

    # numbers_tree = build_tree(numbers)
    # print("Input numbers:",numbers)
    # print("Min:",numbers_tree.find_min())
    # print("Max:",numbers_tree.find_max())
    # print("Sum:", numbers_tree.calculate_sum())
    # print("In order traversal:", numbers_tree.in_order_traversal())
    # print("Pre order traversal:", numbers_tree.pre_order_traversal())
    # print("Post order traversal:", numbers_tree.post_order_traversal())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete_using_min(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete_using_min(9)
    print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete_using_max(17)
    print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]
