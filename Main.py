# STUDENT CLASS
# use camel-case for class names
class Student:

    def __init__(self, first_name, last_name, courses=None):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = courses

    def find_in_file(self, file_name):
        with open(file_name) as f:
            for line in f:
                first_name, last_name, courses = self.prep_record(line.strip())
                #need strip so there is no whitespace between lines
                #print(first_name, last_name, courses)
                student_read_in = Student(first_name, last_name, courses)
                if Student.__eq__(self, student_read_in):
                    # !! NEED TO USE DUNDER EQ METHOD BECAUSE YOU CAN'T COMPARE OBJECTS WITH CONDITIONAL OPERATORS !!
                    return True
            return False

    def add_to_file(self, file_name):
        if self.find_in_file("data.txt"):
            return "Record already exists"
        else:
            record_to_add = self.prep_to_write(self.first_name, self.last_name, self.courses)
            print(record_to_add)
            with open(file_name, "a+") as write:
                write.write(record_to_add + "\n")
            return "Record Added"

    @staticmethod
    def prep_record(line):
        name, courses = line.split(":")  # breaks up into list of courses and list of first and last name
        first_name, last_name = name.split(",")  # breaks up comma separated name into first name and last name
        courses = courses.split(",")  # breaks up the comma separated string of courses into a list of courses
        return first_name, last_name, courses

    @staticmethod
    def prep_to_write(first_name, last_name, courses):
        full_name = first_name + "," + last_name
        courses = ",".join(courses)
        return full_name + ":" + courses

    def __eq__(self, other):
        first_name_same = self.first_name == other.first_name
        last_name_same = self.last_name == other.last_name
        same = first_name_same and last_name_same
        if same:
            return True
        else:
            return False


nabil = Student("nabil", "koney-laryea", ["java", "python", "sql"])
new_student = Student("joey","schmoe",["rust","assembly","javascript"])
print(nabil.find_in_file("data.txt"))
print(new_student.add_to_file("data.txt"))
