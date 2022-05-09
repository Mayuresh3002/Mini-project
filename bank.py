class user():
    usercount = 0
    def __init__(s,f_name,Account_No,age):
        s.f_name= f_name
        s.Account_No = Account_No
        s.age = age

        user.usercount += 1

    def showdetails(s):
        print("f_name:",s.f_name)
        print("Account_No:",s.Account_No)
        print("age:",s.age)
        
              
class bank(user):
    def __init__(s,f_name,Account_No,age):
        super().__init__(f_name,Account_No,age)
        s.__balance = 0

    def viewbal(s):
        print(f"your account balance is --->{s.__balance}")

    def deposit(s,amount):
        s.__balance = s.__balance + amount
        print(f"your deposited amount is --->{amount}")

    def withdraw(s,amount):
        if(amount>=100 and s.__balance>amount):
            s.__balance = s.__balance - amount
            print(f"Your account balance is --->{s.__balance}")

        else:
            print(f"you have insufficient balance")

    def transfer(s,amount,user):
        if(s.__balance>=amount and amount> 0):
            s.__balance= s.__balance - amount
            print(f"Amount transfered to {user}")
            print(s.__balance)

        else:
            print(f"you have insufficient balance.")

f_name=input("enter your name: ")
Account_No=input("enter a A/c No.: ")
age=int(input("enter your age: "))

sbi=bank(f_name,Account_No,age)
print("Welcome to SBI bank")
sbi.showdetails()

print("D for deposit")
print("W for withdraw")
print("T for transfer")
print("V for viewbal")
print("E for Exit")

while(True):
    press = input("enter a button: ")
    if press.upper()=="D": 
           amount=int(input("enter amount: "))
           sbi.deposit(amount)
    elif press.upper()=="W":
        amount=int(input("enter amount: "))
        sbi.withdraw(amount)
    elif press.upper()=="T":
        amount=int(input("enter amount: "))
        user=input("enter a name: ")
        sbi.transfer(amount,user)
    elif press.upper()=="V":
        sbi.viewbal()
    elif press.upper()=="E":
        X=input("Are you sure?,(Y/N)")
        if X.upper()=="Y":
            break
        else:
            print("invalid button")
    else:
        print("invalid input")
                
            
        
