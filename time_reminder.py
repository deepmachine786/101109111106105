import time 

def calculate_second(launch_time:str, travel_time:str):
    launch_time_lists = launch_time.split(" ")
    travel_time_lists =travel_time.split(" ")

    calculate_hours = int(launch_time_lists[0])+int(travel_time_lists[0])
    calculate_second = int(launch_time_lists[1])+int(travel_time_lists[1])
    total_second = 3600*(calculate_hours)+(60*calculate_second) # get the total second 
    # print(" Total Second to Travel and Attck : -", total_second)
    return total_second

if __name__ == "__main__":

    launch_time = input()
    travel_time = input()

    total = calculate_second(launch_time,travel_time)
    
    get_time = time.strftime("%H:%M:%S",time.gmtime(total))
    print(f"{get_time[0:2]} {get_time[3:5]}")

