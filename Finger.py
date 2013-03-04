#The finger class, it is just the raw data per instance
class Finger:
  def __init__(self, data):
    self.data=data
    self.timestamp=data[0]
    self.frame=data[1]
    self.angle=data[2]
    self.majoraxis=data[3]
    self.minoraxis=data[4]
    self.xcoord=data[5]
    self.ycoord=data[6]
    self.xvel=data[7]
    self.yvel=data[8]
    self.id=data[9]
    self.state=data[10]
    self.foo3=data[11]
    self.foo4=data[12]
    self.size=data[13]
    self.unk2=data[14]

