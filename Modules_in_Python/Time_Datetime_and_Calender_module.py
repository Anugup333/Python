import time,datetime,calendar

print("---- total numbers of ticks spend since 12 Am 1st Jan 1970 -----")
print(f"{time.time()}\n")

print("---------- Current Time Tuple ----------")
print(f"{time.localtime(time.time())}\n")

print("------- Formatted Time for the Time tuple being passed ---------")
print(f"{time.asctime(time.localtime(time.time()))}\n")

print("--------- Current Time ---------")
x = datetime.datetime.now()
print(f"{x}\n")

print("------- Print the Year ----------")
y = x.strftime("%Y")
print(f"{y}\n")

print("--------- Print the month ---------")
z = x.strftime("%m")
print(f"{z}\n")

print("------- print the data and time ---------")
print(f"{datetime.datetime(2003,8,1,1,26,40)}\n")

print("--------- print the Calender for the month ---------")
print(f"{calendar.month(2003,8)}\n")

print("--------- Print the Calender of the whole year ---------")
print(f"{calendar.prcal(2024)}")

