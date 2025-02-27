#input dictionary to compute that was provided in the assignment
input_dict = {
  "kg593":"A",
  "gks59":"D",
  "fks50":"A",
  "ggo35":"C",
  "y0e32":"C",
  "hh205":"A",
  "hpr03":"C",
  "gi492":"A", 
  "p03s2":"A", 
  "gl320":"C", 
  "hle32":"D", 
  "f0324":"B", 
  "sdl04":"D", 
  "sdg66":"A"}

#creates a new dictionary to store the values of the input dictionary
value_number={}
for val in input_dict.values():
  value_number[val]=value_number.get(val,0)+1

#defines Sort_dict function to sort in descending order
def sort_dict(val):
  return value_number[val]

#iterates through the dictionary and prints the key and value
sorted_values=sorted(value_number.keys(), key=sort_dict, reverse=True)

#creates frequency dictionary as new dictionary that sorts values in descending order
frequency={}
for val in sorted_values:
  frequency[val]=value_number[val]

#prints the frequency dictionary in descending order it the prequency of the values
for key, value in frequency.items():
  print(f"{key}: {value}")
  