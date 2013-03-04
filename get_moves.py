import csv
from Finger import *
from Frame import *
from Move import *

#INPUT: Data which is obtained by the reader (SEE reader.py)
#OUTPUT: A list of all the moves, characterized by a series of frames
#        where each frame consists of at least one finger.
#        FUTURE WORK: Process the frame/finger features here.
#                     Process featurse across the user session


#DESCRIPTION:
#Time to segment into movements, at this point we must define
#what characterizes a movement.

#Starting from the beginning of the log file, we can start 
#putting together lines of data that are part of the same frame, each
#line corresponds to a finger, once we have a full frame we can add them
#to a move.

#If we get a stopped state, we know a move has ended, begin putting
#together the next move or if the velocity dwindles to near zero then 
#we can say that a single movement has ended and the user has paused 
#until another movement will begin.

#To help with the above checks, the Frame obj has is_still() and is_stopped()
#functions to check for these cases.


def move_list(data):
  move_list=[]
  curr_move=Move()
  curr_frame=Frame()

  last_frameid=None;

  for row in range(0, len(data)):
    if (data[row]):
      #Each row represents a finger in a frame
      curr_finger=Finger(data[row])
      #Handle the first entry
      if (row==0):
        curr_frame.id=curr_finger.frame
        curr_frame.Fingers.append(curr_finger)
        curr_frame.numFingers+=1
      else:
        #A new frame has begun
        if (curr_frame.id!=curr_finger.frame):
          #Check if the old frame was still or stopped (i.e. fingers lifted off)
          #and if so, end the last move and add it to the list of moves.
          if(curr_frame.is_still()) or (curr_frame.is_stopped()):
          #We don't care about collecting still-frame data so just disregard it
          #but end the move accordingly.
             
            #We know the current move has ended so added it to the list of moves
            #but only if there are frames in it, this is to mitigate the fact that
            #WHENEVER there is a still frame a new Move obj is created, but
            #we don't care about these.
            if (curr_move.Framelist):
              curr_move.endAngle=curr_frame.Fingers[0].angle #Only looks at one finger
              curr_move.endXVel=curr_frame.Fingers[0].xvel   #Only looks at one finger
              move_list.append(curr_move)
            curr_move=Move()
          #The last frame was neither still nor stopped, but we need to add it
          #to the current move.
          else:
            if (not curr_move.Framelist):
              curr_move.startAngle=curr_frame.Fingers[0].angle #Not actually accurate e.g. it only looks at one finger
              curr_move.startXVel=curr_frame.Fingers[0].xvel   #Not accurate, see above.
            curr_move.Framelist.append(curr_frame)
            if (curr_frame.numFingers > curr_move.maxFingers):
              curr_move.maxFingers=curr_frame.numFingers
            if (curr_frame.numFingers < curr_move.minFingers):
              curr_move.minFingers=curr_frame.numFingers             
          #Update the current frame
          curr_frame=Frame()
          curr_frame.id=curr_finger.frame
          curr_frame.Fingers.append(curr_finger)
          curr_frame.numFingers+=1
       #A new frame has not begun but there are more fingers to add to it. 
        else:          
          curr_frame.Fingers.append(curr_finger)
          curr_frame.numFingers+=1
  if (curr_move.Framelist):
    curr_move.endAngle=curr_frame.Fingers[0].angle #Only looks at one finger
    curr_move.endXVel=curr_frame.Fingers[0].xvel   #Only looks at one finger
    move_list.append(curr_move)        
  return move_list       

