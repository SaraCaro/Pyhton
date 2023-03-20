import sys

def frequency (filename):
    num_by_char = []
    with open (filename) as myfile:
        content = myfile.read()
        content_list = "".join(content.split())
        for line in content_list:
            key = line.lower()
            if key in num_by_char:
                num_by_char [key] += 1
            else:
                num_by_char [key] = 1
    print(num_by_char)

frequency("words.txt")