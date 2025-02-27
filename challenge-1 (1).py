#defines the function as a string
def middle_three_characters(str1):
  
  #finds the middle of the string
  mi=int(len(str1)/2)
  
  #prints the middle three characters
  res=str1[mi-1:mi+2]
  print(res)
  
  #prompts a user to enter a string
user_input=input("Enter here:")

#calls the function and prints the computed result
middle_three_characters(user_input)
