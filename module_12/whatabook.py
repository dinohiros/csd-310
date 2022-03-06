import mysql.connector 
from mysql.connector import errorcode
import sys 

config = {
    "user": 'whatabook_user',
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#show the menu to the user 
def show_menu():
    print("\n  --- MAIN MENU ---")

    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program")

    try:
        choice = int(input('      <Example: enter 1 to view all books>: '))

        return choice
    except ValueError:
        print("\n  Invalid entry. Goodbye...\n")

        sys.exit(0)

#show all the books to the user
def show_books(_cursor):
    
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    #get results from cursor
    books = _cursor.fetchall()

    print("\n  -- DISPLAYING BOOK LISTING --")
    
    #go through books and print results  
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[1], book[2], book[3]))

#show the 1 location 
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n  -- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))

#validate the user
def validate_user():
    
    try:
        user_id = int(input('\n      Enter a customer id <Example: enter 1 if your id is 1>: '))

        #there are only 3 ids
        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer id. Goodbye.\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid customer id, Goodbye.\n")

        sys.exit(0)

#show the user account menu
def show_account_menu():
    
    try:
        print("\n      --- CUSTOMER MENU ---")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        <Example: Enter 1 to view wishlist>: '))

        return account_option
    except ValueError:
        print("\n  Invalid number. Goodbye.\n")

        sys.exit(0)

#go through database to show wishlist
def show_wishlist(_cursor, _user_id):


    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n        -- DISPLAYING WISHLIST ITEMS --")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

#show books not in the wishlist
def show_books_to_add(_cursor, _user_id):

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n        -- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

#handle MySQL errors
try:

    db = mysql.connector.connect(**config) 

    cursor = db.cursor() # cursor for MySQL queries

    print("\n  Welcome to the WhatABook Application! ")

    user_selection = show_menu() 

    #there are only 
    while user_selection != 4:

        #display books for user 1
        if user_selection == 1:
            show_books(cursor)

        #if the user selects option 2, call the show_locations method and display the configured locations
        if user_selection == 2:
            show_locations(cursor)

        #if the user selects option 3, call the validate_user method to validate the entered user_id 
        #call the show_account_menu() to show the account settings menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            #while account option does not equal 3
            while account_option != 3:

                #if the use selects option 1, call the show_wishlist() method to show the current users 
                #configured wishlist items 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                #if the user selects option 2, call the show_books_to_add function to show the user 
                #the books not in the users wishlist
                if account_option == 2:

                    # how the books not in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    #get the entered book_id 
                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    #add the book to the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() 

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                #only 3 options
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")

                #show account menu 
                account_option = show_account_menu()
        
        #Only 3 options
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please retry...")
            
        #show main menu
        user_selection = show_menu()

    print("\n\n  Program terminated...")

except mysql.connector.Error as err:
    if err.errno ==errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")

    else:
        print(err)

finally:
    db.close()

 