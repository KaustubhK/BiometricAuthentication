#The Move class, a move is a stroke

class Move:
  def __init__(self):
    self.Framelist=[]
    self.minFingers=300 #min number of fingers in this move
    self.maxFingers=0
    self.startAngle=None
    self.endAngle=None
#    self.meanXVel=0
#    self.meanYVel=0
    self.startXVel=0
    self.endXVel=0	
#    self.startfoo3=None
#    self.endfoo3=None
#    self.distance=0


def distance(p0, p1):
  return math.sqrt((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2) 

#def find_length(move):

    
