import os

Users = []
Books = {}
#Users = 
#     [
    # [
    #   ["Aryan", "keskar"], 
    #   ["LOTR", "HP", "Manushruti", "Bhagvad Puran"]
    # ], 
    # [
        # ["Vigneshwar", "Ananth"], 
        # ["HP"]
    # ]
    # ]
#Books = [["LOTR", 2], ["HP", 4]]

def createUser(username,  password):
    info = []
    info.append(username)
    info.append(password)
    books =[]
    user = []
    user.append(info)
    user.append(books)
    Users.append(user)
    
def loadBooks():
    file = open("Books.txt", "r")
    books = file.readlines()
    #print(books)
    for i in range(len(books)):
        bookinfo = books[i].split(',')
        bookinfo.pop(len(bookinfo)-1)
        num = int(bookinfo[1].strip())
        Books[bookinfo[0]] = num
    file.close()
    
def loadUserData():
    file = open("Users.txt", "r")
    
    rawUsers = file.readlines()

    for i in range(len(rawUsers)):
        user = []
        Rawuser = rawUsers[i].split(',')
        Rawuser.pop(len(Rawuser)-1)
        info = []
        books = []
        info.append(Rawuser[0])
        info.append(Rawuser[1])
    
        for j in range(len(Rawuser)):
            if j > 1:
                books.append(Rawuser[j])
        
        user.append(info)
        user.append(books)
        Users.append(user)
    

    file.close()

def AppendUser():
    user = Users[len(Users)-1]
    file = open("Users.txt", "a")
    for i in range(len(user)):
        for j in range(len(user[i])):
            if i == (len(user)-1) and j ==(len(user[i])-1):
                file.write(user[i][j]+",\n")
            else:
                file.write(user[i][j]+", ")
    
    file.close()

def checkLogin(username, password):
    for i in range(len(Users)):
        userPassword = Users[i][0][1].strip()
        if(Users[i][0][0] == username and userPassword== password):
            return Users[i][0][0]
    return 'False'
        
def updateUsers():
    file = open("Users.txt", "w")
    newContents = ""
    for u in Users:
        user_data = ""
        for cred in u[0]:
            user_data += cred
            user_data += ", "
        
        for i in range(len(u[1])):
            user_data += u[1][i] + ", "

        newContents += user_data + "\n"

    file.write(newContents)
    file.close()

def ReturnBook(username, book):
    for u in Users:
        uname = u[0][0].lower()
        if uname == username.lower():
            idx = 2
            found = False
            while idx < len(u[1]) and not found:
                cur_book = u[1][idx].lower()
                if cur_book == book.lower():
                    found = True
                else:
                    idx += 1
    
            ret_book = u[1].pop(idx)
            print(f"The book titled {ret_book} was returned")
            break

    updateUsers()

def updateBooks():
    file = open("Books.txt", "w")
    newBooks = ""
    for k in Books.keys():
        book = k
        count = Books[book]
        line = f"{book}, {count},"
        newBooks += line + "\n"
    
    file.write(newBooks)
    file.close()

def IssueBook(username, book):
    for i in range(len(Users)):
        if (Users[i][0][0] == username):
            if book in Books:
                initialCnt = Books[book]
                if initialCnt == 0:
                    print(f"Book {book} is fully borrowed (Count = 0)")
                else:
                    Users[i][1].append(' '+book)
                    Books.update({book:(initialCnt - 1)})
                    updateUsers()
                    updateBooks()
            else:
                print(f"Book {book} does not exist in library")
            break

def Profile(username):
    for i in range(len(Users)):
        if(Users[i][0][0] == username):
            print(Users[i])

def displayBooks():
    return 0

username = 'False'
while(username == 'False'):
    loadUserData()
    loadBooks()
    
    print("Enter 1 to login")
    print("Enter 2 to create new account")
    userinput = input("Enter your response: ")
    if(userinput == "1"): 
        inputuser = input("Enter your username: ")
        passwordInput = input("Enter your password: ")
        username = checkLogin(inputuser, passwordInput)
    elif(userinput == "2"):
        inputuser = input("Enter your username: ")
        passwordInput = input("Enter your password: ")
        createUser(inputuser, passwordInput)
        AppendUser()

userInput = ''
while(userInput != '4'):
    print("Enter 1 to issue a book")
    print("Enter 2 to return a book")
    print("Enter 3 to view your profile")
    print("Enter 4 to logout and exit the application")
    userInput = input("Enter your response: ")
    if(userInput == '1'):
        displayBooks()
        book = input("enter the name of the book you want to issue: ")
        IssueBook(username, book)
    elif(userInput == '2'):
        book  = input("Enter the name of the book you want to return: ")
        ReturnBook(username, book)
    elif(userInput == '3'):
        Profile(username)
    
    