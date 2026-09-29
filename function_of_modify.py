
# this is file for modify in main project
# this file have all the function for 2 nd file of main project

#***************************starting of this file***************************************

# id modify function

def change_id(l):
    
    try:
        a=int(input("enter the emp_id of the employee to change id:"))
    except ValueError:
        print("please enter valid emp_id")
        return l
    
    for i in l:
        if i[0]==a:
            print("current id of employ is:",i[0],
                  "current name of employ is:",i[1],
                  "current experince of employ is:",i[2],
                  "current salary of employ is:",i[3],
                  "current date of joining of employ is:",i[4],
                  "current status of employ is:",i[5]
                    
                  )
            new_id=int(input("enter new id for employ:"))
            print(i[0],"is changing to",new_id)
            i[0]=new_id
    else:
        print("emoloyee not found")
    return l

# name modify function

def change_name(l):
    try:
        a=int(input("enter the emp_id of the employee to change name:"))
    except ValueError:
        print("please enter valid emp_id")
        return l
    for i in l:
        if i[0]==a:
            new_name=input("enter new name of employ:")
            print(i[1],"is changing to",new_name)
            i[1]=new_name
    return l

# exprince modify function

def change_experince(l):
    a=int(input("enter the emp_id of the employee to change experince:"))
    for i in l:
        if i[0]==a:
            new_experince=int(input("enter new experince of employ:"))
            print(i[2],"is changing to",new_experince)
            i[2]=new_experince
    return l

# salary changing function

def change_salary(l):
    a=int(input("enter the emp_id of the employee to change salary:"))
    for i in l:
        if i[0]==a:
            new_salary=int(input("enter new salary of employ:"))
            print(i[3],"is changing to",new_salary)
            i[3]=new_salary
    return l

# date of joining changing function 

def change_date_of_joining(l):
    a=int(input("enter the emp_id of the employee to change date of joining:"))
    for i in l:
        if i[0]==a:
            new_date_of_joining=input("enter new date of joining of employ:")
            print(i[4],"is changing to",new_date_of_joining)
            i[4]=new_date_of_joining
    return l

# status changing function

def change_status(l):
    a=int(input("enter the emp_id of the employee to change status:"))
    for i in l:
        if i[0]==a:
            new_status=input("enter new status of employ (active/inactive):")
            print(i[5],"is changing to",new_status)
            i[5]=new_status
    return l

#**************************this is end of this file *************************************
#***********************now this file is ready to import*********************************
#                                                                     -by Priyesh Patidar