"""
Modify bubble_sort function such that it can sort following list of transactions happening in an electronic store,
elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

bubble_sort function should take key from a transaction record and sort the list as per that key. For example,

bubble_sort(elements, key='transaction_amount')

This will sort elements by transaction_amount and your sorted list will look like,

elements = [
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]
But if you call it like this,
bubble_sort(elements, key='name')

output will be,

elements = [
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]
"""

# def bubble_sort(elements):
# 	size = len(elements)
# 	for i in range(size - 1):
# 		swapped = False
# 		for j in range(size - 1 - i): # In iteration 1, the highest element is pushed to the end, in iteration 2, second highest element is pushed to last but 1 position, so we dont have to iteration till the end, because the as the iterations increase, the last numbers are already sorted, this saves some time.
# 			if elements[j] > elements[j+1]:
# 				# Swapping the elements, if the left element is greater than the right
# 				tmp = elements[j]
# 				elements[j] = elements[j+1]
# 				elements[j+1] = tmp
# 				swapped = True
# 		if not swapped:
# 			break

# if __name__ == "__main__":
# 	elements = [5,9,2,1,67,34,88,34]
# 	bubble_sort(elements)

def bubble_sort(elements, key):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i): # In iteration 1, the highest element is pushed to the end, in iteration 2, second highest element is pushed to last but 1 position, so we dont have to iteration till the end, because the as the iterations increase, the last numbers are already sorted, this saves some time.
            if elements[j][key] > elements[j+1][key]:
                # Swapping the elements, if the left element is greater than the right
                tmp = elements[j][key]
                elements[j][key] = elements[j+1][key]
                elements[j+1][key] = tmp
                swapped = True
        if not swapped:
            break
    return elements

if __name__ == "__main__":
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    bubble_sort(elements, key='transaction_amount')
    print(elements)
