<!DOCTYPE Pseudocode>

BEGIN MAINPROGRAM
  traffic_list = ReadFromFile()
  number_of_logs = ReadFromFile()
  DIST_1 = 133 # Distance between Camera 1 and Camera 2
  DIST_2 = 57.5 # Distance between Camera 2 and Camera 3
  SPEED_LIMIT = 110 # Speed limit between all cameras
  collectingNbPlates(traffic_list, number_of_logs)
  uniqueNbPlates = collectingNbPlates(traffic_list, number_of_logs)
  checkIfSpeeding(uniqueNbPlates, number_of_logs, traffic_list)
END

BEGIN ReadFromFile
  Open input.txt for input
  read total from input.txt #first line tells us how many lines are to follow
  return traffic_list, number_of_logs
END

BEGIN collectingNbPlates(traffic_list, number_of_logs)
  DIM number_plates() # will store all number plates
  DIM uniqueNbPlates = removeDuplicates(number_plates) # will create array of unique numberplates
  return number_plates
END

BEGIN checkIfSpeeding(uniqueNbPlates, number_of_logs, traffic_list)
  counter = 1 #initiate counter
  DIM speeding() # array for speeding cars
  WHILE counter <= number_of_logs ‘looping through the file
    DIM highway_times() #storing times of each numberplate at checkpoints
		find all checkpoints each plate passed through
    IF plate passed through checkpoint 1 and 2
      calculate difference in time
      calculate average speed with distance/time
      IF average speed > SPEED_LIMIT
          add plate to speeding()
      ENDIF  
    ENDIF
    find all checkpoints each plate passed through
    IF plate passed through checkpoint 2 and 3
      calculate difference in time
      calculate average speed with distance/time
      IF average speed > SPEED_LIMIT
        add plate to speeding()
      ENDIF
    ENDIF
  ENDWHILE
  close input.txt
  print speeding
END
