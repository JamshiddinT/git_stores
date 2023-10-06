# Take Name from User
name= input("Please enter your name : -  ")
 
# Take Math marks from User
maths= input("Please enter your Maths marks : -  ")
 
# Take Science marks from User
science= input("Please enter your Science marks : -  ")
 
# Take English marks from User
english= input("Please enter your English marks : -  ")

# Take Biology marks from User
biology= input("Please enter your Biology marks : -  ")
 
percentage = (int(maths) + int(science) + int(english) + int(biology))/4
 
 
print( "User name is " + name + ", Scored " + str(percentage) +"% in exams" )

