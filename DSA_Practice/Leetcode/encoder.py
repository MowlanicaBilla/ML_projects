"""

Write a function that replaces the words in `raw` with the words in `code_words` 
such that the first occurrence of each word in `raw` is assigned the first unassigned 
word in `code_words`.


encoder(["a"], ["1", "2", "3", "4"]) → ["1"]
encoder(["a", "b"], ["1", "2", "3", "4"]) → ["1", "2"]
encoder(["a", "b", "a"], ["1", "2", "3", "4"]) → ["1", "2", "1"]
"""

def encoder(input_list):
    len_str = max(len(input_list[0]), len(input_list[1]))
    ind_dict = {}
    for i in range(len_str):
        ind_dict[i] = input_list[i]
    print(ind_dict)
    
print(encoder(["a"], ["1", "2", "3", "4"]))