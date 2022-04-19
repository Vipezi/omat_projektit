#! /usr/bin/python3

import time

# Arbitary unix time
#print(time.time())
# start time



# To measure the time to generate a list.
#x = [y for y in range(100_00_00_00)]

# end time


# calculation
#print(end_time - start_time)
start_time = time.time()

for x in range(80):
    for y in range(80):
        xy = x+y
        #print(xy, end=" ")
end_time = time.time()
#print("--------------------")
#print(end_time - start_time)

#############################
# We can stop the execution of the program for a time periode using time.sleep
'''
for y in range(10):
    print(y)
    time.sleep(2)'''
#############################

# Type float
print(time.time)

# Type string
print(time.ctime(time.time()))


#Change from time format "Wed Mar 30 09:56:12 2022" to int in second from start of the epoc in unix time.
#time is saved to variable time_human_readable, and save it to variable unix_time.
#Hint! if you don't want to do it in the hard way, you can look something like datetime module.

import datetime
import time

#time_human_readable = time_human_readable.replace("Wed ","").replace("Mar ", "3")
date = datetime.datetime.strptime#(time_human_readable, "%m%d %H:%M:%S %Y")

unix_time = datetime.datetime.timestamp(date)






