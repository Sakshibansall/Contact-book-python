contacts={}

# adding contacts
def add_contact():
  name=input("enter name: ")
  
  if name in contacts:
    print("contact already exists")
  else:
    number=input("enter the number: ")
    contacts[name]=number
    print("contact added successfully")


# get all contacts
def get_all_contacts():
  if contacts=={}:
    print("no contacts found")
  else:
    for key,value in contacts.items():
      print(f"{key}: {value}")
    
# search contact
def search_contact(contacts,name):
  if name in contacts:
    print(contacts[name])
  else:
    print("contact not found")
  
#delete contact
def delete_contact(contacts,name):
  if name in contacts:
    contacts.pop(name)
    print("contact deleted successfully")
  else:
    print("contact not found")

#update contact
def update_contact(contacts,name):
  if name in contacts:
    print("contact found")
    print("do you want to update the name or number? yes/no")
    k="yes"
    g=input()
    if k==g.lower():
      new_number=input("enter the new number: ")
      contacts[name]=new_number
      print("contact updated successfully")
    else:
      print("contact not updated")
  else:
    print("contact not found")



while True:
  print("1. add contact")
  print("2. get all contacts")
  print("3. search contact")
  print("4. delete contact")
  print("5. update contact")
  print("6. exit")
  
  choice=int(input("enter your choice: "))
  
  if choice==1:
    add_contact()
  elif choice==2:
    get_all_contacts()
  elif choice==3:
    name=input("enter the name to search: ")
    search_contact(contacts,name)
  elif choice==4:
    name=input("enter the name to delete: ")
    delete_contact(contacts,name)
  elif choice==5:
    name=input("enter the name to update: ")
    update_contact(contacts,name)
  elif choice==6:
    break
  else:
    print("invalid choice")
