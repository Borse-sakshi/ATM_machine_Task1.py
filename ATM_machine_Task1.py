/*
OctaNet Service Pvt Ltd
Sakshi Borse
Task 1
*/
import time 

print("please insert your card")

time.sleep(5)

password = 1624

pin = int(input("enter your atm pin"))

balance = 10000

if pin == password:
    while True:
    
        print("""
            1 == balance
            6 == withdraw balance
            2== deposit balance
            4 == exit
            """
              ) 
        try:
            option = int(input("please enter your choice"))
        except:
            print("Please enter valid option") 
        
        if option == 1:
            print(f"your current balance is {balance}")  
            
            print("=========================================")
            print("=========================================")

        if option == 6:

            withdraw_amount = int(input("please enter withdraw_amount "))

            print("=========================================")

            balance = balance - withdraw_amount

            print(f"{withdraw_amount} is debited from your account")
             
            print("=========================================")

            print(f"your current balance is {balance}")

            print("=========================================")
            print("=========================================")

        if option == 2:
            
            deposit_amount = int(input("please enter deposit_amount"))

            print("=========================================")
            
            balance = balance + deposit_amount
            
            print(f"{deposit_amount} is credited to your account")

            print("=========================================")

            print(f"your updated balance is {balance}")
            
            print("=========================================")
            print("=========================================")
        
        if option == 4:
            
            break 
            print("====================XXX=====================")   

else:
    print("wrong pin please try again")
