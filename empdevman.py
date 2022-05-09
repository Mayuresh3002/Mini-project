class Employee():
    empcount = 0
    incamt = 1.10 
    
    def __init__(self, first, last, salary):
        self.first = first 
        self.last = last
        self.salary = salary

        self.email = first.lower()+"."+last.lower()+"@itvedant.com"
        Employee.empcount +=1


    def intro(self):
        return f"{self.first.title()}\n{self.last.title()}\n{self.email}\n{self.salary} "
    

    def increment(self,incamt):
        self.incamt=incamt
        self.salary = self.salary * self.incamt
        return self.salary


class Developer(Employee):
    incamt=1.30
    def __init__(self, first, last, salary, prolang):
        super().__init__(first, last, salary)
        self.prolang = prolang

    def intro(self):
        return f"{self.first.title()}\n{self.last.title()}\n{self.email}\n{self.prolang}"


class Manager(Employee):
    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)

        if(employees is None):
            self.employees = []
        else:
            self.employees = employees
            
    def addemp(self, emp):
        if(emp not in self.employees):
            self.employees.append(emp)
            
    def removeemp(self, emp):
        if(emp in self.employees):
            self.employees.remove(emp)

    def printemp(self):
        for emp in self.employees:
            print(f"---> {emp.intro()}")



        

emp1 = Employee("aj","jena", 10000)
emp2 = Employee("dk","rastogi", 30000)
emp3 = Employee("vishvas","raj", 40000)


mgr1 = Manager('mangesh','Yadav', 70000, [emp1, emp2, emp3])

dev1 = Developer("pratik","shetty", 140000,'Python')
dev2 = Developer("ninad","more", 320000,'Python')
dev3 = Developer("shubam","lotlikar", 230000,'Django')
mgr2 = Manager('jimmy','rella', 70000, [dev1, dev2, dev3])

dev4 = Developer("sagar","kedar", 210000,'Python')

while True:
        print("\n")
        print("Enter 1 to Add Employee")
        print("Enter 2 to Add Developer")
        print("Enter 3 to Add Manager")
        print("Enter 4 to Show Employee Details")
        print("Enter 5 to Show Developer Details")
        print("Enter 6 to Show Manager Details")
        print("Enter 7 to Increment Employee Salary")
        print("Enter 8 to Increment Developer Salary")
        print("Enter 9 to Increment Manager Salary")
        print("Enter 10 to Add Employee in Manager")
        print("Enter 11 to Add Developer in Manager")
        print("Enter 12 to Delete Employee from Manager")
        print("Enter 13 to delete Developer from Manager")
        print("Enter 14 to Show Employees and Developer under Manager")
        print("Enter 15 to Exit")
        print("\n")

        choice = input("Enter Your Choice : ").strip()
        print("\n")

        if choice=="1":
            fname=input("enter emp first name: ").strip()
            lname=input("enter emp last name: ").strip()
            sal=float(input("enter sal : "))

            obj1=Employee(fname,lname,sal)

        elif choice=="2":
            fname=input("enter emp first name: ").strip()
            lname=input("enter emp last name: ").strip()
            sal=float(input("enter sal : "))
            prolang=input("enter prog lang: ").strip()

            obj2=Developer(fname,lname,sal,prolang)

        elif choice=="3":
            fname=input("enter emp first name: ").strip()
            lname=input("enter emp last name: ").strip()
            sal=float(input("enter sal : "))

            obj3=Manager(fname,lname,sal)

        elif choice=="4":
            print('''
                1:emp1
                2:emp2
                3:emp3
                4:emp4
                ''')
            inp=int(input("Proceed:"))
            if(inp==1):
                    
                a=emp1.intro()
                print(a)
            elif(inp==2):
                b=emp2.intro()
                print(b)
            elif(inp==3):
                c=emp3.intro()
                print(c)
            elif(inp==4):
                d=obj1.intro()
                print(d)

        elif choice=="5":
            print('''
                1:developer1
                2:developer2
                3:developer3
                4:developer4
                5:developer5
                    ''')
            inp1=int(input("Proceed:"))
            if(inp1==1):
                a=dev1.intro()
                print(a)
            elif(inp1==2):
                b=dev2.intro()
                print(b)
            elif(inp1==3):
                c=dev3.intro()
                print(c)
            elif(inp1==4):
                d=dev4.intro()
                print(d)
            elif(inp1==5):
                e=obj2.intro()
                print(e)

        elif choice=="6":
            print('''
                1: Manger1
                2: Manager2
                3: Manager3
                    ''')
            inp2=int(input("Proceed:"))
            if(inp2==1):
                a=mgr1.intro()
                print(a)
            elif(inp2==2):
                b=mgr2.intro()
                print(b)
            elif(inp2==3):    
                c=obj3.intro()
                print(c)

        elif choice=="7":
            incamt=1.10
            emp=input("Enter Employee:")
            if(emp=="emp1"):
                a=emp1.increment(incamt)
                print(a)
            elif(emp=="emp2"):
                b=emp2.increment(incamt)
                print(b)
            elif(emp=="emp3"):
                c=emp3.increment(incamt)
                print(c)
            elif(emp=="emp4"):
                d=obj1.increment(incamt)
                print(d)

        elif choice=="8":
            incamt=1.30
            dev=input("Enter Developer:")
            if(dev=="dev1"):
                a=dev1.increment(incamt)
                print(a)
            elif(dev=="dev2"):
                b=dev2.increment(incamt)
                print(b)
            elif(dev=="dev3"):
                c=dev3.increment(incamt)
                print(c)
            elif(dev=="dev4"):
                d=dev4.increment(incamt)
                print(d)
            elif(dev=="dev5"):
                e=obj2.increment(incamt)
                print(e)

        elif choice=="9":
            incamt=2.5
            mg=input("Enter Manager:")
            if(mg=="mgr1"):
                a=mgr1.increment(incamt)
                print(a)
            elif(mg=="mgr2"):
                b=mgr2.increment(incamt)
                print(b)
            elif(mg=="mgr3"):
                c=obj3.increment(incamt)
                print(c)
            

        elif choice=="10":
            
            g=obj3.addemp(obj1)
            print(g)

        elif choice=="11":
            h=obj3.addemp(obj2)
            print(h)

        elif choice=="12":
            i=obj3.removeemp(obj1)
            print(i)

        elif choice=="13":
            j=obj3.addemp(obj2)
            print(j)

        elif choice=="14":
            k=obj3.printemp(obj2)
            print(k)

        elif choice=="15":
            ext=input("Are You Sure You Want To Exit? (Y/N):").lower()
            if(ext==y):
                break
            elif(ext==n):
                continue
            else:
                print("Invalid Response")

        else:
            print("Invalid Response")

        
            
            

            





































































