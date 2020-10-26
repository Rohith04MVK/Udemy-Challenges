string = "<Put a string here>"
ans_list = []
list_string = list(string)
space = ""


def reverse_string(string):
    n = 0
    for i in list_string:
        n = n-1
        ans_list.append(list_string[n])
    return space.join(ans_list)


print(reverse_string(string))


# Or

def reverse_string_2(string):
    return(string[::-1])


print(reverse_string_2(string))
