def numcount (string):
    mytext = "".join(string.split())
    num_by_char = {}
    for letter in string:
        key = letter.lower()
        if key in num_by_char:
            num_by_char[key] +=1
        else:
             num_by_char[key] = 1
    return num_by_char

