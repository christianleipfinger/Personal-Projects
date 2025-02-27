#reads a letter from the alphabet from user
letter=input ("Enter letter of the alphabet")

#displays if it is a vowel
if letter in ["a", "e", "i", "o", "u"]:
  print(letter,"is a vowel")

#displays y as a vowel and consonant
elif letter in ["y"]:
  print(letter,"is sometimes a vowel, and sometimes a consonant")

#displays all other letters as a consonant
else:
  print(letter,"is a consonant")