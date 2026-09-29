# this is 3rd file which have other functions of main project

#***************************starting of 3rd file***************************************
#this file have other functions of main project which is used in main.py file
# function to add data in table

def add_data(l):
    n=int(input("enter no of data to add :"))
    for i in range(n):
        x=[]
        try:
            id=int(input("enter id :"))
            name=input("enter name of employ :")
            experince=int(input("enter experince in years :"))
            salary=int(input("enter salary :"))
            date_of_joining=input("enter date of joining (dd/mm/yyyy):")
            status=input("enter status of employ (active/inactive):")
            x=[id,name,experince,salary,date_of_joining,status]
            l.append(x)
            print("data added successfully")
        except ValueError:
            print ("invalid input")
            print("please enter valid input")
            add_data(l)
    return l

#function to remove a data from table

def remove(l):
    try:
        n=int(input("enter no of data to remove "))
    except ValueError:
        print("invalid input")  
        print("please enter valid input")
        remove(l)
    for i in range(n):
        a=int(input("enter the id of the employ to remove"))
        for i in l:
            if i[0]==a:
                l.remove(i)
                print("data removed successfully")
    return l

#function to show a data with emp_id

def show(l):
    try:
        n=int(input("enter no of data to show "))       
    except ValueError:
        print("invalid input")
        print("please enter valid input")
        show(l)
    for i in range(n):
        a=int(input("enter the emp_id of the employee to display"))
        for i in l:
            if i[0]==a:
                print("Employee id:",i[0],"Employee name:",i[1],"Employee experience:",i[2],"Employee salary:",i[3],"Date of Joining:",i[4],"Status:",i[5])

#function to display all data in the data base

def show_all(l):
    if len(l)==1:
        print("no data in the table")   
    else:
        for i in l:
            print("Employee id:",i[0],"Employee name:",i[1],"Employee experience:",i[2],"Employee salary:",i[3],"Date of Joining:",i[4],"Status:",i[5])

#function to increase the salary of an employ
def increase_salary(l):
    try:
        a=int(input("enter the emp_id of the employee to increase salary:"))
    except ValueError:
        print("please enter valid emp_id")
        return l
    for i in l:
        if i[0]==a:
            increase_amount=int(input("enter the amount to increase the salary by:"))
            new_salary=i[3]+increase_amount
            print(i[3],"is changing to",new_salary)
            i[3]=new_salary
            print("salary increased successfully")
    return l


#**************************this is end of this file *************************************
#***********************now this file is ready to import*********************************
#                                                                     -by Priyesh Patidar