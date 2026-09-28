
# this is file for modify in main project
# this file have all the function for 2 nd file of main project

#***************************starting of this file***************************************

# id modify function

def change_id(l):
    a=int(input("enter the emp_id of the employee to change id:"))
    
    for i in l:
        if i[0]==a:
            new_id=int(input("enter new id for employ:"))
            print(i[0],"is changing to",new_id)
            i[0]=new_id
    else:
        print("emoloyee not found")
    return l

# name modify function

def change_name(l):
    a=int(input("enter the emp_id of the employee to change name:"))
    for i in l:
        if i[0]==a:
            new_name=input("enter new name of employ:")
            print(i[1],"is changing to",new_name)
            i[1]=new_name
    else:
        print("emoloyee not found")
    return l

# exprince modify function

def change_experince(l):
    a=int(input("enter the emp_id of the employee to change experince:"))
    for i in l:
        if i[0]==a:
            new_experince=int(input("enter new experince of employ:"))
            print(i[2],"is changing to",new_experince)
            i[2]=new_experince
    else:
        print("emoloyee not found")
    return l

# salary changing function

def change_salary(l):
    a=int(input("enter the emp_id of the employee to change salary:"))
    for i in l:
        if i[0]==a:
            new_salary=int(input("enter new salary of employ:"))
            print(i[3],"is changing to",new_salary)
            i[3]=new_salary
    else:
        print("emoloyee not found")
    return l

#**************************this is end of this file *************************************
#***********************now this file is ready to import*********************************
#                                                                     -by Priyesh Patidar
