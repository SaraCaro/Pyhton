def is_anagram(left, right):
    left = left.lower()
    right = right.lower()
    print(len(left), len(right))
    count = 0
    if (len(left) != len(right)):
        return (False)
    else:
        for i in range(0, len(left)):
            for j in range(0, len(right)):
                if(left[i] == right[j]):
                    count += 1
        if (count == len(left)):
            return (True)
        else:
            return (False)
left = input("Enter a string 1: ")
right = input("Enter a string 2: ")
result = is_anagram (left, right)
print (result)