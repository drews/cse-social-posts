from Post import Post

all_posts_archive = []
options = ["new","username","print","quit","remove"]

def prompt_action():
    """asks the user which action they'd like to carry out"""
    return input(f"please select an action: {', '.join(options)}\n")

def new_post(user):
    """Constructs Post and adds it to the archive."""
    all_posts_archive.append(
        Post(user, input("Please enter message to post: "))
    )

def prompt_username():
    return input("What's your username: ")

def print_posts():
    for p in all_posts_archive:
        print(p)

def remove_post():
    raise NotImplementedError


username = prompt_username()
action_requested = prompt_action()
while action_requested != "quit":
    if action_requested not in options:
        print("Not an option, please try again...")
    elif action_requested == "username":
        username = prompt_username()
    elif action_requested == "new":
        new_post(username)
    elif action_requested == "print":
        print_posts()        
    elif action_requested == "remove":
        remove_post()
    action_requested = prompt_action()
# naturally exit