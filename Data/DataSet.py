"""
Created on Sat Aug  4 22:32:36 2018

@author: madon
"""

nestedList = [["NewYork",25,120],
              ["Boston",18,30],
              ["Manhattan",22,50],
              ["Birmingham",43,60],
              ["California",50,100],
             ]

print("Location : Age : Monthly Payments ")

for item in nestedList:
    print(item[0],":" * (9-len(item[0])),":",
          item[1]," " *(13-len(str(item[1]))),item[2],"" *(4-len(str(item[2]))),":")