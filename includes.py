def includes(val, val2, val3):
    if val[val3] == val2 or val[1] == val2:
        return True
    else:
        return False

print(includes({'a':1, 'b':2}, 1, 1)) 