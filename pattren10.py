"""
    *     
   ***    
  *****   
 *******  
********* 
 *******  
  *****   
   ***    
    *     
"""

for i in range(1,10):
      
      for j in range(1,11):
          if (i<6 and j>=6-i and j<=4+i ):
             
             print("*",end='')
          elif (i>=6 and j>=i-4 and j<=14-i ):
             
             print("*",end='')    
                        
          else:
             print(" ",end='')
        
      print()
