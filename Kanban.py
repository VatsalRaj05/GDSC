import pickle
import os
if not os.path.exists("storage"):
    proj_list={}
    with open("storage","wb") as f:
        pickle.dump(proj_list,f)


with  open("storage",'rb') as f:
    proj_list=pickle.load(f)
 

def task_disp(s_field,l_name):
    print(f"Here's the list of {s_field} tasks for this project:")
    for i,elem in enumerate(l_name,1):
        print(f"{i}. {elem}")
    print("\n")
    if not l_name:
        print("Empty Task List\n")

def task_add(s_field,k_val):
    det=input("Enter the Details:")
    proj_list[k_val][s_field].append(det)

def task_remove(s_field,k_val):
    field_lst = proj_list[k_val][s_field]
    print("Here's the list of Todo tasks for this project:")
    for i,elem in enumerate(field_lst,1):
        print(f"{i}. {elem}")
    b=int(input("Enter the S.No. of task to be removed: "))
    if 1 <= b <= len(field_lst):
        del field_lst[b-1]
        print("Removed successfully\n")
    else:
        print("Invalid task number.\n")

def todo(proj):
    while True:
        t_list=list(proj_list[proj]["Todo"])
        print("Enter task: ")
        print("1. Add Task \n2. Display Task\n3. Remove Task\n4. Back")
        op=int(input("Enter Option : "))
        if op==1:
            task_add("Todo",proj)
        elif op==2:
            task_disp("Todo",t_list)
        elif op==3:
            task_remove("Todo",proj)
        elif op==4:
            return
        else:
            print("Invaid input\n")

def InProgress(proj):
    while True:
        p_list=list(proj_list[proj]["InProgress"])
        print("Enter task: ")
        print("1. Add Task \n2. Display Task\n3. Remove Task\n4. Back")
        op=int(input("Enter Option : "))
        if op==1:
            task_add("InProgress",proj)
        elif op==2:
            task_disp("InProgress",p_list)
        elif op==3:
            task_remove("InProgress",proj)
        elif op==4:
            return
        else:
            print("Invaid input\n")

def done(proj):
    while True:
        d_list=list(proj_list[proj]["Done"])
        print("Enter task: ")
        print("1. Add Task \n2. Display Task\n3. Remove Task\n4. Back")
        op=int(input("Enter Option : "))
        if op==1:
            task_add("Done",proj)
        elif op==2:
            task_disp("Done",d_list)
        elif op==3:
            task_remove("Done",proj)
        elif op==4:
            return
        else:
            print("Invaid input\n")

def Ready_for_review(proj):
    while True:
        r_list=list(proj_list[proj]["Ready to review"])
        print("Enter task: ")
        print("1. Add Task \n2. Display Task\n3. Remove Task\n4. Back")
        op=int(input("Enter Option : "))
        if op==1:
            task_add("Ready to review",proj)
        elif op==2:
            task_disp("Ready to review",r_list)
        elif op==3:
            task_remove("Ready to review",proj)
        elif op==4:
            return
        else:
            print("Invaid input\n")

def DispProj():
    if not proj_list:
        print("No projects found.")
    else:
        print("Here's the list of Projects:")
        for i, key in enumerate(proj_list.keys(), 1):
            print(f"{i}. {key}")

def AddProj():
    global proj_list 
    a=input("Enter the name of the project: ")
    proj_list[a]={"Todo":[],"InProgress":[],"Done":[],"Ready to review":[]}
    print("Added successfully")

def OpenProj():
    while True:
        DispProj()
        a=int(input("Enter the S.No. of project to be opened:"))
        Proj_Det_List = list(proj_list.values())
        Proj_name_list = list(proj_list.keys())
        if 1 <= a <= len(Proj_Det_List):
            c_proj = Proj_Det_List[a-1]
            for i, key in enumerate(c_proj.keys(), 1):
                print(f"{i}. {key}")
            print(i+1,". Exit")
            j = int(input('Enter your choice:'))
            if j==1:
                todo(Proj_name_list[a-1])
            elif j==2:
                InProgress(Proj_name_list[a-1])
            elif j==3:
                Ready_for_review(Proj_name_list[a-1])
            elif j==4:
                done(Proj_name_list[a-1])
            elif j==5:
                return
            else:
                print("Enter valid option")
            with open("storage","wb") as f:
                pickle.dump(proj_list,f)

        else:
            print("Invalid project number")
        print("\n")

def Delete():
    DispProj()
    Proj_name_list = list(proj_list.keys())
    a=int(input("Enter the S.No. of project to be deleted:"))
    del proj_list[Proj_name_list[a-1]]

print("----------Welcome to Kanban Board----------")
while True:
    print("MAIN MENU")
    print("1. Add Project\n2. Display Projects\n3. Open Projects\n4. Delete a project\n5. Exit")
    try:
        i=int(input("Enter your choice:"))
        if i==1:
            AddProj()
        elif i==2:
            DispProj()
        elif i==3:
            OpenProj()
        elif i==4:
            Delete()
        elif i==5:
            break#exit
        else:
            print("Invalid Input")
    except ValueError:
        print("Invalid Input. Please enter a valid integer.")
    with open("storage","wb") as f:
        pickle.dump(proj_list,f)
