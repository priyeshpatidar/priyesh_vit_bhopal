# this is 3rd file which have other functions of main project

#***************************starting of this file***************************************

# function to add data in table

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

#function to remove a data from table

def remove(l):
    a=int(input("enter the id of the employ to remove"))
    for i in l:
        if i[0]==a:
            l.remove(i)
    return l

#function to show a data with emp_id

def show(l):
    a=int(input("enter the emp_id of the employee to display"))
    for i in l:
        if i[0]==a:
            print(i)    
            
#function to display all data in the data base

def show_all(l):
    for i in l:
        print(i)

#**************************this is end of this file *************************************
#***********************now this file is ready to import*********************************
#                                                                     -by Priyesh Patidar