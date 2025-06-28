"""
Problem statement : 

Aman, who is working at a software company forgot the password of his Linkedin id.But he knows the ASCII values of his password in reverse order. Help aman to find the password.
To decode the password, first reverse the string of digits, then successively pick valid values from the string and convert them to their ASCII equivalents. Some of the values will have two digits, and others three. Use the ranges of valid values when decoding the string of digits.

Some of the ASCII values are given with their characters:

    The ASCII value of A to Z is 65 to 90.
    The ASCII value of a to z is 97 to 122.
    The ASCII value of space characters is 32.

    Note: The password only has alphabets and blank spaces.

Given a string , decode the password by following the steps mentioned above.

Constraints:

1<= |s| <=10^5
s[i] is an ascii character in the range [A-Za-z] or a space character

Sample Input:

796115110113721110141108

Sample Output:

PrepInsta

Explanation :

The reversed string will be 801141011127311011511697, which if analysed as ascii will be “PrepInsta”
"""

# Solution: 

num = input()
num = num[::-1]
res = ""
i =0
while(i<len(num)-1):
    check = num[i] + num[i+1]
    if check == "32":
        res = " "
    elif int(check) in range(65,91) or int(check) in range(97,100):
        res += chr(int(check))
    elif i+2 < len(num):
        check += num[i+2]
        res += chr(int(check))
        i +=1
    i+=2
print(res)
