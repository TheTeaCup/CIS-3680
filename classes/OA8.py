# OA #8 - Hunter Wilson
"""
This project assumes that you have completed PA 8. 
Place several Student objects into a list and shuffle it. 
Then run the sort method with this list and display all of the students information.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    
    def __eq__(self, other):
        """Compares based on name"""
        return self.name == other.name
    
    def __lt__(self, other):
        """determines of self.name is less than other.name"""
        return self.name < other.name
    
    def __ge__(self, other):
        """determines of self.name is greater than other.name"""
        return self.name >= other.name

def main():
    """A simple test."""
    student1 = Student("Ken", 4)
    student2 = Student("Ed", 4)
    student3 = Student("Ken", 4)
    student4 = Student("Hunter", 4)
    
    for i in range(1, 5):
        student1.setScore(i, 100)
        student2.setScore(i, 85)
        student3.setScore(i, 100)
        student4.setScore(i, 75)
        
    studentList = [student1, student2, student3, student4]
    studentList.sort()

    print("Sorted List:\n")
    for student in studentList:
        print(student, "\n")

    

if __name__ == "__main__":
    main()
