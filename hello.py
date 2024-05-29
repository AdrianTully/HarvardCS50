# ask user for their name
name = input("what's your name? ")
# name = input("what's your name? ").strip().title()

# remove shitespace from name
name=name.strip()

# name=name.strip().title()
# allows you to string functions together

# captilise
name = name.title()

# say hello to user
print("Hello,", name)
