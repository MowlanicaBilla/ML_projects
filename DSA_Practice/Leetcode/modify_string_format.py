# Modify String format:
# Input : I_Am_A_Coder
# Output : i.aM.a.cODER

# Input : This_Is_A_Good_Morning
# Output : tHIS.iS.a.gOOD.mORNING

# chnages
# _ = .
# first_upper_letter = first_lower_letter
# remaining_lower_letter = remaining_upper_letter

# Using list
def string_format(s):
    l = []
    temp = s.split('_')
    for i in temp:
        l.append(i[0].lower() + i[1:].upper())
    s = '.'.join(l)
    return s

print(string_format('This_Is_A_Good_Morning'))


# Using String
def string_format_using_str(s):
    new_s = ''
    temp = s.split('_')
    for i in temp:
        new_s = new_s + i[0].lower() + i[1:].upper() + '.'
    new_s = new_s[:-1] #removes the period at the end
    return new_s



print(string_format_using_str('This_Is_A_Good_Morning'))