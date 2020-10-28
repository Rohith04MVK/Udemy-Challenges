def factor_finder(num):
    i = 0
    factor_list = []
    while i < num:
        i = i+1
        if num%i == 0:
            factor_list.append(i)
    return(factor_list)
        
if len(factor_finder(11)) == 2:
    print("Prime Number")
else:
    print("Composite number")