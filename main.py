import reader
import get_moves
import csv

#The main function
#Currently used for testing what works/doesn't
#as well as to read input, get output, create the csv file

FEATURES=['minFingers', 'maxFingers', 'startAngle', 'endAngle', 'startxvel', 'endxvel']

def main():
  data=reader.read_log()
  moves=get_moves.move_list(data)
 # print moves
 # for i in range(len(moves)):
 #   print str(moves[i].maxFingers)+", "+str(moves[i].minFingers) 

 #Create csv file with move features
  csvfile=open('Moves.csv', 'wb')
  writer=csv.writer(csvfile, delimiter=',')
  writer.writerow(FEATURES)
  for i in range(len(moves)):
    writer.writerow([moves[i].minFingers, moves[i].maxFingers, moves[i].startAngle, moves[i].endAngle, moves[i].startXVel, moves[i].endXVel])      

if __name__=="__main__":
  main()
