import sys
from textwrap import wrap
import time 
import datetime as dt
import os 
from itertools import zip_longest
import asyncio 
from functools import  wraps
import subprocess # to call th eprocess ...

import pyttsx3

engine_say = pyttsx3.init()
morning_time = [i for i in range(1,13)] # for morning time 
evening_time = [i for i in range(13,25)] # for night time ..

all_time = dict(zip_longest(morning_time, evening_time))
all_time[12] = 00 

hours =minutes=second = 0

def engine(audio):
    engine_say.say(audio)
    engine_say.runAndWait()

newdict = {} # for store the data in dictionary ...

# this is a only night wake time programming ..
def get_information_from_user():
    engine(" Please Fill Your Task Information First ")
    number_information = input(" Enter a Number to Perform The Task :-  ")
    task_lists = {}
    for i in range(int(number_information)):
        task = input(f"Enter Your {i+1} Task:- ")
        task_time = input(" Enter Your Time start From( Eg: 9:00 pm):-  ")
        task_end_time = input("Enter Your End Time (Eg 10:00 pm):- ")
        task_lists[task] = task_time.lower()+" to "+task_end_time.lower()
    return task_lists # return the task list and save in the file ..

def execute_task_time():pass

def get_time_execute(function):
    @wraps(function)
    async def warpper_function(*args):
        try:
            get_total_second,from_hours, to_hours, from_second, to_second = function(*args)
            ''' from hour is starting hour and from_second is the starting second and to_hour 
            ending the Task ..'''
            start_task = True # This is for Looping ..
            while start_task == True:
                local_hours , local_second = int(wrap(time.ctime(),10)[1][0:2]), int(wrap(time.ctime(),10)[1][3:5]) # get the current 
                    # local time and second ..
                print(local_hours, local_second," and ", from_hours, from_second," to ",to_hours, to_second, time.ctime())
                if (local_hours>=from_hours) and (local_hours>=to_hours and local_second>=to_second):
                    engine(" Your Task is Completed ... Next Task is Running ..")
                    start_task = False# return 0 #execute the code when the time is Over ..
                if (local_hours== from_hours and local_second>=from_second) and (local_hours<=to_hours and local_second<=to_second):
                    engine(" Your Have Completed Your Task in Few Minutes! Please Complete Your Task ! After Time Completing.")
                    await asyncio.sleep(get_total_second//(from_second+to_second)-10)
                else: 
                    await asyncio.sleep(3600*(from_hours-local_hours))
        except Exception as e: 
            print(" Some Error are Occured :- ", e)
            exit(0)


    return warpper_function


@get_time_execute
def execute_task(key:str,value:str) -> tuple:

    # key is task and value is the time to execute the task 
    from_hours, to_hour = value.split("to") # example hours = 9pm ans second = 10 pm 
    # current_time= time.ctime() # get the currentt time ..
    copy_hours ,copy_to_hour = from_hours, to_hour # for checking if time is am or pm 
    print(f" Hours is :- {from_hours} and Second is {to_hour}")
    # now hours = 09:30 am ans second = 10:00 pm 
  
    from_second = int("".join(from_hours.strip().split(":")[1][0:2])) # from 0 to 1 
    to_second = int("".join(to_hour.strip().split(":")[1][0:2]))

    from_hours = from_hours.strip().split(":")[0]
    to_hour = to_hour.strip().split(":")[0]
    if ("am" in copy_hours and int(from_hours)==12 ):
        from_hours = all_time.get(int(from_hours), from_hours)
    elif ("pm" in copy_to_hour and int(to_hour)==12):
        to_hour = 12
    elif ("am" in copy_hours and "pm" in copy_to_hour ):
        from_hours = from_hours
        to_hour = all_time.get(int(to_hour), to_hour)    
        ...
    elif ("pm" in copy_hours and "am" in copy_to_hour):
        from_hours = all_time.get(int(from_hours), from_hours)
        to_hour = to_hour
    else:
        if "pm" in copy_hours and "pm" in copy_to_hour:
            from_hours = all_time.get(int(from_hours), from_hours) # if the time in th ekey thenrretunr the value 
            to_hour = all_time.get(int(to_hour), to_hour) # if the time in key then return the value ...

    print(" second is ",from_second, " and other second is :- ", to_second)
    print(" first hour is :- ",from_hours," and second hour is :- ",to_hour)
    total_hours = 3600*(int(to_hour) - int(from_hours)) # get the total second to Execute the task 
    total_second =60*(from_second+to_second)
    total_time_second = total_hours+total_second
    print(" Total second is :- ", total_time_second)
    return total_time_second,int(from_hours),int(to_hour),from_second, to_second


def get_routine_time_mor(function): 
    @wraps(function)
    async def wrapper_function(*args, **kwargs):
        new_dict = function(*args, **kwargs)
        number = 1
        for key,value in new_dict.items():
            
            engine(f" Your {number} Task of {key} is Start . Now You Start Now")
            print(f" Your {number} Task of {key} is Start. Now You Start Now ")
            # print(newdict) # print the data in the newdict
            await asyncio.gather(execute_task(key,value)) # wait and exexute one by one task in the file ...
            # execute_task(key,value)
            number+=1
        engine(" Your Task Fully Completed Today ! Good Bye!")
        engine(" If You Want ! To Update  or Changed Time ! Table In File! Then Exit This  Command  And Again Run This Script ! Then Your ! Running Perfectly.BY ")
    return wrapper_function

@get_routine_time_mor
def check_Day_mor(newdict:dict) -> dict: 
    newdict_org = {}

    for key,value in newdict.items():
        if "am" in value and "pm" in value :
            newdict_org[key] = newdict_org.get(key, value) # if the key is found then retun else return value ..
        elif "am" in value :
             newdict_org[key] = newdict_org.get(key, value) # if the key is found then retun else return value ..
        else: continue
    return newdict_org

def get_routine_time_eve(function):
    @wraps(function) # not the change of the doc of thies functin ..
    async def wrapper_function(*args, **kwargs):
        new_dict = function(*args, **kwargs)
        number =1 
        for key,value in new_dict.items():
            
            engine(f" Your {number} Task of {key} is Start . Now You Start Now")
            print(f" Your {number} Task of {key} is Start. Now You Start Now ")
            # print(newdict) # print the data in the newdict
            await asyncio.gather(execute_task(key,value)) # wait and exexute one by one task in the file ...
            # execute_task(key,value)
            number+=1
        engine(" Your Task Fully Completed Today ! Good Bye!")
        engine(" If You Want ! To Update  or Changed Time ! Table In File! Then Exit This  Command  And Again Run This Script ! Then Your ! Running Perfectly.BY ")
    return wrapper_function



@get_routine_time_eve
def check_Day_eve(newdict:dict) -> dict:
    newdict_eve = {}
    for key ,value in newdict.items():
        if "pm" in value and "am" in value :
            newdict_eve[key] = newdict_eve.get(key, value)
        elif "pm" in value:
            newdict_eve[key] = newdict_eve.get(key, value)
        else: continue
    return newdict_eve

    


# print the data in file and Passing in the function to Execute tha task ....
def print_data(newdict:dict): # print the data 
    # number =1 
    current_time_now= int(wrap(time.ctime(),10)[1][0:2])
    if (current_time_now<=12):
        engine(" Good Morning....")
        asyncio.run(check_Day_mor(newdict))
        exit(0)

    else: 
        engine(" Good Evening Sir.")
        asyncio.run(check_Day_eve(newdict))
        exit(0)

# def read_setup_file() -> list:
#     with open(os.getcwd()+"\\"+"todo.py", "r+") as file_read:
#         return file_read.readlines()
        

# def write_setup_file():
#     path = "C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
#     with open(path+"Running_To_Do.py", "w+") as files:
#            for i in read_setup_file():
#                files.write(i)
#     # and store the file in the ..
#     with open(os.getcwd()+"\\"+"plan.txt", "r+") as file_read:
#         with open(path+"plan.txt", "w+") as files:
#             files.write(file_read.readline()+"\n")
    
    # with open(path+"message.bat", "w+") as files:
    #     files.write("""
    #     @echo off
    #     msg * You have Complete Full Task Today . Good Bye!
    #     exit    
    #     """)




def read_data(): # read the data from file
    try:
        engine(" Please Check Your File. Your Problem start from line number 135 Please Check and Run Ok . You have Already Save your Task..")
        with open(os.getcwd()+"\\"+"plan.txt", "r+") as files:
                for i in files.readlines():
                    if i.strip() is None or i.strip() =="":
                        engine(" Space Found in Your File , Please Remove ..")
                        continue
                    else:
                        lists =i.split(":-")  # return e data in list whose is in the file ..
                        newdict[lists[0].strip()] = lists[1].strip() 
        print(newdict.items())
        print_data(newdict)
        # asyncio.run(print_data(newdict)) # call the function to execute the task one by one ..        # print_data(newdict) # print the data in the command line
    except Exception as e:
        engine(" Please Remove Space After The End Line of Task ! Please Then Run Again Scipt! OK Bye.")
        print(e)   
        exit(0)  
    


def write_data(data:dict): # write the data from user and Store in the file ..
    try:
        with open(os.getcwd()+"\\"+"plan.txt", "w+") as files:
            for key,value in data.items():
                files.writelines(f"{key.strip()} :- {value.strip()} \n")
        engine(" File Writen Successfully! . Now You Run This Script Again Then Your Task is Start .! Ok By")   
        # write_setup_file()
    except Exception as e:
        print(" File Writing UnSucessfully ",e)
         # write the file in statup window ...
        exit(0)


# Ececute the task by the file each line ....



# this is a Main Function for Executinf the Code ..

if __name__=="__main__":
    if os.path.exists(os.getcwd()+"\\"+"plan.txt"):
        read_data()
    else:
        write_data(get_information_from_user())
    current_time = time.ctime()
    (f" current time is {current_time}")
    print(current_time)
