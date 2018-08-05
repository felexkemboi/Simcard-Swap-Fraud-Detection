"""
Created on Sat Aug  4 22:32:36 2018

@author: madon
"""

nestedList = [["EastLeigh",25,120],
              ["Buru Buru",18,30],
              ["Lavington",22,50],
              ["Kileleshwa",43,60],
              ["Kitusuru",50,100],
             ]

print("Location : Age : Monthly Payments ")

for item in nestedList:
    print(item[0]," : " * (7-len(item[0])),":",
          item[1]," " *(9-len(str(item[1]))),item[2]," " *(4-len(str(item[2]))),)