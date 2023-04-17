print("ToDo List Manager")

ToDo = []

def printToDo():
  print()
  i = 0
  for item in ToDo:
    i += 1
    print(f"{i}.{item}")
  print()

while True:
  menu = input("Do you want to view, add, or edit the todo list?: ")
  if menu == "add":
    item = input("What do you want to add?: ")
    ToDo.append(item)
  elif menu == "edit":
    item = input("What do you want to remove?: ")
    if item in ToDo:
      ToDo.remove(item)
    else:
      print(f"{item} was not in the list")
  elif menu == "view":
    printToDo()