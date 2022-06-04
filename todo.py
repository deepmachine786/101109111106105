from textwrap import wrap
import time 
import datetime as dt
import os 
from itertools import zip_longest
import asyncio 
from functools import  wraps

import pyttsx3

engine_say = pyttsx3.init()
morning_time = [i for i in range(1,13)] # for morning time 
evening_time = [i for i in range(13,25)] # for night time ..

all_time = dict(zip_longest(morning_time, evening_time))

hours =minutes=second = 0

def engine(audio):
    engine_say.say(audio)
    engine_say.runAndWait()

newdict = {} # for store the data in dictionary ...

# this is a only night wake time programming ..
def get_information_from_user():
    engine(" Please Fill Your Task Information First ")
    number_information = input(" Enter a Number to Save the Task : ")
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
            while start_task:
                local_hours , local_second = int(wrap(time.ctime(),10)[1][0:2]), int(wrap(time.ctime(),10)[1][3:5]) # get the current 
                    # local time and second ..
                print(local_hours, local_second," and ", from_hours, from_second," to ",to_hours, to_second)
                if (local_hours>from_hours) and (local_hours>=to_hours and local_second>=to_second):
                    engine(" Your Task is Completed ... Next Task is Running ..")
                    start_task = False# return 0 #execute the code when the time is Over ..
                if (local_hours== from_hours and local_second>=from_second) and (local_hours<=to_hours and local_second<=to_second):
                    await asyncio.sleep(get_total_second//2)
                    engine(" Your Have Completed Your Task in Few Minutes! Please Complete Your Task ! After Time Completing.")
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
    current_time= time.ctime() # get the currentt time ..
    copy_hours ,copy_to_hour = from_hours, to_hour # for checking if time is am or pm 
    print(f" Hours is :- {from_hours} and Second is {to_hour}")
    # now hours = 09:30 am ans second = 10:00 pm 
  
    from_second = int("".join(from_hours.strip().split(":")[1][0:2])) # from 0 to 1 
    to_second = int("".join(to_hour.strip().split(":")[1][0:2]))

    from_hours = from_hours.strip().split(":")[0]
    to_hour = to_hour.strip().split(":")[0]
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



# print the data in file and Passing in the function to Execute tha task ....
async def print_data(newdict:dict): # print the data 
    number =1 
    for key,value in newdict.items():
        engine(f" Your {number} Task of {key} is Start . Now You Start Now")
        # print(newdict) # print the data in the newdict 
        await asyncio.gather(execute_task(key,value)) # wait and exexute one by one task in the file ...
        # execute_task(key,value)
        number+=1
    engine(" Your Task Fully Completed Today ! Good Bye!")




def read_data(): # read the data from file 
    engine(" Please Check Your File. . You have Already Save your Task..")
    with open(os.getcwd()+"\\"+"plan.txt", "r+") as files:
        for i in files.readlines():
            lists = i.split(":-") # return e data in list whose is in the file ..
            newdict[lists[0]] = lists[1].replace("\n","")
    # print_data(newdict) # print the data in the command line 
    asyncio.run(print_data(newdict)) # call the function to execute the task one by one ..


def write_data(data:dict): # write the data from user and Store in the file ..
    try:
        with open(os.getcwd()+"\\"+"plan.txt", "w+") as files:
            for key,value in data.items():
                files.writelines(f"{key} :- {value} \n")
        engine(" File Writen Successfully")
    except Exception as e:
        print(" File Writing UnSucessfully ",e)
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
