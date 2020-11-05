import dbfunctions
while True:
    dbfunctions.username= input("Please enter your username:  ")
    userChoice = input(" 1: to Write a post   or   2: to See all other posts:  ")
    if userChoice in ('1', '2'):
        if userChoice == '1':
            dbfunctions.insert_data()
        elif userChoice == '2':
            dbfunctions.show_data()
