#defines the variable "power_int_list" as a function
def power_int_list(int_list, power):
  
  #creates a new list
  result_list=[]
  
#for expression that iterates through the entered list, raises them to the entered power
  for num in int_list:
    result_pow=num**power
    
#returns the result and appends it to the new list
    result_list.append(result_pow)
  return result_list
  
#prompts the user to enter a list of desired integers
test_list_str=input("Enter a list of integers separated with commas:")

#converts the string to a list of integers
test_list=[int(x) for x in test_list_str.split(',')]

#prompts the user to enter a power they wish to raise the integers to
power=int(input("Enter power to raise integers to:"))

#recalls the function defined in the earlier code and returns the computed results
result_pow=power_int_list(test_list, power)
print(result_pow)