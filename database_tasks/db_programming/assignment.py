# Create a script that
# 1. Reads contents of the files users.csv, purchases.csv and purchaseParts.csv
# 2. Creates a new database called purchases.db
# 3. Creates tables for each of the csv files called: users, purchases and purchaseParts
# 4. Inserts the data for each of the tables
# 5. Finally, join data from all the 3 tables and print it all out. Order the data by "users.email" ascending.
#    Expected output should be like this:
#      (3, 'danny@boy.com', 1, 3, 1, 1, 'Poster')
#      (3, 'danny@boy.com', 2, 3, 2, 2, 'Nail Clipper')
#      (5, 'f51wt@mymail.com', 4, 5, 5, 4, 'Monitor')
#      (5, 'f51wt@mymail.com', 4, 5, 6, 4, 'Keyboard')
#      (2, 'my@mail.com', 3, 2, 3, 3, 'Laptop')
#      (2, 'my@mail.com', 3, 2, 4, 3, 'Monitor')

# Note that the CSV files contains the data format and constraints inside the title.

# Other requirements:
# You need to dynamically create the tables and their content. You CANNOT just do if statements to check for name of the file and then create the table and insert the data manually.
# You NEED to write the script yourself, you cannot use any pre-created library other than sqlite3
# You need to create a function called dropAndCreateTable that accepts the name of the table and table fields in some format. That function needs to drop the table first if it exists (DROP TABLE IF EXISTS tableName) and then needs to create the passed table with the fields given. Note that neither of the DROP TABLE or CREATE TABLE commands work with the ? substitution.
# You need to create a function called insertData that accepts the name of the table and table data in some format. That function needs to insert the passed data into the given table.

import sqlite3

database = "purchase.db"
connection = sqlite3.connect(database)
cursor = connection.cursor()

filenames = ["users.csv" , "purchases.csv", "purchaseParts.csv"]

def dropAndCreateTable(tablename, fields):
    print("dropandcreate")

def insertData(tableName, data):
    print("insertdata")

# Open the files for reading/loop trough the files one by one
# name of the file(excluding .csv) is your table name
# First line of the file? That's your table creation over dropAndCreateTable
# Any other line of the file? That's data for your table! insertData