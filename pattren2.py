"""
A    
BB   
CCC  
DDDD 
EEEEE
"""
a=65 
for i in range(1,6):
       
      for j in range(1,6):
          
          if (j<=i ):
             print(chr(a),end='')
            
          else:
             print(" ",end='')
      a+=1
      print()
