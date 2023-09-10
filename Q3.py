s1=int(input("Enter side1:")) 
 s2=int(input("Enter side2:")) 
 s3=int(input("Enter side3:")) 
 if (s1<0 or s2<0 or s3<0): 
     print("Invalid sides") 
 if (s1+s2>s3 or s2+s3>s1 or s1+s3>s2) and (s1>0 and s2>0 and s3>0): 
     print("The three sides form a triangle:") 
 else: 
     print("Error")
