import os
import sys

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
        myfile=open(f, 'r') 
        if 'NOTAFLAG' in myfile.read(): 
          #print("Alhamdulillahi alla kulli haal, Flag not found")
          myfile.close()
        else:
          #sys.stdout.write(myfile.read())  
          print("\nFlag file is ",myfile) 
          
          myfile.close()
