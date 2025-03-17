from abc import ABC, abstractmethod

class HUCISAClass(ABC):
    def __init__(self, instructor, students=None):
        self.instructor = instructor
        self.students = students if students else []
    
    def enroll(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"{student} has enrolled in {self.__class__.__name__}.")
        else:
            print(f"{student} is already enrolled in {self.__class__.__name__}.")
    
    def attend_class(self, student):
        if student in self.students:
            print(f"{student} is attending {self.__class__.__name__}.")
        else:
             print(f"{student} is not enrolled in {self.__class__.__name__}.")
    
    def learn(self):
        pass
    
class WebDevClass(HUCISAClass):
    def learn(self):
        print(f"Students in {self.__class__.__name__} are learning HTML, CSS, JavaScript.")

class CPClass(HUCISAClass):
    def learn(self):
        print(f"Students in {self.__class__.__name__} are learning Algorithms and Leetcode.")
        
web_dev = WebDevClass("Abdulfetahm", ["Abenezer", "Dawit"])
cp2025 = CPClass("Kidus", ["Leul", "Ahlam", "Miftah", "Lemi"])
# web_dev.enroll("Dawit")
# cp2025.attend_class("Miftah")

cp2025.learn()
web_dev.learn()
        