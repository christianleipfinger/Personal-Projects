#reads name of a month from user
month=input("Enter month")

#displays 31 days for months with 31 days
if month in ["January", "March", "May", "July", "August", "October", "December"]:
    print(month, "has 31 days")

#displays 30 days for months with 30 days
elif month in ["April", "June", "September", "November"]:
  print(month, "has 30 days")

#displays days in February
elif month=="February":
  print (month, "has 28 days, but 29 days on a leap year")      