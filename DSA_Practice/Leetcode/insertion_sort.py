def insertion_sort(elements):
    for i in range(1,len(elements)):
        anchor = elements[i]
        j = i - 1 # Inorder to make sure the left of the anchor elements are less than that element, we are initiating a pointer a position less than that element
        while j >=0 and anchor < elements[j]:
            # swapping the elements if the anchor is greater than the pointer element
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor

if __name__ == "__main__":
    elements = [50, 29,56, 44, 1, 4, 78]
    insertion_sort(elements)
    print(elements)
