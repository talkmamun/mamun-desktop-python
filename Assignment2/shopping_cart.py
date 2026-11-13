# Name : AL MAMUN, Batch-14, 01614071297, talkmamun@gmail.com 
# Assignment 2

# Shopping Cart ...



def checking_numeric_value_input(data):
    
  while True:
    try:
        price = int(input(f" {data}  "))
        if price<0:
           print("Enter Positive value")
        else:   
           return price
    except ValueError:
        print("Invalid Input! Please enter a numeric value.")
 
    
#=============== Main ==================================================================

name = input("\n\nEnter your name: ")  

product1_name = input("Enter product name 1: ")
product1_price = checking_numeric_value_input("Enter product price 1: ")

#----------------------------------

product2_name = input("Enter product name 2: ")
product2_price = checking_numeric_value_input("Enter product price 2: ")

#----------------------------------

product3_name = input("Enter product name 3: ")
product3_price = checking_numeric_value_input("Enter product price 3: ")

total_price = product1_price + product2_price + product3_price

# Determines the discount using: o 5000 or above → 20% discount o 3000–4999 → 10% discount
# o 1000–2999 → 5% discount o Below 1000 → No discount

if total_price >= 5000:
    discount = total_price * 0.20   
elif total_price >= 3000:
    discount = total_price * 0.10   
elif total_price >= 1000:
    discount = total_price * 0.05       
else:
    discount = 0    

# Subtotal: 4300 Discount: 430 Final Total: 3870

subtotal = total_price
final_total = subtotal - discount

print(f"\nCustomer Name:: {name}")

print(f"\nProduct 1:: {product1_name}")
print(f"Price 1:: {product1_price}")

print(f"\nProduct 2:: {product2_name}")
print(f"Price 2:: {product2_price}")

print(f"\nProduct 3:: {product3_name}")
print(f"Price 3:: {product3_price}")

print(f"\nSubtotal: {subtotal:.2f}")      
print(f"Discount: {discount:.2f}")
print(f"Final Total: {final_total:.2f}\n")