class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

        
    def print_tree(self, level):
        if level < self.get_level():
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    
def build_product_tree(): 
    # Each child is an instance of tree Node
    ind_state1 = TreeNode("Gujarat")
    ind_state1.add_child(TreeNode("Ahmedabad"))
    ind_state1.add_child(TreeNode("Baroda"))

    ind_state2 = TreeNode("Karnataka")
    ind_state2.add_child(TreeNode("Mysore"))
    ind_state2.add_child(TreeNode("Bangalore"))

    india = TreeNode("India")
    india.add_child(ind_state1)
    india.add_child(ind_state2)

    us_state1 = TreeNode("New Jersey")
    us_state1.add_child(TreeNode("Priceton"))
    us_state1.add_child(TreeNode("Trenton"))

    us_state2 = TreeNode("California")
    us_state2.add_child(TreeNode("San Francisco"))
    us_state2.add_child(TreeNode("Mountain View"))
    us_state2.add_child(TreeNode("Palo Alto"))

    us = TreeNode("United States of America")
    us.add_child(us_state1)
    us.add_child(us_state2)



    location = TreeNode("Global")
    location.add_child(india)
    location.add_child(us)
    
    return location

if __name__ == "__main__":
    location = build_product_tree()
    # print(root.get_level())
    location.print_tree(1)
    pass