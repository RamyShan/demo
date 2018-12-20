"""This is a 
multiline docstring."""

# comment

thisissue = []

thisall =	[{
  "id": 101,
  "Title": "Head first JavaScript",
  "Author": "JS"
},{
  "id": 102,
  "Title": "Head first JSON",
  "Author": "JSON"
},{
   "id": 103,
  "Title": "Head first Typescript",
  "Author": "TS"
},{
   "id": 104,
  "Title": "Head first HTML",
  "Author": "HTML"
},{
   "id": 105,
  "Title": "Head first PYTHON",
  "Author": "PY"
}]


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$                              $$$$$$$$$$$$")
print("$$$$$$$$$$$     Library Management       $$$$$$$$$$$$")
print("$$$$$$$$$$$                              $$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


def print_dict(entity):
    for i in entity:
        print("Book id : " + str(i["id"]))
        print("Book Title : " + i["Title"])
        print("Book Author : " + i["Author"])
        print("\n\n")
    
def add_book(entity):
    temp_id = raw_input('Enter Book id')
    temp_title = raw_input('Enter Book Title')
    temp_Author = raw_input('Enter Book Author')
    entity.append({"id": temp_id,"Title": temp_title,"Author": temp_Author})

def search_book(entity):
    print("1. Search book by id ")
    print("2. Search book by Title ")
    print("3. Search book by Author ")
    search_option = raw_input('Enter the choice : ')
    if search_option == "1":
      temp_id = raw_input('Enter the id : ')
      j=1
      for i in entity:
        if(str(i["id"]) == temp_id):
          print("Book is avaliable")
          print(i)
        else:
          if(j==(len(entity)-1)):
            print("End of search")
            break
        j = j+ 1
    elif search_option == "2":
      temp_title = raw_input('Enter the Title : ')
      j=1
      for i in entity:
        # if((i["Title"]).upper() == (temp_title).upper()):
        if((temp_title).upper() in (i["Title"]).upper()):
          print("Book is avaliable")
          print(i)
        else:
          if(j==(len(entity)-1)):
            print("End of search")
            break
        j = j+ 1
    elif search_option == "3":
      temp_author = raw_input('Enter the Author : ')
      j=1
      for i in entity:
        # if((i["Author"]).upper() == (temp_author).upper()):
        if((temp_author).upper() in (i["Author"]).upper()):
          print("Book is avaliable")
          print(i)
        else:
          if(j==(len(entity)-1)):
            print("End of search")
            break
        j = j+ 1


def remove_book_id(entity,temp_id):
  j=1
  for i in entity:
    if(str(i["id"]) == temp_id):
      try:
        entity.pop(j)
      except IndexError:
        entity.pop()
      print(i)
  j = j+ 1

def remove_book(entity):
  temp_id = raw_input('Enter the id : ')
  remove_book_id(entity,temp_id)

def append_book(entity,issue,temp_id):
  for i in entity:
    if(str(i["id"]) == temp_id):
      issue.append(i)

def issue_book(entity,issue):
  temp_id = raw_input('Enter the id : ')
  append_book(entity,issue,temp_id)
  remove_book_id(entity,temp_id)


while True:

  print("1. Display all Books ")
  print("2. Add a new book ")
  print("3. Search a book ")
  print("4. Remove a book ")
  print("5. Issue a book ")
  print("6. Display issued book ")
  print("7. Return a book ")
  print("8. Quit the application")

  option = raw_input('Enter a option to go : ')

  if option == "1":
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n$$$$$$$$$$$$$$$$$$$$$       Display all books      $$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print_dict(thisall)
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n \n ")
  elif option == "2":
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n$$$$$$$$$$$$$$$$$$$$$           Add a book         $$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    add_book(thisall)
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n \n ")
  elif option == "3":
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n$$$$$$$$$$$$$$$$$$$$$       Search in all books    $$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    search_book(thisall)
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n \n ")
  elif option == "4":
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n$$$$$$$$$$$$$$$$$$$$$       Remove a book          $$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    remove_book(thisall)
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n \n ")
  elif option == "5":
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n$$$$$$$$$$$$$$$$$$$$$         Issue a book         $$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    issue_book(thisall,thisissue)
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n \n ")
  elif option == "6":
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n$$$$$$$$$$$$$$$$$$$$$   Display all issued books   $$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print_dict(thisissue)
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n \n ")
  elif option == "7":
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n$$$$$$$$$$$$$$$$$$$$$       Return back a book     $$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    issue_book(thisissue,thisall)
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n \n ")
  elif option == "8":
    print('closing application')
    break



