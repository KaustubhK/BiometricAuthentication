#The frame class, consists of multiple fingers and frame attributes
import math

class Frame:
  def __init__(self):
    self.Fingers=[]
    self.id=None
    self.numFingers=0 

  def is_still(self):
    still_count=0
    for i in range(len(self.Fingers)):
      if (abs(float(self.Fingers[i].xvel))<0.03 and abs(float(self.Fingers[i].yvel))<0.03):
        still_count=still_count+1
    if (still_count==len(self.Fingers)):
      return True
    else:
      return False

  #Note: STOP_STATE==7
  def is_stopped(self):
    for i in range(len(self.Fingers)):
      if (self.Fingers[i].state==7):
        return True
    return False
      
    #All inter-frame attributes go here
    #Suggestions:
    #        -distance between consecutive fingers
    #        
    #Might be helpful to have some 
    #mean inter-frame "features" to help with Move features
    #  -average ellipse size?
    #  -average orientation??

  #Functions to find features pertaining to a single Frame go here
  
