import readline


# def read_first_n_lines(txtfile, n):
#     with open(txtfile) as f:
#         output = f.readlines()[0:n]
#         return output

def read_first_n_lines(txtfile, n):
    with open(txtfile) as myfile:
        head = [next(myfile) for x in range(n)]
        return head

print(read_first_n_lines('test.txt', 4))