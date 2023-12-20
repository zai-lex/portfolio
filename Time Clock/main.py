from time_formatter import add_time

# This program is a time clock 
# You can input the starting time and how much time needs to be added
# Additionally you can input a starting day of the week
# The program will tell you if any days go by and if so how many
# Below are test cases 

print(add_time("11:59 PM", "24:05", "Wednesday"))
# Returns: 12:04 AM, Friday (2 days later) 

print(add_time("5:01 AM", "0:00"))
# Returns: 5:01 AM 

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM 

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day) 

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later) 

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later) 