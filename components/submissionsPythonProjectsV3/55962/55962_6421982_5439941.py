import datetime

# Define the bus schedule as a dictionary
bus_schedule = { 
    "Bobcat_Express" :{
           "R Street Village Apts.": {
           "AM":{
               "Monday": ["6:29", "7:09", "7:49", "8:44", "9:24", "10:04", "10:44"],
               "Tuesday": ["6:29", "7:09", "7:49", "8:44", "9:24", "10:04", "10:44"],
               "Wednesday": ["6:29", "7:09", "7:49", "8:44", "9:24", "10:04", "10:44"],
               "Thursday": ["6:29", "7:09", "7:49", "8:44", "9:24", "10:04", "10:44"],
               "Friday": ["6:29", "7:09", "7:49", "8:44", "9:24", "10:04", "10:44"]
           },
           "PM":{
               "Monday": ["12:09", "1:49", "3:17", "4:57", "6:22", "8:02"],
               "Tuesday": ["12:09", "1:49", "3:17", "4:57", "6:22", "8:02"],
               "Wednesday": ["12:09", "1:49", "3:17", "4:57", "6:22", "8:02"],
               "Thursday": ["12:09", "1:49", "3:17", "4:57", "6:22", "8:02"],
               "Friday": ["12:09", "1:49", "3:17", "4:57", "6:22", "8:02"]
           }
       },
       "El Redondo Dr. (Across from Jenner Dr.)": {
               "AM": {
                   "Monday": ["6:32", "7:12", "7:52", "8:47", "9:27", "10:07", "10:47"],
                   "Tuesday": ["6:32", "7:12", "7:52", "8:47", "9:27", "10:07", "10:47"],
                   "Wednesday": ["6:32", "7:12", "7:52", "8:47", "9:27", "10:07", "10:47"],
                   "Thursday": ["6:32", "7:12", "7:52", "8:47", "9:27", "10:07", "10:47"],
                   "Friday": ["6:32", "7:12", "7:52", "8:47", "9:27", "10:07", "10:47"]
               },
               "PM": {
                   "Monday": ["12:12", "1:52", "3:20", "5:00", "6:25", "8:05"],
                   "Tuesday": ["12:12", "1:52", "3:20", "5:00", "6:25", "8:05"],
                   "Wednesday": ["12:12", "1:52", "3:20", "5:00", "6:25", "8:05"],
                   "Thursday": ["12:12", "1:52", "3:20", "5:00", "6:25", "8:05"],
                   "Friday": ["12:12", "1:52", "3:20", "5:00", "6:25", "8:05"]
               }
       },
           "Compass Pointe Apts. (Bus stop on Pacific Dr. in Front)": {
               "AM": {
                   "Monday": ["6:34", "7:14", "7:54", "8:49", "9:29", "10:09", "10:49"],
                   "Tuesday": ["6:34", "7:14", "7:54", "8:49", "9:29", "10:09", "10:49"],
                   "Wednesday": ["6:34", "7:14", "7:54", "8:49", "9:29", "10:09", "10:49"],
                   "Thursday": ["6:34", "7:14", "7:54", "8:49", "9:29", "10:09", "10:49"],
                   "Friday": ["6:34", "7:14", "7:54", "8:49", "9:29", "10:09", "10:49"]
               },
               "PM": {
                   "Monday": ["12:14", "1:54", "3:22", "5:02", "6:27", "8:07"],
                   "Tuesday": ["12:14", "1:54", "3:22", "5:02", "6:27", "8:07"],
                   "Wednesday": ["12:14", "1:54", "3:22", "5:02", "6:27", "8:07"],
                   "Thursday": ["12:14", "1:54", "3:22", "5:02", "6:27", "8:07"],
                   "Friday": ["12:14", "1:54", "3:22", "5:02", "6:27", "8:07"]
               }
       },
           "Merced College The Bus Terminal": {
               "AM": {
                   "Monday": ["6:39", "7:19", "7:59", "8:54", "9:34", "10:14", "10:54"],
                   "Tuesday": ["6:39", "7:19", "7:59", "8:54", "9:34", "10:14", "10:54"],
                   "Wednesday": ["6:39", "7:19", "7:59", "8:54", "9:34", "10:14", "10:54"],
                   "Thursday": ["6:39", "7:19", "7:59", "8:54", "9:34", "10:14", "10:54"],
                   "Friday": ["6:39", "7:19", "7:59", "8:54", "9:34", "10:14", "10:54"]
               },
               "PM": {
                   "Monday": ["12:19", "1:59", "3:27", "5:07", "6:32", "8:12"],
                   "Tuesday": ["12:19", "1:59", "3:27", "5:07", "6:32", "8:12"],
                   "Wednesday": ["12:19", "1:59", "3:27", "5:07", "6:32", "8:12"],
                   "Thursday": ["12:19", "1:59", "3:27", "5:07", "6:32", "8:12"],
                   "Friday": ["12:19", "1:59", "3:27", "5:07", "6:32", "8:12"]
               }
           },
           "M St. At Bellevue RD (Bellevue Ranch)": {
               "AM": {
                   "Monday": ["6:44", "7:24", "8:04", "8:59", "9:39", "10:19", "11:00"],
                   "Tuesday": ["6:44", "7:24", "8:04", "8:59", "9:39", "10:19", "11:00"],
                   "Wednesday": ["6:44", "7:24", "8:04", "8:59", "9:39", "10:19", "11:00"],
                   "Thursday": ["6:44", "7:24", "8:04", "8:59", "9:39", "10:19", "11:00"],
                   "Friday": ["6:44", "7:24", "8:04", "8:59", "9:39", "10:19", "11:00"]
               },
               "PM": {
                   "Monday": ["12:25", "2:05", "3:33", "5:13", "6:38", "8:18"],
                   "Tuesday": ["12:25", "2:05", "3:33", "5:13", "6:38", "8:18"],
                   "Wednesday": ["12:25", "2:05", "3:33", "5:13", "6:38", "8:18"],
                   "Thursday": ["12:25", "2:05", "3:33", "5:13", "6:38", "8:18"],
                   "Friday": ["12:25", "2:05", "3:33", "5:13", "6:38", "8:18"]
               }
           },
           "University Transit Center (UTC)": {
               "AM": {
                   "Monday": ["6:55", "7:35", "8:30", "9:10", "9:50", "10:30", "11:11"],
                   "Tuesday": ["6:55", "7:35", "8:30", "9:10", "9:50", "10:30", "11:11"],
                   "Wednesday": ["6:55", "7:35", "8:30", "9:10", "9:50", "10:30", "11:11"],
                   "Thursday": ["6:55", "7:35", "8:30", "9:10", "9:50", "10:30", "11:11"],
                   "Friday": ["6:55", "7:35", "8:30", "9:10", "9:50", "10:30", "11:11"]
               },
               "PM": {
                   "Monday": ["12:51", "2:16", "3:59", "5:24", "7:04", "8:29"],
                   "Tuesday": ["12:51", "2:16", "3:59", "5:24", "7:04", "8:29"],
                   "Wednesday": ["12:51", "2:16", "3:59", "5:24", "7:04", "8:29"],
                   "Thursday": ["12:51", "2:16", "3:59", "5:24", "7:04", "8:29"],
                   "Friday": ["12:51", "2:16", "3:59", "5:24", "7:04", "8:29"]
               }
           },
           "Promenade Center": {
               "PM": {
                   "Monday": ["11:20", "1:00", "2:25", "4:08", "5:33", "7:13"],
                   "Tuesday": ["11:20", "1:00", "2:25", "4:08", "5:33", "7:13"],
                   "Wednesday": ["11:20", "1:00", "2:25", "4:08", "5:33", "7:13"],
                   "Thursday": ["11:20", "1:00", "2:25", "4:08", "5:33", "7:13"],
                   "Friday": ["11:20", "1:00", "2:25", "4:08", "5:33", "7:13"]
               }
           },
           "Merced Mall Target": {
               "PM": {
                   "Monday": ["11:29", "1:09", "2:37", "4:17", "5:42", "7:22"],
                   "Tuesday": ["11:29", "1:09", "2:37", "4:17", "5:42", "7:22"],
                   "Wednesday": ["11:29", "1:09", "2:37", "4:17", "5:42", "7:22"],
                   "Thursday": ["11:29", "1:09", "2:37", "4:17", "5:42", "7:22"],
                   "Friday": ["11:29", "1:09", "2:37", "4:17", "5:42", "7:22"]
               }
           },
           "Walmart on Loughborough Dr.": {
               "PM": {
                   "Monday": ["11:38", "1:18", "2:46", "4:26", "5:51", "7:31"],
                   "Tuesday": ["11:38", "1:18", "2:46", "4:26", "5:51", "7:31"],
                   "Wednesday": ["11:38", "1:18", "2:46", "4:26", "5:51", "7:31"],
                   "Thursday": ["11:38", "1:18", "2:46", "4:26", "5:51", "7:31"],
                   "Friday": ["11:38", "1:18", "2:46", "4:26", "5:51", "7:31"]
               }
           },
           "Amtrak Station": {
               "PM": {
                   "Monday": ["11:50", "1:30", "2:58", "4:38", "6:03", "7:43"],
                   "Tuesday": ["11:50", "1:30", "2:58", "4:38", "6:03", "7:43"],
                   "Wednesday": ["11:50", "1:30", "2:58", "4:38", "6:03", "7:43"],
                   "Thursday": ["11:50", "1:30", "2:58", "4:38", "6:03", "7:43"],
                   "Friday": ["11:50", "1:30", "2:58", "4:38", "6:03", "7:43"]
               }
           },
           "K St. Between 18th & 19th St.(The Bus stop)": {
               "PM": {
                   "Monday": ["11:52", "1:32", "3:00", "4:40", "6:05", "7:45"],
                   "Tuesday": ["11:52", "1:32", "3:00", "4:40", "6:05", "7:45"],
                   "Wednesday": ["11:52", "1:32", "3:00", "4:40", "6:05", "7:45"],
                   "Thursday": ["11:52", "1:32", "3:00", "4:40", "6:05", "7:45"],
                   "Friday": ["11:52", "1:32", "3:00", "4:40", "6:05", "7:45"]
               }
           },
           "Merced Transpo (REQ)": {
               "AM": {
                   "Monday": ["REQ", "REQ", "REQ", "REQ", "REQ", "REQ"],
                   "Tuesday": ["REQ", "REQ", "REQ", "REQ", "REQ", "REQ"],
                   "Wednesday": ["REQ", "REQ", "REQ", "REQ", "REQ", "REQ"],
                   "Thursday": ["REQ", "REQ", "REQ", "REQ", "REQ", "REQ"],
                   "Friday": ["REQ", "REQ", "REQ", "REQ", "REQ", "REQ"]
               }
           },
           "Rite Aid/Walgreens on G St.": {
               "PM": {
                   "Monday": ["12:01", "1:41", "3:09", "4:49", "6:14", "7:54"],
                   "Tuesday": ["12:01", "1:41", "3:09", "4:49", "6:14", "7:54"],
                   "Wednesday": ["12:01", "1:41", "3:09", "4:49", "6:14", "7:54"],
                   "Thursday": ["12:01", "1:41", "3:09", "4:49", "6:14", "7:54"],
                   "Friday": ["12:01", "1:41", "3:09", "4:49", "6:14", "7:54"]
               }
           },
           "El Portal Plaza & G Street": {
               "PM": {
                   "Monday": ["12:03", "1:43", "3:11", "4:51", "6:16", "7:56"],
                   "Tuesday": ["12:03", "1:43", "3:11", "4:51", "6:16", "7:56"],
                   "Wednesday": ["12:03", "1:43", "3:11", "4:51", "6:16", "7:56"],
                   "Thursday": ["12:03", "1:43", "3:11", "4:51", "6:16", "7:56"],
                   "Friday": ["12:03", "1:43", "3:11", "4:51", "6:16", "7:56"]
               }
           },
           "R Street Village Apts 2": {
               "PM": {
                   "Monday": ["12:09", "1:49", "3:17", "4:57", "6:22", "8:02"],
                   "Tuesday": ["12:09", "1:49", "3:17", "4:57", "6:22", "8:02"],
                   "Wednesday": ["12:09", "1:49", "3:17", "4:57", "6:22", "8:02"],
                   "Thursday": ["12:09", "1:49", "3:17", "4:57", "6:22", "8:02"],
                   "Friday": ["12:09", "1:49", "3:17", "4:57", "6:22", "8:02"]
               }
           }
       }
   }
def find_next_bus(schedule, day, time, period, start_stop):
    # Get the current time
    current_time = datetime.datetime.now().time()
    current_hour = current_time.hour
    current_minute = current_time.minute

    # Handle the case when the time is in PM
    if period == "PM" and current_hour < 12:
        current_hour += 12

    # Check for the next available bus
    if day in schedule and time in schedule[day][period]:
        for bus_time in schedule[day][period][time]:
            bus_hour, bus_minute = map(int, bus_time.split(':'))
            if (bus_hour > current_hour) or (bus_hour == current_hour and bus_minute >= current_minute):
                return time, bus_time
    return None, None

#Potential error on the input Start_stop
def main():
    print("Welcome to the CatTracks Shuttle System: BobCat Express Route!")

    # Get a list of available bus stops
    available_stops = list(bus_schedule["Bobcat_Express"].keys())

    print("Available bus stops:")
    for i, stop in enumerate(available_stops, 1):
        print(f"{i}. {stop}")

    while True:
        day = input("Enter the day of the week (e.g., Monday): ")
        time = input("Enter the time (e.g., 8:30): ")
        period = input("AM or PM?")

        # Prompt the user to select a bus stop
        stop_choice = input("Select a bus stop by entering its number: ")

        if stop_choice.isdigit():
            stop_choice = int(stop_choice)
            if 1 <= stop_choice <= len(available_stops):
                start_stop = available_stops[stop_choice - 1]
            else:
                print("Invalid bus stop selection.")
                continue
        else:
            print("Invalid input for bus stop selection.")
            continue

        next_time, next_bus = find_next_bus(bus_schedule["Bobcat_Express"], day, time, period, start_stop)

        if next_time and next_bus:
            print(f"The next bus from {start_stop} at {next_time} is at {next_bus}.")
        else:
            print("No bus found for the given inputs.")

        another_search = input("Do you want to search for another bus? (yes/no): ")
        if another_search.lower() != "yes":
            break

if __name__ == "__main__":
    main()
#End