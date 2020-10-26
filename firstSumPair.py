# Given a list of intigers and a number the function will find the first pair with the number as the sum from the list


my_list = [1, 2, 3, 6, 7, 8, 9, 10]


def firstSumPair(list1, sum):
    num1 = 0
    num2 = 1
    while num2 < len(list1):
        if list1[num1]+list1[num2] == sum:
            print([list1[num1], list1[num2]])
            break
        else:
            num1 = num1+1
            num2 = num2+1


firstSumPair(my_list, 3)
