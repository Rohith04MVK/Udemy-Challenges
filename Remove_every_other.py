'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''



my_list = [1,2,3,4,5]

def remove_every_other(list1):
    n = 1
    list2 = []
    for i in list1:
        if n < len(list1):
            list1.pop(n)
            n = n+2
    print(list1)
        
remove_every_other(my_list)