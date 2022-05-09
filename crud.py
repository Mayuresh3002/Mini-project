#insert delete update

def createfile(ids,name,age,place,salary):
    #create
    
    file=open("login.txt","w")
    data=[]
    record=[ids,name,age,place,salary]
    data.append(record)
    print(data)

    for i,n,a,p,s in data:
        file.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^5}\n")
        print(i,n,a,p,s)
    file.close()
     

def addrecord(ids,name,age,place,salary):
    #insert
        
    file=open("login.txt","r")
    content=file.readlines()
    file.close()

    data=[]

    for row in content:
        data.append(row.strip().split())
    #print(data)

    newrecord=[ids,name,age,place,salary]
    data.append(newrecord)

    file=open("login.txt","w")
    for i,n,a,p,s in data:
        file.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^5}\n")
        print(i,n,a,p,s)
    file.close()


def delrecord():
    #delete
        
    file=open("login.txt","r")
    content=file.readlines()
    file.close()

    data=[]

    for row in content:
        data.append(row.strip().split())
    print(data)

    ids=input("Enter Id:")
    name=input("Enter Name:")
    age=input("Enter Age:")
    place=input("Enter Place:")
    salary=input("Enter Salary:")

    record=[ids,name,age,place,salary]
    data.remove(record)

    file=open("login.txt","w")
    for i,n,a,p,s in data:
        file.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^5}\n")
        print(i,n,a,p,s)
    file.close()


def ShowRec():
    #show
    file = open("login.txt","r")
    record = file.readlines()
    file.close()
    print(record)

    for d in record:
        print(d)


def updaterec(ids,name,age,place,salary):
    #Update
    file=open("login.txt","r")
    content=file.readlines()
    file.close()

    data=[]

    for row in content:
        data.append(row.strip().split())
    #print(data)

    
    newid=input("Enter New Id:")
    newname=input("Enter New Name:")
    newage=input("Enter New Age:")
    newplace=input("Enter New Place:")
    newsal=input("Enter New Salary:")

    
    file=open("login.txt","w")
    for i,n,a,p,s in data:
        file.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^5}\n")
        #print(i,n,a,p,s)
    file.close()

    addrecord(newid,newname,newage,newplace,newsal)
    Delrecord(ids,name,age,place,salary)
    




def Delrecord(ids,name,age,place,salary):
    #delete
        
    file=open("login.txt","r")
    content=file.readlines()
    file.close()

    data=[]

    for row in content:
        data.append(row.strip().split())
    #print(data)

    

    record=[str(ids),name,str(age),place,str(salary)]
    data.remove(record)

    file=open("login.txt","w")
    for i,n,a,p,s in data:
        file.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^5}\n")
        #print(i,n,a,p,s)
    file.close()









