#testing splitting function()

"""
Speeding Python Script.

This script determines whether a car is speeding in the given traffic data.
"""

from datetime import datetime #importing date and time module
DIST_1 = 133 # Distance between Camera 1 and Camera 2
DIST_2 = 57.5 # Distance between Camera 2 and Camera 3
SPEED_LIMIT = 110 # Speed limit between all cameras
TIME_FMT = "%H:%M:%S" # Format of times involved within the Script


def main():
    ReadFromFile() # Calls ReadFromFile function
    traffic_list, number_of_logs = ReadFromFile() # receiving tuple to share variables
    collectingNbPlates(traffic_list, number_of_logs) # calls my collectingNbPlates functions
    uniqueNbPlates = collectingNbPlates(traffic_list, number_of_logs) # allows filled number_plates list to be passed as uniqueNbPlates
    checkIfSpeeding(uniqueNbPlates, number_of_logs, traffic_list) # Calls my checkIfSpeeding function

def ReadFromFile():
        try:
            traffic = open("input.txt", "r") # import the data file
        except Exception as e:
            print("Failed to find input.txt")
            exit(1)

        traffic_list = traffic.readlines() # Creates a new list called traffic_list which comprises of the file traffic specified above
        number_of_logs = traffic_list[0].strip('\n') # This strips the text file of the "\n" which is the enter key to create a new line
        return traffic_list, number_of_logs # Return paramaters using a tuple



def collectingNbPlates(traffic_list, number_of_logs): # collecting number plates
    number_plates = [] # Creating an empty list called number_plates
    for log_num in range(1, int(number_of_logs)+1):
        log = traffic_list[log_num].strip('\n')
        log_components = log.split() # SPlit separates log into a list for each line, with an index of 0,1,2 and so on
        if not log_components[2] in number_plates: # If the number plate found, isn't the list number_plates then add it
            number_plates.append(log_components[2])
    return number_plates 


def checkIfSpeeding(uniqueNbPlates, number_of_logs, traffic_list):
    speeding = [] # Creating an empty list for speeding cars
    for plate in uniqueNbPlates:
        highway_times = {}  # Creating an empty dictionary
        for log_num in range(1, int(number_of_logs)+1):
            log = traffic_list[log_num].strip('\n') # \n = new line which is removed with .strip
            log_components = log.split() # Have to split log again due to scope of variables
            if plate == log_components[2]:
                highway_times.update({log_components[1]: log_components[0]})
        if '1' in highway_times and '2' in highway_times: # run this if the numberplate passes through checkpoint 1 and 2
            time1obj = datetime.strptime(highway_times['1'], TIME_FMT) # Gets the time that the car passes through checkpoint 1 using key 1 of dictionary
            time2obj = datetime.strptime(highway_times['2'], TIME_FMT) # Gets the time that the car passes through checkpoint 2 using key 2 of dictionary
            diffobj = time2obj - time1obj # Minus the later time from the earlier time to get difference or time taken to travel between them
            diff_hours = float(diffobj.seconds)/float(3600)
            avg_speed = DIST_1/diff_hours # calculates average speed of number plate between checkpoints 1 & 2
            avg_speed = round(avg_speed, 1) # Rounds the result of avg_speed to 1DP
            if avg_speed > SPEED_LIMIT:
                speeding_str = highway_times['2'] + " 2 " + plate + " " + str(avg_speed) # Create a string with appropriate information if car is speeding
                speeding.append(speeding_str) # add the above string to a list of speeding cars
        if '2' in highway_times and '3' in highway_times: # Run this if numberplate passes through checkpoint 2 and 3
            time1obj = datetime.strptime(highway_times['2'], TIME_FMT)
            time2obj = datetime.strptime(highway_times['3'], TIME_FMT)
            diffobj = time2obj - time1obj
            diff_hours = float(diffobj.seconds)/float(3600)
            avg_speed = DIST_2/diff_hours
            avg_speed = round(avg_speed, 1)
            if avg_speed > SPEED_LIMIT:
                speeding_str = highway_times['3'] + " 3 " + plate + " " + str(avg_speed) # Creates the required output string
                speeding.append(speeding_str) # Adds the created string to the speeding list

    for item in speeding:
        print(item)

if __name__ == '__main__':
    main()
