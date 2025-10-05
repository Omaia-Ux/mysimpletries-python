
print (1846+43+253+52)
num1= 10
num2= 20
num3= 30
num4= 40
Sum = num1+num2+num3/num4
print (Sum)
10%10 == 0
print(10/10)
print(10//10)
#number % same number
print (100%100)
#small number % big number = small number
print(100%101)
# big number % small number = big number
print(10%5)
           #10-5=5 or 5-5=0
           # we cant have minus results = so we cant minus (big numb) \from\ (small numb)
print (18000000000000000000/8000000000)
#if

import pandas as pd
# nutritional values per 100g (boiled, cooked without salt)
data={
    "food":["potato","white rice (cooked)","pasta (cooked)"],
      "calories(kcal)": [86, 130, 131],
      "protien (g)": [1.7, 2.4, 5.0],
      "carbs (g)": [20, 28, 25],
      "fiber (g)": [1.8, 0.4, 1.3],
      "fat (g)": [0.1, 0.3, 1.1],
      }
df=pd.DataFrame(data)
import caas_jupyter_tools
caas_jupyter_tools.display_dataframe_to_user("comparison of potato, rice, and pasta (per 100g, cooked)", df)
