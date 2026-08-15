fhand = open('hello.txt')
for line in fhand:
    if '@' in line:
        data = line
        found = data.find('@')
        to_print = data.find(' ', found)
        print(line[found+1:to_print]) 
    # continue