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


def remove(l):
    a=int(input("enter the id of the employ to remove"))
    for i in l:
        if i[0]==a:
            l.remove(i)
    return l
    ...

def show(l):
    ...

def show_all(l):
    for i in l:
        print(i)


l=[["id","name","experince","salary"]]
flag=True
while flag:
    print("-----plese select what you want to do-----")
    print("1 - for adding data")
    print("2 - for removeing data")
    print("3 - for show the spesific data")
    print("4 - for show all data")
    choice=int(input("enter your choice"))
    if choice==1:
        l=add_data(l)
    elif choice==2:
        l=remove(l)
    elif choice==4:
        show_all(l)


















