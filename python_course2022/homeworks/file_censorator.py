#! /usr/bin/python3

'''
def file_censorator(filename):
    with open(filename, 'r') as file:
        content=file.readlines()
        del content[0]

file_name = "uncensoredfile.txt"

with open(file_name, 'w') as file:
    content = file.write("Here me calling your name. I trying to reach after you.")

print(file_censorator(file_name))

'''

# Python program to
# demonstrate merging
# of two files
  
data = data2 = ""
  
# Reading data from file1
with open('file1.txt') as fp:
    data = fp.read()
  
# Reading data from file2
with open('file2.txt') as fp:
    data2 = fp.read()
  
# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data2
  
with open ('file3.txt', 'w') as fp:
    fp.write(data)


# Python program to
# demonstrate merging of
# two files
  
# Creating a list of filenames
filenames = ['file1.txt', 'file2.txt']
  
# Open file3 in write mode
with open('file3.txt', 'w') as outfile:
  
    # Iterate through list
    for names in filenames:
  
        # Open each file in read mode
        with open(names) as infile:
  
            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())
  
        # Add '\n' to enter data of file2
        # from next line
        outfile.write("\n")

def file_parser(filename):
    with open(filename, 'r') as f:
        content = f.read()
        #result_file='results.txt'
        #print(content)
        content = content.replace("[","").replace("]","").replace("\n",",")
        content = content.split(",")
        with open('results.txt', 'w') as rf:
            for i in content:
                if i.isdigit() == True:
                    i = int(i)
                    divident = i // 3
                    remainder = i % 3
                    rf.write(f"{i},{divident},{remainder}\n")
    return rf

def file_sensorer(file):
    brother7 = ['JUHANI','TIMO','AAPO','SIMEONI','LAURI','EERO','TUOMAS']
    file_reader = open(file,'r')
    content = file_reader.read()
    for s in brother7:
        stars='*******'
        content = content.replace(s, stars)
        sc = s.capitalize()
        content = content.replace(sc, stars)
    sensored_file =  "data_sensored.txt"
    file_writer = open(sensored_file,'w')
    file_writer.write(content)
    return sensored_file
    