#this is second file of project 
#this file will have modify function 

#***************************starting of this file***************************************

#importing function file in this 

import function_of_modify as f_o_m

#main function of modify

def modify_table(l):
    print("-----------enter what you want to modify-----------------")
    print("1 - for emp_id:")
    print("2 - for name:")
    print("3 - for experince")
    print("4 - for salary")
    print("5 - for date of joining")
    print("6 - for status")
    print("7 - for exit")
    print("----------------------------------")
    
    # taking user choice

    try:
        c=int(input("enter you choice"))
    except ValueError:
        print("invalid choice")
        return l

    # calling the function
    
    if c==1:
        l=f_o_m.change_id(l)
    elif c==2:
        l=f_o_m.change_name(l)
    elif c==3:
        l=f_o_m.change_experince(l)
    elif c==4:
        l=f_o_m.change_salary(l)
    elif c==5:
        l=f_o_m.change_date_of_joining(l)
    elif c==6:
        l=f_o_m.change_status(l)
    elif c==7:
        print("exiting from modify")
    else:
        print("invalid choice")
        modify_table(l)

#**************************this is end of this file *************************************
#***********************now this file is ready to import*********************************
#                                                                     -by Priyesh Patidar

