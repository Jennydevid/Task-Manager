#choices-- add, view, update
#login/ signup
#if account exists actions will be perfomed otherwise exit

import csv
import sys
import pyttsx3
import cowsay

from manager import check_password

def main():
    engine = pyttsx3.init()
    msg = "Welcome to the Task Manager!!"
    cowsay.cow(msg)
    engine.say(msg)
    engine.runAndWait()
    msg1 = ("If you are new here please sign up(press s) otherwise login(press l)")
    engine.say(msg1)
    engine.runAndWait()
    ans = input(msg1+"\nEnter here: ").lower()
    if(ans == 's'):
        signUp()
        print("To access the tasks you need to login!!")
        logIn()
    elif(ans == 'l'):
        logIn()
    else:
        sys.exit("Invalid input!!")
    
    
    # login_signup()
def signUp():
    u_input = input("Username: ").lower().strip()
    filename = u_input + ".txt"
    while True:
        password = input("Create a password of atleast 6 charactres(nums, chars, special chars): ")
        if check_password(password):
            break
        else:
            continue
    with open("record.csv", "a") as record:
        writer = csv.DictWriter(record, fieldnames=["filename", "password"])
        # writer.writeheader()
        writer.writerow({"filename": filename, "password": password})


def logIn():
    u_input = input("Username: ").lower().strip()
    password = input("Enter the password: ")
    fname = u_input+".txt"
    with open('record.csv', 'r') as record:
        reader = csv.DictReader(record)
        for row in reader:
            if fname in row.values():
                if(password == row["password"]):
                    print("You have successfully loged in!!")
                    break
                else:
                    sys.exit("Incorrect password!!")
        else:
            sys.exit("Sorry username not found!!")

    managetask(fname)


def managetask(filename):
    print("-----Ways to manage your tasks-----")
    print("Type 'add' to add tasks")
    print("Type 'view' to view your tasks")
    print("Type 'update' to update your tasks")
    choice = input("What would you like to do? ").lower().strip()
    print("\n")

    
    if choice == "add":
        with open(filename, "w") as file:
            tasks = int(input("What number of tasks are you going to enter? "))
            writer = csv.DictWriter(file, fieldnames=["s.no","task", "target", "status"])
            writer.writeheader()
            for i in range(tasks):
                task = input(f"Enter task {i+1}: ")
                target = input("What time do you have to complete the task in? ")
                writer.writerow({"s.no":i+1, "task": task, "target": target, "status":"Incomplete"})

    elif choice == 'view':
        print("----- YOUR TASKS-----")
        with open(filename) as to_read:
            reader = csv.DictReader(to_read)
            for dict in reader:
                print(f"{dict['s.no']}.{dict['task']}-----{dict['target']}({dict['status']})") 
               
    elif choice == 'update':
        with open(filename) as to_read:
            reader = csv.DictReader(to_read)
            for dict in reader:
                print(f"{dict['s.no']}.{dict['task']}-----{dict['target']}({dict['status']})") 
        print("\n")
        task_num = input("Which task do you want to update?\n(enter its number): ")
        status = input("What should the updated status be: ")
        with open(filename, 'r+') as update:
            reader = csv.DictReader(update, fieldnames=["s.no","task", "target", "status"])
            for dict in reader:
                if (task_num == dict["s.no"]):
                    dict['status'] = status
                    print("The status has been updated!!")        
                    break
        
              
main()
# managetask(input("Username: ")+".txt")