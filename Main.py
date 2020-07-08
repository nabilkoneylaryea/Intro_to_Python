# STUDENT CLASS
# use camel-case for class names
class Student:

    def __init__(self, first_name, last_name, courses=None):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = courses

    def find_in_file(self, file_name):
        pass
        with open(file_name) as f:
            for line in f:
                first_name, last_name, courses = self.prep_record(line.strip())
                student_read_in = Student(first_name, last_name, courses)
                if self == student_read_in:
                    return True
        return False

    def add_to_file(self, file_name):
        pass

    @staticmethod
    def prep_record(line):
        name, courses = line.split(":")  # breaks up into list of courses and list of first and last name
        first_name, last_name = name.split(",")  # breaks up comma separated name into first name and last name
        courses = courses.split(",")  # breaks up the comma separated string of courses into a list of courses
        return first_name, last_name, courses

nabil = Student("nabil", "koney-laryea", ["java", "python", "sql"])
print(nabil.find_in_file("data.txt"))