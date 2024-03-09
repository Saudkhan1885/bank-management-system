import re
class BankAccount:                                               # class 
    def __init__(self, name, acc_number, balance,password,used=0):
        self.name = name
        self.acc_number = acc_number
        self.balance = balance
        self.used=used
        self.password=password
    
    def accounts_detail(self):
        print(f'''\t\t\t-------------------------------
        \t\t|| Name: {self.name}                
        \t\t|| Account Number: {self.acc_number} 
        \t\t|| Balance: {self.balance}           
        \t\t-------------------------------\n\n''')
        
        

class banklist:                                                      # class 
    def __init__(self):
        self.list=[BankAccount("",0,0,0) for _ in range (10)]
        self.course_count=0

# print all accounts
             
    def printall(self):
        
        for data in self.list:
            if data.used!=0:
                data.accounts_detail()
                print("\n")

#adding account 

    def adding(self):
        if self.course_count>10:
            print("No more bank account can be add")
        elif self.course_count<10 or self.course_count>0: 
            i=0
            i=int(input("Choose an index to add acount "))
            check=0
            while self.list[i].used==0:
                self.list[i].name = input("Enter the name: ")
                check+=1
                while not all(char.isalpha() or char.isspace() for char in self.list[i].name):
                        self.list[i].name = input("Invalid input. Enter only characters and spaces: ")
                self.list[i].acc_number = input("Enter the 11-digit account number: ")
                x = self.list[i].acc_number
                while len(x) != 11 or not x.isdigit():
                    x = input("Invalid input. Enter exactly 11 digits: ")
                    for account in self.list:
                        if account.acc_number == x:
                             while account.acc_number == x:
                                 print("This account number is already taken. Please try another.")
                                 x = input("Enter the 11-digit account number: ")
                                 while len(x) != 11 or not x.isdigit():
                                    x = input("Invalid input. Enter exactly 11 digits: ")
                    self.list[i].acc_number = x
 
                                
                self.list[i].balance=float(input("enter the balance "))
                self.list[i].used=1
                self.course_count+=1
                
                while True:
                    password = input("Set a password (must contain special characters, uppercase and lowercase letters): ")
                    if len(password) < 8:
                        print("Password must be at least 8 characters long.")
                    elif not re.search("[A-Z]", password):
                        print("Password must contain at least one uppercase letter.")
                    elif not re.search("[a-z]", password):
                        print("Password must contain at least one lowercase letter.")
                    elif not re.search("[!@#$%^&*()_+=\-{};':\",./<>?]", password):
                        print("Password must contain at least one special character.")
                    else:
                        self.list[i].password = password
                        break
                break
            if check==0:
                print("Account already exist on this index")
        else:
            print("no index must be between 0 and 10 ")
#delete account 

    def deleteaccount(self):
        Name=str(input("the name of account you want to delete "))
        count=0
        for nam in self.list:
            if nam.name==Name:
                print("Account found!")
                tries=0
                while tries<3:
                     Pass=input("plz enter your account password ")
                     if nam.password==Pass:
                       
                        nam.used=0
                        count+=1
                        self.course_count-=1
                        print("Account delete successfully")
                        break
                     else:
                       tries += 1
                       print(f"Password incorrect. {3-tries} attempt(s) remaining.")
            
        if count==0:
            print("sorry account not found ")   
                
            
#deposit money 

    def depositmoney(self):
        Name=input("enter the account name ")
        check=0
        for dep in self.list:
            if dep.name==Name:
                
                tries=0
                while tries<3:
                    Pass=input("plz enter your account password ")                
                    if dep.password==Pass:
                      print("your account current status is ")
                      dep.accounts_detail()
                      money=float(input("how much money do you want deposit "))
                      dep.balance+=money
                      print("your ",money,"money has been deposit to your account ")
                      print("your current balance is ",dep.balance," thanks")
                      check+=1
                      print("\n\n")
                      break
                    else:
                        tries+=1
                        print(f"Password incorrect. {3-tries} attempt(s) remaining.")
        if check!=0:
            print("money transfer successfully")
            print("\n\n")
            
# with drawal 
    def withdraw(self):
        check=0
        draw=input("Name of the account you want withdraw money ")
        for dra in self.list:
            if dra.name==draw:
                tries=0
                while tries<3:
                    Pass=input("plz enter your account password")
                    if dra.password==Pass:
                
                        dra.accounts_detail()
                        money=float(input("how much money do you want to withdraw "))
                        if dra.balance>=money:
                           dra.balance-=money
                           print("your account remaining balance is ",dra.balance)
                           check+=1                        
                           break
                        else:
                           print("As you see your current accout balance is not enough to withdraw your desired amount \nSorry!")
                    else:
                        tries+=1
                        print(f"Password incorrect. {3-tries} attempt(s) remaining.")
                        
        if check!=0:
            print("your money has been with draw ")
# transfer money 
    def transfer(self):
        check=0
        From=input("From which account do you want to transfer money ")
        for tran in self.list:
            if tran.name==From:
                tries=0
                while tries<3:
                    Pass=input("Plz enter your account password")
                    if tran.password==Pass:                  
                       tran.accounts_detail()
                       money=float(input("How much money do you want to withdraw "))
                       if tran.balance>=money:
                           tran.balance-=money
                           print("\tYour account remaining balance is ",tran.balance)
                           To=input("\n\nTo which account do you want to transfer money ")
                           for tran in self.list:
                              if tran.name==To:
                               print("your account found:")
                               print("Name",tran.name)
                               tran.balance+=money
                               print("So you transfer the ",money," money to ",tran.name)
                               check+=1
                               tries=4
                           break
                               
                       else:
                          print("As you see your current accout balance is not enough to withdraw your desired amount \nSorry!") 
                          break 
                    else:
                        tries+=1
                        print(f"Password incorrect. {3-tries} attempt(s) remaining.")                      
        if check==0: 
             print("there is no account on this name  ")
        
# account update    
    def account_update(self):
        print("your account plz ")
        choice=0
        name=input("Account name ?")
        for nam in self.list:
            if nam.name==name:
                tries=0
                while tries<3:
                    Pass=input("Plz enter your account password")
                    if nam.password==Pass:                  
                      nam.accounts_detail()
                      print("\n\n Sorry to say this \n\tBut due to bank security issues you only change your name not number ")
                      check=input("you want to change your name \n Yes \n No ")
                      if check=="yes" or check=="YES":
                        nam.name=input("your account new name ")
                        choice+=1
                        while not all(char.isalpha() or char.isspace() for char in nam.name):
                           nam.name = input("Invalid input. Enter only characters and spaces: ")
                        break
                      elif check=="no" or check=="NO":
                         print("Thank you ")
                         break
                    else:
                        tries+=1
                        print(f"Password incorrect. {3-tries} attempt(s) remaining.") 
                    
        if choice==0:
                print("sorry there is no account on this name ")
# specific account
    def specific_account(self):
        name=input("your account name plz")
        choice=0
        while not name.isalpha():
            name=input("Invalid input. Enter only characters:")     
        for search in self.list:
            if search.name==name:
                tries=0
                while tries<3:
                    Pass=input("Plz enter your account password")
                    if search.password==Pass:
                      search.accounts_detail() 
                      choice+=1
                      break
                    else:
                        tries+=1
                        print(f"Password incorrect. {3-tries} attempt(s) remaining.") 
                      
        if choice==0:
            print("sorry there is no account on this name ")
                
  # main area               
    
                
choice = 0
bank_list=banklist()

while choice != 10:
    print('''\n         ----(Welcom to Bank system)---- \n           
             (1) Create account
             (2) delete specific account
             (3) deposit money 
             (4) View all account
             (5) Money withdrawel 
             (6) Transfer money 
             (7) Account update 
             (8) specific account 
             (10) quite \n\n''')
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("WELCOME TO CREATING BANK ACCOUNT\n\n")
        bank_list.adding()
    elif choice==2:
        bank_list.deleteaccount()
    elif choice==3:
        bank_list.depositmoney()
    elif choice == 4:
        print("\n\t\t\t------[All ACCOUNTS IN THE BANK]-------\n")
        bank_list.printall()
    elif choice==5:
        bank_list.withdraw()
    elif choice==6:
        bank_list.transfer()
    elif choice==7:
        bank_list.account_update()
    elif choice==8:
        bank_list.specific_account()   
    

print("Thank you for your cooperation")