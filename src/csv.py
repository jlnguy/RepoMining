import csv
import numpy as np

#things to do

#either have the provider have the names for data as "DATE" and "DATA"
#or have python know that if its a string then skip it, tried but then read all
#numbers as strings

#the test file being used has dates with no data, where they put a period

#maybe if there's also blank space just skip it
def array_return_values(info):
    arrayinfo = np.asanyarray(info)
    return arrayinfo

def array_return_dates(dates):
    arraydates = np.asanyarray(dates)
    return arraydates

def read_file():
    np.set_printoptions(threshold=np.inf)
    with open('test.csv') as csvfile: #for now just reading it from my computer
        readCSV = csv.reader(csvfile, delimiter = ',') 
        
        dates = []
        info = []
        
        for row in readCSV:
            time = row[0]
            data = row[1]
    
            if time == "." or data == ".":   #where there's a date with no data put ' . '
                continue
            
            elif time == "DATE" and data == "DATA": #assuming first row has date and date strings, check above
                continue
                
            elif time == " " or data == " ": #testing for blanks
                continue
                
            else:                           #only add them in here
                dates.append(time)
                info.append(data)
                
        dates = list(map(float,dates))      #change all strings into floats 
        info = list(map(float,info))
       
 #test   arraydates = array_return_values(info)
 #test   print(arraydates)


        
        
        
        

   
  


            
            
    

            
  
            
        
    
