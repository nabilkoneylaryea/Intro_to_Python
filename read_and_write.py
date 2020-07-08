# READING A FILE
#
# OPTION ONE ON OPENING AND READING FILES
#
# file_name = "data.txt"
# f = open(file_name)
# #This gives an error??
# f_contents = f.read()
# print(f_contents)
# # COULD RUN INTO MEMORY PROBLEMS IF YOU DON'T CLOSE
# # KINDA LIKE A DATABASE
# f.close()
#
# OPTION TWO ON OPENING AND READING FILES
#
# file_name = name
# f = open(name)
# for line in name:
#   print(line)
# f.close()
# EXAMPLE:
# file_name = "data.txt"
# f = open(file_name)
# for line in f:
#     print(line)
# f.close()
# NOTE: Can use line.strip() to get rid of white space between lines
#
# OPTION THREE (BEST PRACTICE USING A CONTEXT MANAGER)
#
# name = "data.txt"
# with open(name) as f:
#   for line in f:
#       print(line)
#
# NOTE: this method makes it easier
#
# BUILDING A FUNCTION TO CONVERT INFO FROM A FILE TO VALUES THAT CAN BE PASSED INTO A CONSTRUCTOR
# LINE FORMAT ON FILE: first_name,last_name:course_1,course_2,etc.
# CONSTRUCTOR:

def prep_record(line):
    name, courses = line.split(":")  # breaks up into list of courses and list of first and last name
    first_name, last_name = name.split(",")  # breaks up comma separated name into first name and last name
    courses = courses.split(",")  # breaks up the comma separated string of courses into a list of courses
    return first_name, last_name, courses

def prep_to_write(first_name, last_name, courses):
    full_name = first_name + "," + last_name
    courses = ",".join(courses)
    return full_name + ":" + courses

name = "data.txt"
with open(name) as f:
    for line in f:
        print(line.strip())
        first_name, last_name, courses = prep_record(line)
        print(first_name, last_name, courses)



#
# WRITING / APPENDING TO A FILE
#
# second argument in open() method is the mode
# when you write to a file using the "w" mode you are replacing what is already in the file
# use the "a+" mode to append to a file
# a - append
# + - if the file doesn't already exist make the file
# record_to_add = "My name is " + name
# with open(name, "w") as write:
#   write.write(record_to_add + "\n")