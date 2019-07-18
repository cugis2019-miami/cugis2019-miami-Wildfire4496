#day 3 of Coding
"""
Created on Wed Jul 17 10:03:48 2019

@author: admin
"""

    m=5
    d=3
    w=8
    print("There are" ,m, "milk,", d, "dark and,", w, "white chocolates")

#dict data structure
    chocolate1= {"milk":5}
    chocolate2= {"dark":3}
    chocolate3= {"white":8}
    
    #DICT
    chocolatebox={"milk":5,"dark":3, "white":8}
print(chocolatebox)
print("the number of chocolates in the box are", chocolatebox)   

#Dict structure practice
caprisunbox={"fruit punch":5,"tropical punch":7, "blue raspberry":9}
print(caprisunbox)

#Spread sheet code practice
chocolatebox={"milk":5, "dark":3, "white":8}
print("the number of chocolates in the chocolate box is", chocolatebox["milk"])
 chocolatebox={"milk":5, "dark":3, "white":8}
 print("The number of white chocolate in the chocolate box is",chocolatebox["white"])
 
age={"Steve":32,"Lia": 28, "Vin":45,"Katie":38}
gender={"Steve": male, "Lia": female, "Vin":45, "Katie":38}
print("Lia is",age["Lia"],"years old and she is",gender["Lia"])

      
      #New DataFrame
import pandas
dir(pandas)
 chocolatebox={"milk":5, "dark": 3, "white":8}
 chocolateinfo= pandas.Series(chocolatebox)
 print(chocolateinfo)
 print(chocolate)
