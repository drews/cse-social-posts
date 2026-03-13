from Post import Post

options = ["new","username","print","quit","remove"]

def prompt():
    return input(f"please select an action: {', '.join(options)}\n")
def handleNew():
    pass
def handleUsername():
    pass
def handlePrint():
    pass
def handlequit():
    pass
def handleRemove():
    pass

all_posts_archive = []

user_input = prompt()
while user_input != "quit":
    if user_input not in options:
        print("Not an option, please try again...")
    elif user_input == "new":
        handleNew()
    elif user_input == "username":
        handleUsername()
    elif user_input == "print":
        handlePrint()        
    elif user_input == "remove":
        handleRemove()
    user_input = prompt()
exit(0)