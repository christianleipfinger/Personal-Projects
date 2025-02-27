#reads user input of grade percentage
#displays their grade as a letter
#how far they are from the next highest grade
#an encouraging or discouraging message based on their grade
grade=float(input("Enter grade percentage"))
if grade>=90:
  print("A")
  print("You are", grade-89, "points away from a B")
  print("You are doing exceptional!")
elif grade>=80:
  print("B")
  print("you are", 90-grade, "points away from an A")
  print("You are doing good!")
elif grade>=70:
  print("C")
  print("you are", 80-grade, "points away from a B")
  print("You are doing okay.")
elif grade>=60:
  print("D")
  print("you are", 70-grade, "points away from a C")
  print("you are not doing good.")
elif grade>=0:
  print("F")
  print("you are", 60-grade, "points away from a D")
  print("you are failing.")