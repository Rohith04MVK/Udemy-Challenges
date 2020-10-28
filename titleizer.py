string = "hello there how are you"
space = ''


def titleizer(string):
    my_list = list(string) 
    num = 0
    my_list[0] = my_list[0].upper()
    for i in my_list:
        num = num+1
        if i ==' ':
            my_list[num] = my_list[num].upper()
    print(space.join(my_list))

titleizer(string)