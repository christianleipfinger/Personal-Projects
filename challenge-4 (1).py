#defines the email domain and splits the entered information
def extract_email_domain(email):
  return email.split("@")[-1]

#reads the info from the user and stores it in a dictionary
def main():
  domain_count={}

  #prompts the user to enter the email address information
  print("Enter email addresses line by line, then type 'done' when finished")

  #true statement for in correspondence with the user input
  while True:
    user_input=input()
    if user_input.lower()=="done":
      break

   #splits the email addresses into a list, then lists only the domains
    words=user_input.split()
    for word in words:
      if "@" in word:
        email=extract_email_domain(word)
        domain_count[email]=domain_count.get(email, 0)+1

  #prints the email domain and the number of times it appears based on the input
  print(domain_count)

main()




