# hello 

import json 

item_category="bills"
    
category_value=0
    
with open("data1_category.txt", "r") as f:
        result=json.load(f)

print(result,"\n")            
            
for category, amount in result.items():  # result as a dictionary 
         if category==item_category:
              category_value = category_value + int(amount)
              print(amount)
print(category_value)
