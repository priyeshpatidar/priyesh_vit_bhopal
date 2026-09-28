#this is second file of project 
#this file will have modify function 

#***************************starting of this file***************************************

#importing function file in this 

import function_of_modify as f_o_m

#main function of modify

def modify_table(l):

    # giving user choice
    
    print("------enter what you want to modify------")
    print("1 for emp_id:")
    print("2 for name:")
    print("3 for experince")
    print("4 for salary")
    
    # taking user choice
    
    c=int(input("enter you choice:"))
    
    # calling the function
    
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
        modify_table(l)

#**************************this is end of this file *************************************
#***********************now this file is ready to import*********************************
#                                                                     -by Priyesh Patidar

