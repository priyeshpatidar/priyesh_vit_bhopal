#this is second file of project 
#this file will have moify function 

#***************************starting of this file***************************************

#importing function file in this 

import function_of_modify as f_o_m

#main function of modify

def modify_table(l):
    print("enter what you want to modify")
    print("1 for emp_id:")
    print("2 for name:")
    print("3 for experince")
    print("4 for salary")
    c=int(input("enter you choice"))
    if c==1:
        l=f_o_m.change_id(l)
    elif c==2:
        l=f_o_m.change_name(l)
    elif c==3:
        l=f_o_m.change_experince(l)
    elif c==4:
        l=f_o_m.change_salary(l)
    else:
        print("invalid choice")



