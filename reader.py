import csv

#INPUT: The file path
#OUTPUT: A list of lists where each list within the list is a row
#        from the original data log.

def read_log():
  file=raw_input("Enter the log file path: ")
  reader=csv.reader(open(file))
  data=[]
  
  for row in reader:
    data.append(row)
 
  return data

#TESTING PURPOSES:
#def main():
#  data=read_log()
#  for row in range(len(data)):
#    print data[row]
#
#if __name__=="__main__":
#  main()  
