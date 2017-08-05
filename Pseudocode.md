<!DOCTYPE Pseudocode>

BEGIN AQUIREINFORMATION
  import textfile #this should be done first before your previous 3 lines right?
  Get distance1
  Get distance 2
  Get SPEED_LIMIT

END

BEGIN NUMBERPLATES
#Seeing that the textfile was imported in the previous subroutine, how is it accessed again here?
#Remember the scope of variables.
#What are you trying to achieve here?
  FOR every line in textfile
    separate with delimiter( ) into textfile()
    append textfile[3] to numberplates[]
END

BEGIN TIMES
  FOR every numberplate
    get times passed through each checkpoint #you are going to have to write pseudocode to get this - keep a counter
    IF number plate passes through checkpoint1 and checkpoint2
      timetaken = checkpoint2time - checkpoint1time
      averagespeed = distance1 / timetaken
        IF averagespeed > speedlimit
          add "numberplate checkpoint2 averagespeed" to speeding[]
        ENDIF
    ENDIF
    IF numberplate passes through checkpoint2 and checkpoint3
      timetaken = checkpoint3time - checkpoint2time
      averagespeed = distance2 / timetaken
        IF averagespeed > speedlimit
        add "numberplate checkpoint3 averagespeed" to speeding[]
        ENDIF
    ENDIF
END

BEGIN OUTPUT
  Print speeding[]
END
