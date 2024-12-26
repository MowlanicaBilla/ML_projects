digits = [1,2,3]
s = [str(integer) for integer in digits]
a_string = "".join(s)
res = int(a_string)
res += 1
final_lst = list(map(int, str(res)))
print(final_lst)