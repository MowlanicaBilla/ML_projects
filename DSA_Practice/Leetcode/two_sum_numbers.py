a = [2,4,3]
b = [5,6,4]
def list_to_num(l):
    strings = [str(integer) for integer in l]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer
# res1 = sum(d * 10**i for i, d in enumerate(a[::-1]))
# res2 = sum(d * 10**i for i, d in enumerate(b[::-1]))
res1 = list_to_num(a)
res2 = list_to_num(b)
output = res1 + res2
res = [int(x) for x in str(output)]
final_output = res[::1]
print(final_output)