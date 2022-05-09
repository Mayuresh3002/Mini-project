class Employees():
    empcount=0
    incamt=1.10
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary
        self.email=f"{self.first.lower()}.{self.last.lower()}@itv.com"
        Employees.empcount+=1


    def increment(self):
        self.salary=self.salary*self.incamt

    def fullname(self):
        return f"{self.first} {self.last}"


class Developer(Employees):
    incamt=1.30

    def __init__(self,first,last,salary,prolang):
        super.__init__(first,last,salary)
        self.prolang=prolang
        
class Manager(Employees):
    def __init__(self,first,last,salary,employees=None):
        super().__init__(first,last,salary)

        if(employees is None):
            self.employees=[]
        else:
            self.employees =employees

    def addemp(self,emp):
        if(emp not in self.employees):
            self.employees.append(emp)

    def removeemp(self,emp):
        if(emp in self.employees):
            self.employees.remove(emp)

    def printemp(self):
        for emp in self.employees:
            print(f"----> {emp.fullname()}")



















        
