("\nwelcome to my computer....!".title())
print("\nHelp center:")
print("1:list directory".title())
print("2:create directory".title())
print("3.show current directory".title())
print("4.delete folder".title())
print("5.create file".title())
print("6:delete file".title())
print("7:Exit\n")

while(True):
    import os


    n=int(input("select Operation: "))

    if(n==1):
        print(os.listdir())

    elif(n==2):
        newfolder=input("Folder Name: ").strip().lower()
        makedir=os.mkdir(newfolder)

    elif(n==3):
        currentdir=os.getcwd()
        print("Current Directory",currentdir)

    elif (n==4):
        deletefolder=input("Enter folder name delete :").strip().lower()
        removefolder=os.rmdir(deletefolder)

    elif(n==6):
        deletefile=input("Enter file name you want to delete :").strip().lower()
        removefile=os.remove(deletefile)

    elif(n==5):
        Name=input("Enter name of file with extension: ".title())
        file=open(f"{Name}","w")
        content=input("enter content here: ")
        cont=file.write(content)
        print(f"file {Name} created successfully..!")
        file.close()

    elif(n==7):
        ext=input("are you sure, you want to exit? (Y/N): ")
        if(ext.lower()=="y"):
            break
        elif(ext.lower()=="n"):
            continue
        else:
            print("Invalid Response")
            print("Please Select Valid Response")

    































        
        
        
        
