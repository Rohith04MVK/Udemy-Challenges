string = "hello there how are you"
space = ''


def titleizer(string):
    my_list = list(string) 
    for i in my_list:
        if i == ' ':
            index_elem = my_list.index(' ')
            elem = my_list[index_elem+1]

            my_list[index_elem+1] = elem.upper()
            my_list[0] = my_list[0].upper()
    print(space.join(my_list))

titleizer(string)