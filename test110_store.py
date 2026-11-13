
# Expense Tracker v2.0: Business
# Requirements

import json

#--------------------------------------------------------------
def add_new_expense_input():
    
     expense_item_new_dict={}
     
     item_name     = input("item Name : ")
     item_value    = int(input("item value : "))
     item_category = input("item category : ")
           
     expense_item_new_dict.update({"name"    : item_name } )
     expense_item_new_dict.update({"amount"  : item_value } )
     expense_item_new_dict.update({"category": item_category } )
     
     #print(expense_item_new_dict)
     #print(type(expense_item_new_dict))
     
     # expense_list.append(expense_item_new_dict)
     
     return  expense_item_new_dict   
          
#--------------------------------------------------------------
def save_data_List_to_file(expense_list):
     
     print("Save data")
     print(expense_list)
         
     result=""
     
     for data_dic in expense_list:
         result += json.dumps(data_dic) + "\n"
          
     print("\n",result)
         
     with open("data1_expense.txt", "w") as f:
        f.write(result)

     #open and read the file after the appending:

     with open("data1_expense.txt") as f:
        print("\n Save one by one item : \n",f.read(),"\n\n")
          
     #--------------------------------------------------------
     print("\n Save Shortcut method : ")       
     with open("data1_expense.json", "w") as f:
        json.dump(expense_list, f, indent=4)
     print("\nData saved successfully! (Shortcut method ) ")
        
     with open("data1_expense.txt") as f:
       print(" \n",f.read(),"\n\n")
       

#-----------------------------------------------------------
def apend_new_data_to_file(file_name, data_dict):
   
  #result = print("json.dump(data_dict) : " , json.dumps(data_dict))
  
  result = json.dumps(data_dict) + "\n"
    
  with open(file_name, "a") as f:
         f.write(result)
            
  print("Successfully add the new data to file ")
  
  
#-----------------------------------------------------------
def save_whole_dict_data_to_file(file_name, data_dict):
   
  #result = print("json.dump(data_dict) : " , json.dumps(data_dict))
  
  result = json.dumps(data_dict) + "\n"
    
  with open(file_name, "w") as f:
         f.write(result)
            
  print("Successfully add the new data to file ")
  

#----------------------------------------------------------
def load_data_from_file_to_List(file_name):

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
           print("File Exist")
           return True

   except FileNotFoundError:
           print("File not Exist")
           return False 

#----------------------------------------------------
def view_all_expense(data):   
    print("Name  :  Amount  :  Category ")  
    for res in data:
       print(f"{res["name"]}   :   {res["amount"]}     :    {res["category"]} ")  

#----------------------------------------------------
def view_category_wise_expense(data):   
      

    category_summary = {}

    for res in data:
        category = res["category"]
        amount = res["amount"]
        category_summary[category] = category_summary.get(category, 0) + amount
        
    print("category_summary : ",category_summary)
    print("Category   :   Amount     :   no_of_items  ")
     
    for category, amount in category_summary.items():
        no_of_items= no_of_items = sum( 1 for res in data if res["category"] == category )
        print(f"{category}   :   {amount}  : ({no_of_items}) " )
    
    max_category, max_amount = max(     category_summary.items(),     key=lambda item: item[1]    )
    print("\nMax (Category  &  Amount) : ", max_category, max_amount)
    
    min_category, min_amount = min(     category_summary.items(),     key=lambda item: item[1]    )
    print("Min (Category  &  Amount) : ", min_category, min_amount)
        
    total_category_count =  len(category_summary)   
    total_amount         =  sum(category_summary.values())   
    avg_amt              =  total_amount/total_category_count
    
    print(f"Total_Category_amount_Average  :  {total_category_count} ,  {total_amount} , {avg_amt} " )
        
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
def view_specific_category(data):
     
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
def set_category_wise_budget():
    print()   
    #food, transport, bills, shopping, health, other. Any
    #other category is saved as "other"
    
    i=input("Enter s:Set Budget , v:View Budget,  ")
     
    if i=="s":  
            category_budget_dict = {}    
            while True :
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
                elif category_name =="q" or category_name =="Q":
                    break 
                category_budget = input("Enter Category Budget : ") 
                category_budget_dict[category_name] =  category_budget
                #print("category_budget_dict (each) : ", category_budget_dict)
                # End while 
            
            print("category_budget_dict : ", category_budget_dict)
            save_whole_dict_data_to_file(data_category_file, category_budget_dict)
     
    elif i=="v":         
        print("Budget Report") 
        view_category_wise_budget(data_category_file)
    else:
        print("Invalid input")   
     
               
    # print(category_budget_dict)  

 #----------------------------------------------------
def view_category_wise_budget(file_name):
    
    print("Load category Data from file to List[] ")
    result = {}
    
    with open(file_name, "r") as f:
        result=json.load(f)
            
    #return result
    
    
    print("Category  :  Amount  ")  
    for category, amount in result.items():
          print(f"{category}   :   {amount} "  )  
   
        
        
#=====================================================================================
#=====================================================================================

expense_list =[]
expense_category_dict={}

budget_category_dict={}

data_expense_file  = "data1_expense.txt"
data_category_file = "data1_category.txt"

#----------------------------------------------------
if check_file_exists_or_not(data_expense_file):
   expense_list=load_data_from_file_to_List(data_expense_file)
   print("\nLoad Existing File Data : ", expense_list)
else: 
   with open(data_expense_file, "w") as f:
        print("Create New File ")

#----------------------------------------------------
if check_file_exists_or_not(data_category_file):
   #expense_list=load_data_from_file_to_category_dict()
   #print("\nExisting File Data : ", expense_list)
   print()
else: 
   with open(data_category_file, "w") as f:
        print("Create New File ")
#----------------------------------------------------
  
  
  
while True: 
  
  print("\nMain Menu ")
  print("    1: add expense,  2: edit expense 3: delete expense  \n" \
        "    4: view all expense,  5: View category wise expense 6: View category wise count 7: view specific category \n " \
        "    8: delete expense(item)  9: Category wise Budget  0: Quit \n\n ")
  
  a=int(input("Enter No : "))
    
  if a==1:
    # print("\nExpense List (before insert) : " , expense_list) 
    # expense_list.append = add_new_expense()
    
    new_expense_dict = add_new_expense_input()
    
    #print("new_expense_dict :" , new_expense_dict)
    expense_list.append (new_expense_dict)
    
    #print("successfully added the data to main list : " , new_expense_dict )     
    #print("\nExpense List (all, After insert ): " , expense_list) 
    
    apend_new_data_to_file(data_expense_file, new_expense_dict)     
    
    #save_data_List_to_file(expense_list)
    
    
  elif a==4:   
    view_all_expense(expense_list)
    
  elif a==5:   
     view_category_wise_expense(expense_list)
  
  elif a==6:   
    view_category_wise_count(expense_list)
  
  elif a==7:   
      view_specific_category(expense_list)
          
  elif a==8:
      print("Load Data ")
      
  
  elif a==9:
     print("Budget")
     set_category_wise_budget() 
     
          
  elif a==0:
    print("Exit Program")
    break
      
          
  