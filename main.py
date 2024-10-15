class Student:
    def __init__(self, idStudent, name, lastName, email, dateOfBirth, computerCourses=None):
        self.idStudent = idStudent
        self.name = name
        self.lastName = lastName
        self.email = email
        self.dateOfBirth = dateOfBirth
        self.computerCourses = computerCourses if computerCourses is not None else []

    @staticmethod
    def __checkForSkill(sl, rl, c):
        if sl < rl:
            print("Probably, it will be difficult for you...")
        else:
            print(f"Successfully registered to {c} course!")

    def registerInCourse(self, ComputerCourse, knowledgeLevel):
        self.computerCourses.append(ComputerCourse)
        self.__checkForSkill(knowledgeLevel, ComputerCourse.skillRequires, ComputerCourse.name)

class ComputerCourse:
    def __init__(self, idCourse, name, durationInHours, skillRequires, description, idTeacher):
        self.idCourse = idCourse
        self.name = name
        self.durationInHours = durationInHours
        self.skillRequires = skillRequires
        self.description = description
        self.idTeacher = idTeacher
        self.studentsList = []

    def addNewStudent(self, student):
        self.studentsList.append(student)

    def showAllStudents(self):
        print(f"Students enrolled in {self.name} course:")
        for student in self.studentsList:
            print(f"{student.name} {student.lastName}")

class CourseMaterial:
    def __init__(self, title, type_of_material):
        self.title = title
        self.type_of_material = type_of_material

    def display_info(self):
        print(f"Material Title: {self.title}, Type: {self.type_of_material}")

class AdvancedComputerCourse(ComputerCourse):
    def __init__(self, idCourse, name, durationInHours, skillRequires, description, idTeacher, prerequisites):
        super().__init__(idCourse, name, durationInHours, skillRequires, description, idTeacher)
        self.prerequisites = prerequisites

    def showPrerequisites(self):
        print(f"Prerequisites for {self.name}: {self.prerequisites}")

class Exam(ComputerCourse, CourseMaterial):
    def __init__(self, idCourse, name, durationInHours, skillRequires, description, idTeacher, title, type_of_material):
        ComputerCourse.__init__(self, idCourse, name, durationInHours, skillRequires, description, idTeacher)
        CourseMaterial.__init__(self, title, type_of_material)

    def showExamDetails(self):
        print(f"Exam Details: {self.title} for the course {self.name}")

    @staticmethod
    def attempt(minScore, studentScore):
        if studentScore > minScore:
            return True
        else:
            return False

# main()
course1 = ComputerCourse(1, "Computer Science", 10, 0, "Good for beginners", 0)
course2 = AdvancedComputerCourse(2, "Advanced Computer Science", 20, 1, "For advanced learners", 1, "Basic Computer Science")

for i in range(5):
    student = Student(i, f"Student{i}", f"LastName{i}", f"student{i}@example.com", "2000-01-01")
    course1.addNewStudent(student)
    student.registerInCourse(course1, knowledgeLevel=0)

for i in range(5, 10):
    student = Student(i, f"AdvancedStudent{i}", f"LastName{i}", f"advancedstudent{i}@example.com", "2000-01-01")
    course2.addNewStudent(student)
    student.registerInCourse(course2, knowledgeLevel=1)

# output
course1.showAllStudents()
course2.showAllStudents()

course2.showPrerequisites()

#
material1 = CourseMaterial("Intro to Programming", "Video")
material2 = CourseMaterial("Data Structures", "Book")
material1.display_info()
material2.display_info()

exam1 = Exam(3, "testExam", 1, 2, "test your skills before course", 0, "Base Exam", "Test")
if exam1.attempt(5, 10):
    print("😄")
exam1.showExamDetails()