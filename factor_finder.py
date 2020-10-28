def factor_finder(num):
    i = 0
    factor_list = []
    while i < num:
        i = i+1
        if num%i == 0:
            factor_list.append(i)
    print(factor_list)
        
factor_finder(11)