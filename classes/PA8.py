# PA #8 - Hunter Wilson
"""
Add three methods to the Student class that compare two Student objects. 
One method should test for equality. 
A second method should test for less than. 
The third method should test for greater than or equal to. 
In each case, the method returns the result of the comparison of the two students names. 
Include a main function that tests all of the comparison operators.
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
    
    def equal(self, other):
        """Compares based on name"""
        return self.name == other.name
    
    def lessthan(self, other):
        """determines of self.name is less than other.name"""
        return self.name < other.name
    
    def greaterthan(self, other):
        """determines of self.name is greater than other.name"""
        return self.name >= other.name

def main():
    """A simple test."""
    student1 = Student("Ken", 4)
    student2 = Student("Ed", 4)
    student3 = Student("Ken", 4)
    
    for i in range(1, 5):
        student1.setScore(i, 100)

    for i in range(1, 5):
        student2.setScore(i, 85)

    for i in range(1, 5):
        student3.setScore(i, 100)
        
    print(student1)
    print(student2)
    print(student3)

    print("\nComparisons:")
    print(f"Student 1 == Student 2: {student1.equal(student2)}")
    print(f"Student 1 == Student 3: {student1.equal(student3)}")
    print(f"Student 1 < Student 2: {student1.lessthan(student2)}")
    print(f"Student 1 >= Student 2: {student1.greaterthan(student2)}")
    print(f"Student 2 >= Student 1: {student2.greaterthan(student1)}")

if __name__ == "__main__":
    main()
