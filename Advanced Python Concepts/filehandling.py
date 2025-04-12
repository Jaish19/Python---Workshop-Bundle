--------------------------------
#KEY TERMS TO LEARN IN FILE HANDLING:
# 1. read, write
# 2. replace a string one with another
# 3. replace a string in line
# 4. os.path.exist
# 5. file object attributes

# FILE HANLING:
# file object = open(file_name [, access_mode][, buffering])

fw=open('sample.txt','w')
fw.write('Write a new text\n')
fw.write('Excellent job to go ahead!\n')
fw.close()

fr=open('sample.txt','r')
view=fr.read() # To read entire contents from the file
viewOne = fr.readline()
viewThree = fr.readlines()
print(view)
fr.close()


# FILE OBJECT ATTRIBUTES

fo = open("foo.txt", "w")
fo.write('hi jai ganesh\n')
fo.write("welcome\n")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace



# PYTHON FILE HANDLING: PERFORM WRITE OPERATION.


with open ('jai.txt','w') as f:
    f.write('New statements are entering\n')
    f.write('I think it will overwrite on it')
    f.close()
    
with open('jai.txt','r') as f:
    contents=f.readlines() # readlines to read all the lines where if i mention readline for reading the single line
    contents_two=f.readline()
    contents_three=f.xreadlines()  # type of xreadlines is file. Need to use x.next() to read the data.
for i in contents:
    print(i)

# PYTHON FILE HANDLING: PERFORM READ OPERATION.


with open ('jai.txt','w') as f:
    f.write('New statements are entering\n')
    f.write('I think it will overwrite on it')
    f.close()
    
with open('jai.txt','r') as f:
    print(f.read(10))
    print(f.read(4))


 # PYTHON FILE HANDLING: FILE READ POSITIONS

 with open ('jai.txt','w') as f:
    f.write('New statements are entering\n')
    f.write('I think it will overwrite on it')
    line_to_add=["Hella Guys","Wat's up there?\n"]
    f.writelines(line_to_add)
    f.close()
    
with open('jai.txt','r+') as f:
    print("Reading the string:",f.read(10))
    position=f.tell()
    print("current position of offset:",position)
    
    
    position=f.seek(2,1)
#     print("after seek position:",position)
    print("Again read the string after seek it",f.read(10))


# PYTHON FILE HANDLING: RENAMING AND DELETING FILES IN PYTHON
import os
os.rename('from.txt','jai.txt')

# DELETING FILES

import os
os.remove('jai.txt')

# MAIN EXAMPLE:

# Open a file
import fileinput
import time
with open('input1.txt', 'r+') as info:
    print ("Name of the file: ", info.name)
    print ("Closed or not : ", info.closed)
    print ("Opening mode : ", info.mode)
    print ("Softspace flag : ", info.softspace)

    start= time.time()

    line = info.readline()
    line2 = info.readlines()
    line3 = info.xreadlines()
    print (line)
    print (line2)
    print (line3)
    for i,j in enumerate(line):
        # print (i, j)
        if i == 4:
            print (j[0])
            # j[0] = info.write("Something I'm writing here!")
            # print (j[0])

    # with open('file', 'r') as input_file, open('new_file', 'r+') as output_file:
    #     for line in input_file:
    #         if line.strip() == 'to replace':
    #             output_file.write('new line\n')
    #         else:
    #             output_file.write(line)

    # print ("time taken to read", (end-start))
    # print (data + "Hi")
    info.close()


for line in fileinput.input('input1.txt', inplace=True):
      print (line.rstrip().replace('Something Im writing here!', 'changed text'),)

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def afterReplacingDisplay(fileName):
    lines = open(fileName, 'r+').readlines()
    print lines

replace_line('input1.txt', 0, 'Mage')
afterReplacingDisplay('input1.txt')

end = time.time()
print ("time difference: ", end - start)


----------------------------------------------------------------------------------------------------

# create the filename.txt and write some txt into it...if that file already exist means just print its already exist

import os
if os.path.exists('filename.txt'):
    print "File exists"

else: 
     with open("filename.txt", 'w+') as fr:
       fr.write("new gen")
       
with open("filename.txt","r") as fw:
    print(fw.read(5))

-------------------------------------------------------------------------------

# Create a file using function and will pass message if its already exists

import os

def create():
    print("Create a next file here:")
    name=raw_input("Please enter the file name:")+'.txt'
    print("file name is:",name)
    try:
        if os.path.exists(name):
            print("its already exists")
        else:
            with open(name,'w') as fr:
                fr.write('jai this is your file...')
            
    except:
        print("Something Happening here...")
        
        
create()
------------------------------------------------------------------------------------


=======================================================
--------------------OS OPERATIONS--------------------
===========================================================
import os
print(os.getcwd()) # TO GET CURRENT WORKING DIRECTORY
print(os.path.abspath('.')) # to get current working directory
print(os.listdir('.')) # directory listdir
os.chdir(".\gum") # changing the directory
print(os.getcwd()) 
os.chdir("../")# go back to parent directory
print(os.getcwd())

--------------------------------------------

os.mkdir("D:\python\pythonIDE\pythonBase\change") # to create the new directory..if the directory is already exist it wil throw an error
print(os.getcwd())


# Leaf directory  
directory = "Nikhil"
      
# Parent Directories  
parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"
      
# Path  
path = os.path.join(parent_dir, directory)  
      
# Create the directory  
# 'Nikhil'  
os.makedirs(path)

os.rmdir(path)

----------------------------------

# File name  
file = 'file1.txt'
      
# File location  
location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
      
# Path  
path = os.path.join(location, file)  
      
# Remove the file  
# 'file.txt'  
os.remove(path)

-----------------------
-----------------------------------------------------------------------------------
# Getting working directory and listing it...storing the listing values into the variable...so by giving change[4] 4th file of the list, I just checking it whether its existing or what?

import os
print(os.getcwd())
print(os.path.abspath('.'))
change=os.listdir('.')
print(change[4])
if os.path.exists(change[4]):
    print("Already exist")
else:
    print("Noooo")

------------------------------------------------------------------------------

#Creating the function with make directory and changing the directory and creating new file as well as writing into it...


import os

def create():
    
    try:
        print(os.getcwd())
        os.mkdir("E:\gum")
        print(os.getcwd())
        os.chdir("E:\gum")
        print(os.getcwd())
        if os.path.exists("filename.txt"):
            print("Its already exist")
        else:
            with open("filename.txt",'w') as fw:
                fw.write("welcome new checking operation")
        
    except:
        print("Cant handle this operation until gets corrected")
        
        
create()


---------------------------------------------------------------------------------------------------------------------
METHOD 2:
import os
def main():
    print("this file may exist already")
    
def create():
    try:
        print(os.getcwd())
        os.chdir("./fund")
        print(os.getcwd())
        name=raw_input("User type the file name you wanna create:")+".txt"
        if os.path.exists(name):
            main()
        else:
            with open(name,'w') as fw:
                fw.write("Hi I am moving towards success")
                
    except:
        print("Techii fault")
        
        
create()

---------------------------------------------------------------------------------------

# How to search the words and replacing it using file HANDLING

METHOD 1:

import fileinput
userFile=raw_input("Enter the file name:")+'.txt'
textToSearch=raw_input("Enter the search word:")
textToCorrect=raw_input("Enter to correct:")
# print(userInput)
with open(userFile,'r+') as fr:
    
    for line in fileinput.input(userFile):
        fr.write(line.replace(textToSearch,textToCorrect))

METHOD 2:

with open('read.txt','r+') as file:
    filedata=file.read()
    filechange=filedata.replace('Internet','Online')

with open('read.txt','w') as file:
    file.write(filechange)


METHOD 3: COUNT OF LETTERS


with open('read.txt','r+') as file:
    filedata=file.read()
print(filedata.count('a'))



-----------------------------------------------------------------------------------

# Read a txt file and do the changes and copy the changed informations to new txt file

with open('read.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('Internet', 'Online')
# print(filedata.count('a'))

# Write the file out again
with open('state.txt', 'w') as file:
  file.write(filedata)


  --------------------------------------------------------------------------------------------------------

  # To check numeric is existing in file or not

with open('fine.txt','r+') as fo:
    for i in fo.read().split():
        if i.isdigit():
            print("yes numeric is existing here",i)
        else:
            pass


-----------------------------------------------------------------------

# adding the new line to the existing file

names = ["Its a new experience to explore", "Different environemnt to explore in swiss"]
with open ('jai.txt','r') as f:
    contents = f.readlines()
    print(contents)
    for i in names:
        contents.append(i)
    print(names)

fw = open('jai.txt', 'w')

fw.write('\n'.join(contents))
fw.close()

----------------------------------------------------------------


# LOGIC 2: adding the new line to the existing file
with open('jai.txt', 'r') as fr:
    lineToWrite = ["aaaa bbbb cccc", 'dddd eeee ffff']
    appendContent = open('jai.txt', 'r').readlines()
    appendContent.extend(lineToWrite)
    print(appendContent)
    newAppendList = []
    for i in appendContent:
        if '\n' not in i:
            newAppendList.append(i+'\n')
        else:
            newAppendList.append(i)
    print(newAppendList)
    open('jai.txt','w').writelines(newAppendList)

------------------------------------------------------------