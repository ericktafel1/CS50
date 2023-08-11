## The .split() method converts a string into a list. It separates the string based on a specified character that's passed into .split() as an argument. 

approved_users = "elarson,bmoreno,tshah,sgilmore,eraab"
print("before .split():", approved_users)
approved_users = approved_users.split(",")
print("after .split():", approved_users)