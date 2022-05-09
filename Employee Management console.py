import pymysql as p

def getconnect():
    return p.connect(host="localhost", user="root", password="", database="companyinfo")


def insertdata(t):
    db=getconnect()
    cr=db.cursor()
    sql="insert into empinfo values(%s,%s,%s,%s,%s)"
    cr.execute(sql,t)
    print("Data Added Successfully")
    db.commit()
    db.close()
    
def updatedata(t):
    db=getconnect()
    cr=db.cursor()
    sql="update empinfo set Name=%s, Department=%s, Salary=%s, Location=%s where Id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()

def updateNameByID(t):
    db=getconnect()
    cr=db.cursor()
    sql="update empinfo set Name=%s where Id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()

def updateDeptByID(t):
    db=getconnect()
    cr=db.cursor()
    sql="update empinfo set Department=%s where Id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()

def updateSalByID(t):
    db=getconnect()
    cr=db.cursor()
    sql="update empinfo set Salary=%s where Id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()

def updateLocByID(t):
    db=getconnect()
    cr=db.cursor()
    sql="update empinfo set Location=%s where Id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()

def deleterow(t):
    db=getconnect()
    cr=db.cursor()
    sql="delete from empinfo where Id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()

def deleteName(t):
    db=getconnect()
    cr=db.cursor()
    sql="update empinfo set Name=Null where Id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()
    

def deleteDept(t):
    db=getconnect()
    cr=db.cursor()
    sql="update empinfo set Department=Null where Id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()


def deleteSal(t):
    db=getconnect()
    cr=db.cursor()
    sql="update empinfo set Salary=Null where Id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()


def deleteLoc(t):
    db=getconnect()
    cr=db.cursor()
    sql="update empinfo set Location=Null where Id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()


def fetch():
    db=getconnect()
    cr=db.cursor()
    sql ="select * from empinfo"
    cr.execute(sql)
    data=cr.fetchall()
    for d in data:
        print (f"{d[0]:^3} {d[1]:^10} {d[2]:^30} {d[3]:^20} {d[4]:^20}")
    db.commit()
    db.close()

def fetchName(t):
    db=getconnect()
    cr=db.cursor()
    sql ="select Name from empinfo where ID=%s"
    cr.execute(sql)
    data=cr.fetchall()
    for d in data:
        print (f"{d[1]:^3}")
    db.commit()
    db.close()


def fetchDept(t):
    db=getconnect()
    cr=db.cursor()
    sql ="select Department from empinfo where ID=%s"
    cr.execute(sql)
    data=cr.fetchall()
    for d in data:
        print (f"{d[2]:^20}")
    db.commit()
    db.close()


def fetchSal(t):
    db=getconnect()
    cr=db.cursor()
    sql ="select Salary from empinfo where ID=%s"
    cr.execute(sql)
    data=cr.fetchall()
    for d in data:
        print (f"{d[3]:^20}")
    db.commit()
    db.close()


def fetchLoc(t):
    db=getconnect()
    cr=db.cursor()
    sql ="select Location from empinfo where ID=%s"
    cr.execute(sql)
    data=cr.fetchall()
    for d in data:
        print (f"{d[4]:^20}")
    db.commit()
    db.close()
    

abc=True
while(abc):
    print("""
         Database operations as follows :
         To Insert records, Press '1'
         To Update records, Press '2'
         To Delete records, Press '3'
         To View records, Press '4'
         To Exit the app, Press 'e'
         """)

    a=input("Enter your choice :")

    if(a=="1"):
        b=int(input("Enter Id number :"))
        c=input("Enter the Name :")
        d=input("Enter the Department :")
        e=int(input("Enter the Salary :"))
        f=input("Enter the Location :")
        t=(b,c,d,e,f)
        insertdata(t)

    elif(a=="2"):
        print("""Select What to Update,
                 To Update Name, Select 1
                 To Update Department, Select 2
                 To Update Salary, Select 3
                 To Update Location, Select 4
                 To Update All details, Select 5
                 """)

        x=input("Enter Your Choice :")
        if(x=="1"):
            b=int(input("Enter Id whose Name is to be Updated :"))
            c=input("Enter Name :")
            t=(c,b)
            updateNameByID(t)

        elif(x=="2"):
            b=int(input("Enter Id whose Department is to be Updated :"))
            c=input("Enter Department :")
            t=(c,b)
            updateDeptByID(t)

        elif(x=="3"):
            b=int(input("Enter Id whose Salary is to be Updated :"))
            c=int(input("Enter Salary :"))
            t=(c,b)
            updateSalByID(t)

        elif(x=="4"):
            b=int(input("Enter Id whose Location is to be Updated :"))
            c=input("Enter Location :")
            t=(c,b)
            updateLocByID(t)            
        
        elif(x=="5"):
            b=int(input("Enter Id whose details to be Updated:"))
            c=input("Enter Name :")
            d=input("Enter Department :")
            e=int(input("Enter Salary :"))
            f=input("Enter Location :")
            t=(c,d,e,f,b)
            updatedata(t)            

        else:
            print("Invalid Selection")
            
    elif(a=="3"):
        print("""Select What to Delete,
                 To Delete Name, Select 1
                 To Delete Department, Select 2
                 To Delete Salary, Select 3
                 To Delete Location, Select 4
                 To Delete All details, Select 5
                 """)

        x=input("Enter Your Choice :")
        if(x=="1"):
            b=int(input("Enter Id whose Name is to be deleted :"))
            c=input("Enter Name :")
            t=(c,b)
            deleteName(t)

        elif(x=="2"):
            b=int(input("Enter Id whose Department is to be deleted :"))
            c=input("Enter Department :")
            t=(c,b)
            deleteDept(t)

        elif(x=="3"):
            b=int(input("Enter Id whose Salary is to be deleted :"))
            c=int(input("Enter Salary :"))
            t=(c,b)
            deleteSal(t)

        elif(x=="4"):
            b=int(input("Enter Id whose Location is to be deleted :"))
            c=input("Enter Location :")
            t=(c,b)
            deleteLoc(t)            
        
        elif(x=="5"):
            t=int(input("Enter Id whose details to be deleted:"))
            deleterow(t)            

        else:
            print("Invalid Selection")

    elif(a=="4"):
        print("""Select What to View,
                 To View Name, Select 1
                 To View Salary, Select 2
                 To View Department, Select 3
                 To View Location, Select 4
                 To View All details, Select 5
                 """)

        x=input("Enter Your Choice :")
        if(x=="1"):
            t=int(input("Enter Id to fetch it's Name :"))
            fetchName(t)

        elif(x=="2"):
            t=int(input("Enter Id to fetch it's Department :"))            
            fetchDept(t)

        elif(x=="3"):
            t=int(input("Enter Id to fetch it's Salary :"))
            fetchSal(t)

        elif(x=="4"):
            t=int(input("Enter Id to fetch it's Location :"))
            fetchLoc(t)            
        
        elif(x=="5"):
            fetch()            

        else:
            print("Invalid Selection")


    elif(a=="e"):
        abc=False
        break
        
    else:
        print("Syntax Error : Invalid Option")
        
        
