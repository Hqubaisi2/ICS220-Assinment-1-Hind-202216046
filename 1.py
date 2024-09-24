class Student :
    def __init__(self,sid,sname,sscore):
        self.student_id=sid
        self.student_name=sname
        self.score=sscore
    def printStudentDetails(self):
        print(self.student_name, self.student_id, self.score)

#Test
s1=Student("2023",sname:"Tim",sscore:90)
s1.printStudentDetails()

s2=Student("2023",sname:"John",sscore:85)
s2.printStudentDetails()