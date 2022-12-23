def show_options():
  print("You can \n1. Create a new contact \n2. Delete a contact \n3. Modify a phone number \n4. Modify an email \n5. Show contacts\n6. Exit the phonebook")
  action = int(input("Please choose number:"))
  return action

def create_new_contact(phonebook):
  name_contact = input("The name: ")
  phone_number_contact = input("The number: ")
  email_contact = input("The email: ")
  if name_contact in phonebook:
    print("This contact all ready exists.")
    rep = input("Do you want to change it ? (Yes/No):")
    if rep == "No":
      print("No contact has been changed.")
      return
  list_1 = [phone_number_contact, email_contact]
  phonebook[name_contact] = list_1
  print("The new contact has been created/ changed.")

def delete_contact(phonebook): 
  delete_name = input("What is the name of the contact you want to erase ?:")
  if delete_name in phonebook:
    phonebook.pop(delete_name) 
    #del phonebook[delete_name]
    print(phonebook)
  else: 
    print("Sorry, this name is not registered in your phonebook.")

def modify_phone_number(phonebook): 
  change_name = input("What is the name of the contact you want to change (the number) ?:")
  if change_name in phonebook:
    new_phone_num = input("What is the new phone number ?")
    #list1 = phonebook[change_name]
    #email_contact = list1[1]
    #list1 = [new_phone_num, email_contact]
    #phonebook[change_name] = list1
    phonebook[change_name][0] = new_phone_num
    print(phonebook)
    print("The contact's number has been change")
  else: 
    print("Sorry, this name is not registered in your phonebook.")

def modify_email(phonebook): 
  change_name = input("What is the name of the contact you want to change (the number) ?:")
  if change_name in phonebook:
    new_email_num = input("What is the new email contact ?")
    #list1 = phonebook.get(change_name)
    #num_contact = list1[0]
    #list1 = [num_contact, new_email_num]
    #phonebook[change_name] = list1
    phonebook[change_name][1] = new_email_num
    print(phonebook)
    print("The contact's email has been change")
  else: 
    print("Sorry, this name is not registered in your phonebook.")

def show_contacts(phonebook):
  #for key in phonebook.keys():
  #  print(key, ",", phonebook[key][0], ",", phonebook[key][1])
  for key, value in phonebook.items():
    print(key, ",", value[0], "," , value[1])


def save_phonebook(phonebook):
  phonebook1 = ""
  for key in phonebook.keys():
    contact = key + ", " + phonebook[key][0] + ", " + phonebook[key][1] + "\n"
    phonebook1 += contact
  with open("phonebook.txt", "w") as fil:
    fil.write(phonebook1)




def run_program():
  phonebook = {}
  action = show_options()
  while action != 6: 
    if action == 1:
      #print("Entered create new contact")
      create_new_contact(phonebook)
    elif action == 2:
      #print("Entered delete contact")
      delete_contact(phonebook)
    elif action == 3:
      #print("Entered modify phone number")
      modify_phone_number(phonebook)
    elif action == 4:
      #print("Entered modify email")
      modify_email(phonebook)
    elif action == 5:
      #print("Entered create show contacts")
      show_contacts(phonebook)
    else:
      print("Sorry this option does not exist.")
    action = show_options()
  save_phonebook(phonebook)

run_program()