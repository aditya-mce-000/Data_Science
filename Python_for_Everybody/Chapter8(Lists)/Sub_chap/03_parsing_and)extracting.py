fhand = open("C:\\Users\\adity\\OneDrive\\Documents(1)\\Programming\\Data_Science\\Python_for_Everybody\\mail_box.txt")
for line in fhand:
    if '@' in line:
        data = line
        found = data.find('@')
        to_print = data.find(' ', found)
        print(data[found+1:to_print])