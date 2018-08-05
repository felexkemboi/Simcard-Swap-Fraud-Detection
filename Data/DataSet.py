"""
Created on Sat Aug  4 22:32:36 2018

@author: madon
"""

nestedList = [["California",25,120],
              ["California",18,30],
              ["California",22,50],
              ["Birmingham",43,60],
              ["California",50,100],
             ]

print("Location : Age : Monthly Payments ")

for item in nestedList:
    print(item[0]," : " * (10-len(item[0])),":",
          item[1]," " *(14-len(str(item[1]))),item[2]," " *(4-len(str(item[2]))),)