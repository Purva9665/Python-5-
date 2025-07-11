dict={'Alice':85,'Jhon':90,'krishna':99}
name=input("Enter the student name: ")
if name in dict:
    print(f"{name}'s marks: {dict[name]}")
else:
    print("Student name not found.")

