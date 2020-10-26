# Accepts a list and checks if the content og the list is lists
# eg: [[1],[2]] - True
# eg: [[2], 4]] - Flase

my_list = [[1], [2]]


def list_check(list1):
    l = all(isinstance(ellement, list) for ellement in list1)
    print(l)


list_check(my_list)