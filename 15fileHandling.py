# Write Data into a File
"""file=open('/home/raj/Desktop/Rajkumar.txt', 'w') #Enter the full and correct path (use pwd in terminal)

file.write("HI I AM RAJKUMAR\n")
file.write("I AM FROM THIRUVALLUR\n")
file.write("This Is My First File\n ")
file.write("I Am Beginner In Python Programing Language\n")
file.close()

#Read Data into a File

file=open('/home/raj/Desktop/Rajkumar.txt', 'r')
#print(file.read()) # Read total contend
#print(file.read(100)) # read enter number of characters
#print(file.readline()) # Default print first line
print(file.readlines())

# append mode (a)
file=open('/home/raj/Desktop/Rajkumar.txt', 'a') # file open in append mode
file.write("My Wife Name Is Chellakutty\n") # add the date in file
file.close()


#File open in loop method
file=open('/home/raj/Desktop/Rajkumar.txt', 'r')
for i in file:
    print(i)
file.close()"""


file=open('/home/raj/Desktop/ShellScripting/practised-files/arrays.sh', 'r')
print(file.read())