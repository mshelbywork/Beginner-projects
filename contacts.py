# create a smart contacts manager

'''menu system: (while loop)
1. Add contact
2. View all contacts
3. Search contact
4. Modify tags
5. Delete contact
6. Exit
'''

contacts = {
    "Name": {
        "phone": "...",
        "email": "...",
        "tags": {"tag1", "tag2"}
    }
}

'''
1. add contact, multiple prompts stored as values for each list
possibly a for loop that reprompts until task is complete. 
name.title() verify area code? verify email?

2.display everything

3.search function
do I need to ask or auto detect search type?
search nested function contacts [name]

4. modify tags (somethign to do with sets).
maybe tag = variable, setlist updated to variable? pulls variable
when it's time to update. possibly other for loop to add tags
and /or view tags. 

5. delete contact
search or flip through? enumerate to make selection easier?

6. quit - ends while loop
'''
'''
def add_contact():
        name = input ('Name: ')
        phone = int(input ('Phone Number: '))
        # if phone.count() < 7:
            print ('Phone number is less than 7 digits')
            print ('Is this correct \n 1.Yes \n 2.No')
            confirm= int(input ('please select number'))
            if confirm != 1:
                phone = input ('Phone Number: ')
        email = input ('Email: ')
       # if not email.string.includes ('@'):
            print ('email missing @, please try again')
            email = input ('Email: ')
        print ('tags:Work, Family, School, etc')
        tags = input ('tags:')
        contacts[name] = {}
        contacts[name]['phone'] = phone
        contacts[name]['email'] = email
        contacts[name]['tags'] = tags
    return contacts

add_contact ()
'''

'''
def view_contacts():
    for views in contacts:
        print (contacts.items())
view_contacts()
'''

def search():
    print ('would you like to search by \n 1. name \n 2. email \n 3. phone \n 4. tag \n 5. go back')
    search_type = int(input ('select number: '))
    if search_type ==1:
        name = input('Name:')
        contact = contacts.get(name)
        if contact:
            print (f'Name: {name}, Email: {contact[email]}, Phone Number: {contacts[phone]}, Tags: {' ,'.join(contacts[tags])}')
        else:
            print ('contact not found')
    elif search_type ==2:
        email = input('email:')
        found = False
        for name, info in contacts.items():
            if info["email"] == email_search:
                print(f"Name: {name}, Email: {info['email']}, Phone: {info['phone']}, Tags: {', '.join(info['tags'])}")
                found == True
            else: 
                print ('No contact found with that email')
    elif search_type ==3:
        find_phone = input('phone:')
        found = False
        for name, info in contacts.items():
            if info['phone'] == find_phone:
                print(f"Name: {name}, Email: {info['email']}, Phone: {info['phone']}, Tags: {', '.join(info['tags'])}")
                found = True
            else: 
                print ('No contact was found with that phone number')
        contacts.get(phone)
    elif search_type ==4:
        find_tag = input('tag:')
        found = False
        for name, info in contacts.items():
            if info['tags'] == find_tag:
                print(f"Name: {name}, Email: {info['email']}, Phone: {info['phone']}, Tags: {', '.join(info['tags'])}")
                found == True
            else:
                print('No tags found')
search()
