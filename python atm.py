import time
print("Please insert your Card")
time.sleep(5)
password=1234
pin=int(input("Enter your atm pin"))
balance=5000
if pin==password:
    while True:
        print("""
          1 == balance
          2 == withdraw
          3 == deposite
          4 == exit """)
        try:
            option=int(input("Please enter your choice"))
        except:
            print("Please enter valid option")
        if option==1:
            print(f"Your current balance is {balance}")
        if option==2:
            withdraw_amount=int(input("Please enter withdrawal amount"))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount } is deducted from your account")  
            print(f"your current balance is {balance}")   
        if option==3:
            deposite_amount=int(input("Please enter deposite_amount"))
            balance=balance+deposite_amount
            print(f"{deposite_amount} is credited to your account") 
            print(f"Your updated balance is {balance}")
        if option==4:
            break             
else:
    print("wrong pin inserted")


