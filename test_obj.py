#This file/class is just me messing around with python
#to check different things, disregard it

class test_class:
  def __init__(self):
     data=[]
  data=[]

class test_container: 
  def __init__(self):
     objlist=[]
  objlist=[]

  def change_item(test_container):
    test_container.objlist[0].data[0]+="ha"
    return test_container

def main():
  moo=test_class()
  moo.data.append("hi")
  moo.data.append("test")
  bag=test_container()
  bag.objlist.append(moo)
  print bag.objlist[0].data[0]
  bag.objlist[0].data[0]="boo"
  print bag.objlist[0].data[0]
  print moo.data[0]
  moo.data[0]="cat"
  print bag.objlist[0].data[0]

  new=bag
  new=test_container.change_item(bag)
  print new.objlist[0].data[0]
  print bag.objlist[0].data[0]
  


if __name__=="__main__":
  main()
