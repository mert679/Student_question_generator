import random

print("--STUDENT QUESTION GENERATOR--") 
print("Using this application you can manage students and questions") 
print(". You can also select a random question for a random student ") 
print(". ") 
print()
print("Existing students: ")



def showStudents(students):
  
  for student in range(len(students)):
    print(int(student)+1,students[student])


students = ["Fatma" , "Taha" , "Aras"]
for s in range(len(students)):
    print(int(s)+1,".",students[s])

print()




print()
print("Existing questions: ") 
questions = ["What is the difference between while and for loops? ", "How can you print custom error messages for runtime errors? "]

def showQuestions(questions):

  for question in range(len(questions)):
    print(int(question)+1,questions[question])

for q in range(len(questions)):
    print(int(q)+1,".",questions[q])
print()
print()
print()

print("Choose one of the actions: ")
print("A -> Add student")
print("M -> Move the student up in the list")
print("R -> Remove student by name")
print("RL -> Remove the last student")

print("----------------------------------")

print("a -> Add question")
print("r -> Remove question by item number ")
print("rl -> Remove the last question ")
print("G -> Randomly assign a question to a student")
print("Q -> Quit the application ")


while True:
  order = input("Please choose an action: ")
  if order == "A":
    addStudent = str(input("Enter the student name to be added: "))
    students.append(addStudent)
    showStudents(students)
  
  elif order == "M":
    chgItem = int(input("Enter the item number to move up. ")) - 1
    studentsArr = students[chgItem-1]
    students[chgItem-1] = students[chgItem]
    students[chgItem] =  studentsArr
    showStudents(students)


  elif order == "R":
    delStudent = str(input("Enter the student name to be removed: "))
    if delStudent in students:
      print("The student is deleted.")
      students.remove(delStudent)
      showStudents(students)
    else:
      print("This student is not exist. ")
      continue
  elif order == "RL":
    print("The last student in the list deleted. ")
    students.pop()
    showStudents(students)
    
    
  elif order == "a":
    addQuestion = str(input("Enter a question to be added "))
    if addQuestion != "":
      questions.append(addQuestion)
      showQuestions(questions)
    else:
      print("Please enter question.")
      continue
  elif order == "r":
    quesNumb = int(input("Enter the question number to be removed: ")) -1 
    del questions[quesNumb]
    showQuestions(questions)
  elif order == "rl":
    print("The last question in the list is deleted.")
    questions.pop()  
    showQuestions(questions)

  elif order == "G":
    stdRand = random.choice(students)
    qstnRand = random.choice(questions)
    print(qstnRand,"is asked for",stdRand)
  elif order =="Q":
    print("Goodbye")
    break

