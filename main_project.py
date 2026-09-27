#*******************************************start*******************************************
# this is main project
# importing other file of this project

import modify
import function_of_main_projects 
    
#main program's data

l=[["id","name","experince","salary"]]
flag=True

#main loop

while flag:
    
    #to give user choice

    print("-----plese select what you want to do-----")
    print("1 - FOR adding data")
    print("2 - FOR removeing data")
    print("3 - FOR show the spesific data")
    print("4 - FOR show all data")
    print("5 - FOR modify data")
    
    # taking user choice

    choice=int(input("enter your choice:"))
    
    # calling the function
    
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
#                                                                       -by priyesh patidar

