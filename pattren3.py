"""
A    
BC   
DEF  
GHIJ 
KLMNO"""
a=65
for i in range(1,6):
      for j in range(1,6):
          if (j<=i ):
             print(chr(a),end='')
             a+=1
          else:
             print(" ",end='')
        
      print()
