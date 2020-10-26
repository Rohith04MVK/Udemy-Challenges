def vowel_counter(string):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    vowel_dict = {}
    list_of_string = list(string)
    for vowel in list_of_string:
        print(vowel)
        if vowel == "a":
            a = a+1
            vowel_dict['a'] = a
        elif vowel == "e":
            e = e+1
            vowel_dict['e'] = e
        elif vowel == "i":
            i = i+1
            vowel_dict['i'] = i
        elif vowel == "o":
            o = o+1
            vowel_dict['o'] = o
        elif vowel == "u":
            u = u+1
            vowel_dict['u'] = u
    print(vowel_dict)


vowel_counter("Hello there how are you")