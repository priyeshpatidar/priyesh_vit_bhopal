#*******************************************start*******************************************

#TO add data in table

def add_data(l):
    n=int(input("enter no of data "))
    for i in range(n):
        x=[]
        id=int(input("enter id :"))
        name=input("enter name of employ :")
        experince=int(input("enter experince in years :"))
        salary=int(input("enter salary :"))
        x=[id,name,experince,salary]
        l.append(x)
    return l

#to remove a data from table

def remove(l):
    a=int(input("enter the id of the employ to remove"))
    for i in l:
        if i[0]==a:
            l.remove(i)
    return l

#to show a data with emp_id

def show(l):
    a=int(input("enter the emp_id of the employee to display"))
    for i in l:
        if i[0]==a:
            print(i)    
            
#to display all data in the data base

def show_all(l):
    for i in l:
        print(i)
    
#main program's data

l=[["id","name","experince","salary"]]
flag=True

#main loop

while flag:
    
    #to give user choice

    print("-----plese select what you want to do-----")
    print("1 - for adding data")
    print("2 - for removeing data")
    print("3 - for show the spesific data")
    print("4 - for show all data")
    
    # to calling function

    choice=int(input("enter your choice"))
    if choice==1:
        l=add_data(l)
    elif choice==2:
        l=remove(l)
    elif choice==3:
        show(l)
    elif choice==4:
        show_all(l)
    else:
        print("invalid choice")
        
#to check if user want to continue
       
    c=input("do you want to continue(y/n)")
    c=str(c)
    if c=="y" or c=="Y":
        print("ok")
    elif c=="n"or c=="N":
        flag=False
    else:
        print("invalid choice ")

#**********************************end of program******************************************
#by priyesh patidar

