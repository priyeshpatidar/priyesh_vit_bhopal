#*******************************************start*******************************************
# this is main project
# in this file we are importing all other file of this project

import modify
import function_of_main_projects 
    
#main program's data

l=[["id","name","experince","salary","date of joining","status"]]
flag=True

#main loop

while flag:
    
    #to give user choice

    print("-----------plese select what you want to do-----")
    print("1 - FOR adding data")
    print("2 - FOR removeing data")
    print("3 - FOR show the spesific data")
    print("4 - FOR show all data")
    print("5 - FOR modify data")
    print("6 - FOR exit")
    print("7 - FOR increase the salary of an employ")
    print("-------------------------------------------------")

    # taking user choice
    
    try:
        choice=int(input("enter your choice:"))
    except ValueError:
        print("invalid choice")
        continue
    
    # to geting the function of other file according to user choice
    
    if choice==1:
        f=function_of_main_projects.add_data(l)
    elif choice==2:
        f=function_of_main_projects.remove(l)
    elif choice==3:
        function_of_main_projects.show(l)
    elif choice==4:
        function_of_main_projects.show_all(l)
    elif choice==5:
        modify.modify_table(l)
    elif choice==6:
        flag=False
    elif choice==7:
        function_of_main_projects.increase_salary(l)
    else:
        print("invalid choice")
        
    print("-------------------------------------------------")

#**********************************end of program******************************************
#                                                                       -by priyesh patidar
#**************************this is end of this file ***************************************
