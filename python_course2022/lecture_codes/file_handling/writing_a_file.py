#! /usr/bin/python3

filename = "Antares.txt"

file_handler = open(filename, 'w')

file_handler.write("A bright red star.\n")
file_handler.close()

file_handler = open(filename, 'a')

file_handler.write("How old is it?")
#print(file_handler.closed) #False, file is open
file_handler.close()

#print(file_handler.closed) #True, file is closed

#if file_handler.closed == True:
    #print("File is closed")

file_reader = open(filename, 'r')

# read one line
line_from_file = file_reader.readline()

# read whole file
whole_file = file_reader.read()

#print(line_from_file)
#print(whole_file)
#for i in file_reader:
#    print(i)

file_reader.close()

open(filename, 'a').write("\nA red giant in Scorpios starsystem!")

with open(filename) as file:
    #print(file.closed)
    content_of_file = file.read()
    #print(file.closed)

#print(file.closed)
#print(content_of_file)

with open(filename) as file2:
    lines_of_file = file.readline()

print(lines_of_file[0])
#for line in file2:
    #if "\n" not in line :
    #   print(line)