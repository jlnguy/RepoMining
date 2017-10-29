import csv
import numpy as np
def read_file():    
    print("Enter input file:")
    filename = input()+'.csv'
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ",") #csv = comma separated
                
        dates = []
        info = []
        
        for row in readCSV:
            time = row[0]
            data = row[1]
    
            if time == "." or data == ".":   #where there's a date with no data put ' . '
                continue
                            
            elif time == " " or data == " ": #testing for blanks
                continue
                
            else:                           #only add them in here
                dates.append(time)
                info.append(data)
                            
        return (info, dates)


        
        
        
        

   
  


            
            
    

            
  
            
        
    
