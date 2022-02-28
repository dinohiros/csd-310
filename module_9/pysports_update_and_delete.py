import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "BbbdGTR2022$",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

#method for inner join on player and team tables, go though the data and print results 
def show_players(cursor, title):

    # inner join 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get the results from the cursor object 
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    # iterate over the player data set and display the results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

# try block to handle MySQL errors 
try:
    db = mysql.connector.connect(**config) 

    #get the cursor object
    cursor = db.cursor()

    #insert player query 
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    #player data fields 
    player_data = ("Smeagol", "Shire Folk", 1)

    #insert a new player record
    cursor.execute(add_player, player_data)

    #commit the insert
    db.commit()

    #show all records in the player table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    #update the new player 
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    #execute update
    cursor.execute(update_player)

    #show all records in the player table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    #delete query 
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(delete_player)

    #show all records in the player table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue... ")

#handle errors
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
