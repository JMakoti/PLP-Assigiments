# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
#Read the file
file = open("python-week4/assignment_contacts.txt", "r")
content = file.read()
print(content)

modified_content = content + "\nName: John Doe\nEmail: john.doe@gmail.com\nPhone: 123-456-7890\n"

#Write a modified content to the file
with open("python-week4/assignment_contacts_modified.txt", "w") as new_file:
    new_file.write(modified_content)