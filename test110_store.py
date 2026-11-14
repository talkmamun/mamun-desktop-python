
# Expense Tracker v2.0: Business
# Requirements

import json

#--------------------------------------------------------------
def add_new_expense_input_to_list():
    
     expense_item_new_dict={}
     
     #--Input--
     item_name     = input("item Name : ")
     item_value    = generate_input_valid_positive_int_float_value()    
     item_category = generate_input_valid_category_name()
               
     if item_category == "q" or item_category=="Q":
         return {} 
          
     category_expensed_amount       =  view_category_wise_indivisual_expensed_amount(data_expense_file, item_category)
     category_budget_amount         =  view_indivisual_category_wise_budget_amount(data_category_budget_file, item_category) 
    
     print(f"Expensed amount (previous) ({ item_category}) : {category_expensed_amount}  \n" \
               f"Category_budget ({ item_category}) : ",  category_budget_amount  )
         
     if category_expensed_amount + item_value  <= category_budget_amount :
                     
            expense_item_new_dict.update({"name"    : item_name } )
            expense_item_new_dict.update({"amount"  : item_value } )
            expense_item_new_dict.update({"category": item_category } )
                    
            #print(expense_item_new_dict)
            #print(type(expense_item_new_dict))
            # expense_list.append(expense_item_new_dict)
            
            return  expense_item_new_dict   
     else:
           print(f"You can't add new item, Buget is over the value \n"\
                 f" {category_expensed_amount + item_value}  <= {category_budget_amount}")  
           return {} 
     
#--------------------------------------------------------------
def view_category_wise_indivisual_expensed_amount(data_expense_file, item_category):
     
    result = []

    with open(data_expense_file, "r") as f:

        for line in f:
            data_dic = json.loads(line)
            result.append(data_dic)
            
    category_summary = {}
       
    for res in result:
        if res["category"]==item_category:
           amount = int(res["amount"])
           category_summary[item_category] = category_summary.get(item_category, 0) + amount
           
    total_amount =  sum(category_summary.values())   
    
   # print("category_summary " , category_summary )
   # print("Total_amount : ", total_amount)
    
    return total_amount

#--------------------------------------------------------------
def generate_input_valid_positive_int_float_value():  
      while True:
            try:
              positive_value = float( input(f"Enter positive int/float value : ")       )
              if positive_value < 0:
                 print("value cannot be negative.")
                 continue
              break
          
            except ValueError :
                    print("Invalid input! Please enter a numeric value.")
      
      return  positive_value      
        
        
#--------------------------------------------------------------
def save_expense_data_List_to_file(expense_list):
     
     print("Save data")
     print(expense_list)
         
     result=""
     
     for data_dic in expense_list:
         result += json.dumps(data_dic) + "\n"
          
     # print("\n",result)
         
     with open("data1_expense.txt", "w") as f:
         f.write(result)

     #open and read the file after the appending:

     #with open("data1_expense.txt") as f:
       # print("\n Save one by one item : \n",f.read(),"\n\n")
          
     #--------------------------------------------------------
     print("\n Save Shortcut method : ")       
     with open("data1_expense.json", "w") as f:
        json.dump(expense_list, f, indent=4)
     print("\nData saved successfully! (Shortcut method ) ")
        
     #with open("data1_expense.txt") as f:
      #print(" \n",f.read(),"\n\n")
       

#-----------------------------------------------------------
def apend_new_data_to_file(file_name, data_dict):
   
  #result = print("json.dump(data_dict) : " , json.dumps(data_dict))
  
  result = json.dumps(data_dict) + "\n"
    
  with open(file_name, "a") as f:
         f.write(result)
            
  print("Successfully add expense to the data to file \n")
  
  
#-----------------------------------------------------------
def save_whole_dict_data_to_file(file_name, data_dict):
   
  #result = print("json.dump(data_dict) : " , json.dumps(data_dict))
  
  result = json.dumps(data_dict) + "\n"
    
  with open(file_name, "w") as f:
         f.write(result)
            
  print("Successfully add (dictionary) data to file \n")
  

#----------------------------------------------------------
def load_expense_data_from_file_to_List(file_name):

    print("Load Data from file to List[] ")
    result = []

    with open(file_name, "r") as f:

        for line in f:
            data_dic = json.loads(line)
            result.append(data_dic)
    return result
  
#----------------------------------------------------
  
def check_file_exists_or_not(file_location):
    
   try:
        with open(file_location, "r") as f:
           print("File Exist\n")
           return True

   except FileNotFoundError:
           print("File not Exist\n")
           return False 

#----------------------------------------------------
def view_all_expense(data):   
    print("\nName  :  Amount  :  Category \n -------------------------------- ") 
    i=0 
    for res in data:
       print(f"{res["name"]}   :   {res["amount"]}     :    {res["category"]} ")  
       i=i+1
    print("total items : ", i )    
#----------------------------------------------------
def view_category_wise_expense(data):   
      
    category_summary = {}

    for res in data:
        category = res["category"]
        amount = res["amount"]
        category_summary[category] = category_summary.get(category, 0) + amount
        
        
    print("\ncategory_summary : ", category_summary)
    print("\nCategory   :   Amount     :   no_of_items  \n----------------------------------------------")
    
     
    for category, amount in category_summary.items():
        no_of_items = sum( 1 for res in data if res["category"] == category )
        print(f"{category}   :   {amount}  : ({no_of_items}) " )
    
    
    max_category, max_amount = max(     category_summary.items(),     key=lambda item: item[1]    )
    print("\nMax (Category  &  Amount) : ", max_category, max_amount)
    
    min_category, min_amount = min(     category_summary.items(),     key=lambda item: item[1]    )
    print("Min (Category  &  Amount) : ", min_category, min_amount)
        
    total_category_count =  len(category_summary)   
    total_amount         =  sum(category_summary.values())   
    avg_amt              =  total_amount/total_category_count
    
    print(f"Total_Category_amount_Average  :  {total_category_count} ,  {total_amount} , {avg_amt:.2f} " )
        
    total_noof_items = len(data)
        
        
#----------------------------------------------------
def view_category_wise_count(data):   
   
    print("Category   :   Amount")

    category_summary = {}

    for res in data:
        category = res["category"]
        amount = 1
        category_summary[category] = category_summary.get(category, 0) + amount
        
    print("category_summary : ",category_summary)
    for category, amount in category_summary.items():
        print(f"{category}   :   {amount}")
        
    total_amount =  sum(category_summary.values())   
    print("Total_amount : ", total_amount)
    
    
#----------------------------------------------------
def view_specific_category_expense(data):
     
    category=input("\nEnter category Name : ") 
      
    print("Category   :   Amount")

    category_summary = {}

    for res in data:
        if res["category"]==category:
           category = res["category"]
           amount = res["amount"]
           category_summary[category] = category_summary.get(category, 0) + amount
           print(f"{category}   :   {amount}")
           
    print("category_summary : ",category_summary)
    for category, amount in category_summary.items():
        print(f"{category}   :   {amount}")
        
    total_amount =  sum(category_summary.values())   
    print("Total_amount : ", total_amount)


#----------------------------------------------------
def category_wise_budget_view_save():
    
    print()   
    #food, transport, bills, shopping, health, other. Any
    #other category is saved as "other"
    
    category_budget_dict =  view_all_category_wise_budget_dictionary(data_category_budget_file)
  
    print("----------------------------") 
    
    while True :
        
           i=input("Enter s:Set Budget, v:View Budget,  0,Q: Quit ")
            
           if i=="s" or i=="S" :  

                category_name = generate_input_valid_category_name()  #  input valid category_name
                
                if category_name=="q" or category_name=="Q" :  
                    break
                 
                category_budget = generate_input_valid_positive_int_float_value()
                
                category_budget_dict[category_name] =  category_budget
                
                print(f"category_budget_dict : ", category_budget_dict)
                save_whole_dict_data_to_file(data_category_budget_file, category_budget_dict)  # Save to file 
     
           elif i=="v" or i=="V" :         
                print("Budget Report") 
                view_all_category_wise_budget_dictionary(data_category_budget_file)
                
           elif i =="q" or i =="Q" or i==0:
                break 
           else:
              print("Invalid input")   
               
    # print(category_budget_dict)  

#----------------------------------------------------
def view_indivisual_category_wise_budget_amount(file_name, item_category) :

    result = {}
    category_value = 0
    
    with open(file_name, "r") as f:
        result=json.load(f)
            
    for category, amount in result.items():  # result as a dictionary 
         if category==item_category:
              category_value += int(amount)
    
    return category_value  

#----------------------------------------------------
def view_all_category_wise_budget_dictionary(file_name):
    
    print("\nLoad category Data from file to List[] ")
    
    result = {}
    
    with open(file_name, "r") as f:
        result=json.load(f)
            
    #return result
        
    print("Category  :  Amount  \n ---------------------- ")  
    for category, amount in result.items():  # result as a dictionary 
          print(f"{category}   :   {amount} "  )  
    print()
    return result    
   
#----------------------------------------------------
def generate_input_valid_category_name():
            valid_category_name={"food","transport","bills","shopping","health","other"}
                
            while True: 
                category_name   = input("Enter Category Name "
                                        "\n(f:food, t:transport, b:bills, s:shopping, h:health, o:other) (q:Quit) : ") 
                                             
                if category_name =="f" or category_name =="F":
                    category_name="food"
                elif category_name =="t"  or category_name =="T" :
                    category_name="transport"
                elif category_name =="b" or category_name =="B" :
                    category_name="bills"
                elif category_name =="s" or category_name =="S":
                    category_name="shopping"
                elif category_name =="h" or category_name =="H":
                    category_name="health"
                elif category_name =="o" or category_name =="O":
                    category_name="other"
            
                if category_name in valid_category_name:
                    return  category_name   # return valid valid category name
                elif category_name =="q" or category_name =="Q":     
                    return "q"    
                else:
                    print("Enter valid category name") 
                
            return  category_name  
  
  
  
def delete_item_from_expense_list(expense_item, expense_list ):
   
    if expense_item=="" :
        expense_item = input("\nEnter expense item for delete : ") 
        
        for item in expense_list:
          print("item : " , item)
          if item["name"] == expense_item:
              expense_list.remove(item)
              break
          print("item : " , item)
    
    return expense_list

#=====================================================================================
#=====================================================================================

expense_list =[]
expense_category_dict={}

budget_category_dict={}

data_expense_file          = "data1_expense.txt"
data_category_budget_file  = "data1_category.txt"

#-------------------------------------------------------
if check_file_exists_or_not(data_expense_file):
   expense_list = load_expense_data_from_file_to_List(data_expense_file)
   print("\nLoad Existing data File to list : ", expense_list)
else: 
   with open(data_expense_file, "w") as f:
        print("Create New File ")

#-------------------------------------------------------
if check_file_exists_or_not(data_category_budget_file):
   #expense_list=load_data_from_file_to_category_dict()
   #print("\nExisting File Data : ", expense_list)
   print()
else: 
   with open(data_category_budget_file, "w") as f:
        print("Create New File ")
#-------------------------------------------------------
  
  
  
while True: 
  
  print("\nMain Menu ")
  print("    1: add expense,  2: edit expense 3: delete expense  \n" \
        "    4: view all expense,  5: View category wise expense 6: View category wise count 7: view specific category \n" \
        "    8: delete expense(item)  9: Category wise Budget  0/Q: Quit \n\n ")
  
  #--- valid input ---
  while True:
    a = input("Enter valid No (0123456789 0/Q) :  ")
    ai=int(100)
    
    if a in "0123456789" and len(a) == 1:
        ai=int(a)
        break
    elif a in "qQ" and len(a) == 1:
        break
    else:
        print("Invalid input (0123456789 qQ) ")    
             
             
 #-------------------------------------------------------------------      
  if a=="1" or ai== 1 :
    new_expense_dict = add_new_expense_input_to_list()  # return Dictionary
    
    if new_expense_dict is not None  and len(json.dumps(new_expense_dict))>8 :   
       expense_list.append (new_expense_dict)
       apend_new_data_to_file(data_expense_file, new_expense_dict)     
          
  elif a=="3" or ai==3 :   
    
    print("Before delete :", len(expense_list))   
    expense_list=delete_item_from_expense_list("", expense_list )   
    
    save_expense_data_List_to_file(expense_list)  
    print("After delete :", len(expense_list))      
          
  elif a=="4" or ai==4 :   
    view_all_expense(expense_list)
    
  elif a=="5" or   ai==5:   
     view_category_wise_expense(expense_list)
  
  elif  a=="6" or   ai==6: 
    view_category_wise_count(expense_list)
  
  elif  a=="7" or   ai==7:   
      view_specific_category_expense(expense_list)
          
  elif  a=="8" or   ai==8: 
      print("Load Data ")
        
  elif  a=="9" or   ai==9: 
     print("Budget")
     category_wise_budget_view_save() 
               
  elif a=="0" or a=="q" or a=="Q" or ai==0 :
    print("Exit Program")
    break
      
          
  