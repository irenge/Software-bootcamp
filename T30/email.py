class Email:
    has_been_read = False
    is_spam = False
    
    def __init__ (self, email_contents, from_address):
        self.from_address = from_address
        self.email_contents = email_contents
    
    # method 
    def mark_as_read(self):
        self.has_been_read = True
    
    def mark_as_spam(self):
        self.is_spam = True

inbox = [Email("Hello", "jbi.octave@gmail.com"), Email("Hi    ", "jules@gmail.com   ")]

def add_email(contents, email):
    new_email = Email(contents, email)
    inbox.append(new_email)

def get_count(inbox):
    return len(inbox)

def get_email(i):
    print(inbox[i].email_contents)
    inbox[i].mark_as_read()

def get_unread_emails():
    unread = []
    for message in inbox:
        if message.has_been_read == False:
            unread.append(message)
    return unread

def get_spam_emails():
    spam = []
    for email in inbox:
        if email.is_spam == True:
            spam.append(email)
    return spam

def delete(i):
    inbox.remove(inbox[i])

def convert(x):
    if x == True:
        return "Yes"
    elif x == False:
        return "No"
def entry():
    while True:
        try:
            x = int(input("Enter the ID number of the email: "))
            break
        except ValueError:
            print("Oops! That was not a valid number. Try again ...")
    return x


### create a list to store al emails

# An Email Simulation
user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/delete/send/quit?")
    length = get_count(inbox)

    if user_choice == "read":
        print("ID EMAIL               CONTENTS     IS_READ")
        for i in range (length):
            print(f"{i} {inbox[i].from_address} {inbox[i].email_contents}      {convert(inbox[i].has_been_read)}")
        
        while True:
            x = entry()
            if x >= 0 and x < length:
                print("The content is ")
                get_email(x)
                print()
                break
            else:
                print(f"Please enter between 0 inclusive and  {length - 1} inclusive")
        unread = get_unread_emails()
        if len(unread) == 0:
            print("All mails have been read")
        else:
            print("UNREAD EMAILS")
            print("ID EMAIL               CONTENTS     IS_READ")
            for un in unread:
                print(f"{un.from_address} {un.email_contents} {convert(un.has_been_read)}")

    elif user_choice == "mark spam":
        print("ID EMAIL               CONTENTS\tSPAM")
        for i in range (length):
            print(f"{i} {inbox[i].from_address}\t{inbox[i].email_contents}\t{convert(inbox[i].is_spam)}")
        x = entry()
        if x >= 0 and x < length:
            y = inbox[x]
            y.mark_as_spam()
        ## print list of spam 
        spam = get_spam_emails()
        print("SPAM EMAILS")
        for sp in spam:
            print(f"{sp.from_address}\t{sp.email_contents}\t{convert(sp.is_spam)}")
    elif user_choice == "send":
        address = input("Enter the email address to send to: ")
        contents = input("Type in the message to send:")
        add_email(contents, address)
    elif user_choice == "delete":
        for i in range (length):
            print(f"{i} {inbox[i].from_address} {inbox[i].email_contents} ")
        while True:
            x = entry()
            if x >= 0 and x < length:
                print("The content is ")
                delete(x)
                print()
                break
            else:
                print(f"Please enter between 0 inclusive and  {length - 1} inclusive")
        length = get_count(inbox)
        print("Now after deletion the list is ")
        if length == 0:
            print("The inbox is empty")
        else:
            for i in range (length):
                print(f"{i} {inbox[i].from_address} {inbox[i].email_contents}")

    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
