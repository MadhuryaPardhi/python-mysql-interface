import mysql.connector, pickle
from prettytable import PrettyTable
# Connect to MySQL Database
myconn = mysql.connector.connect(password="<placeholder_password>", user="root", host='localhost')
cursor = myconn.cursor()

def PrintChoices():
    Choices = ['1. TO CREATE A NEW TABLE',
               '2. TO SELECT DATA FROM TABLE',
               '3. TO INSERT DATA INTO TABLE',
               '4. TO UPDATE DATA IN TABLE',    
               '5. TO DELETE DATA FROM TABLE',
               '6. TO DROP A TABLE',
               '7. TO CREATE A DATABASE',
               '8. TO CHANGE THE DATABASE',
               '9. TO DROP A DATABASE',
               '0. Exit.']
    for i in Choices:
        print(i)

def GetColumnHeader(table):
    cursor.execute("DESC " + table)
    var = cursor.fetchall()
    colnames = []
    for i in var:
        colnames.append(i[0])
    return colnames

def CreateTable():
    print("<! CREATING TABLE !>")
    tablename = input("ENTER TABLE NAME ==> ")
    columns = input("COLUMNS (with datatype)(separated with ,) ==>")
    cursor.execute(f"Create table {tablename} ({columns})") 
    print("TABLE CREATED")

def SelectData():
    print("<! SELECTING DATA !>")
    table = input("ENTER TABLE NAME ==> ")
    myTable = PrettyTable(GetColumnHeader(table))
    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall()
    for row in data:
        myTable.add_row(row)
    print(myTable)

def InsertData():
    print("<! INSERTING DATA !>")
    table = input("TABLE NAME ==> ")
    cols = GetColumnHeader(table)
    print("COLUMNS ==> ", end=" ")
    print(*cols, sep=",")
    value = input("ENTER DATA ACCORDING TO COLUMNS ==> ").split(",")  
    query = "INSERT INTO " + table + " VALUES("
    for i in range(len(cols)):
        if value[i].isdigit():
            query += value[i] + ","
        else:
            query += "'" + value[i] + "'" + ","
    query = query[:-1] + ")"
    cursor.execute(query)
    print("DATA INSERTED SUCCESFULLY...")
    myconn.commit()

def UpdateData():
    print("<! UPDATING DATA !>")
    table = input("TABLE NAME ==> ")
    cols = GetColumnHeader(table)
    print("Columns ==> ", end=" ")
    print(*cols, sep=",")
    updtc = input("COLUMN TO UPDATE ==> ")
    updtv = input("UPDATED VALUE ==> ")
    condc = input("COLUMN TO BE USED FOR SEARCH ==> ")
    condv = input("VALUE TO BE SEARCHED ==> ")
    updtv = updtv if updtv.isdigit() else "'" + updtv + "'"
    condv = condv if condv.isdigit() else "'" + condv + "'"
    cursor.execute("UPDATE "+table+" SET "+updtc+" = "+updtv+" WHERE "+condc+" = "+condv)
    myconn.commit()
    print("Updated Data Successfully...")

def DeleteData():
    print("<! DELETING DATA !>")
    table = input("TABLE NAME ==> ")
    cols = GetColumnHeader(table)
    print("Columns ==> ", end=" ")
    print(*cols, sep=",")
    col = input("COLUMN TO BE SEARCHED ==> ")
    value = input("VALUE TO BE SEARCHED ==> ")
    value = value if value.isdigit() else "'" + value + "'"
    cursor.execute("DELETE FROM " + table + " WHERE " + col + " = " + value)
    myconn.commit()
    print("DELETED DATA SUCCESSFULLY...")

def DropTable():
    print("<! DROPPING TABLE !>")
    cursor.execute("DROP TABLE " + input("TABLE NAME ==> "))
    print("Dropped Table Successfully...")

def CreateDB():
    print("<! CREATING DATABASE !>")
    global CURR_DB
    DB = input("DATABASE ==>").strip()
    PS = input("PASSWORD ==>").strip()
    AVAL_DB[DB] = PS
    cursor.execute("CREATE DATABASE " + DB)
    UpdateFile(AVAL_DB)
    CURR_DB = ChooseDB(AVAL_DB)

def GetDB():
    try:
        with open('dbs.bin', 'rb') as F:
            AVAL_DB = pickle.load(F)
            return AVAL_DB
    except FileNotFoundError:
        print("<!NO DATABASE FOUND IN THE RECORD!>\n<!PLEASE USE GUEST TO CREATE YOUR DATABASE !>")
        with open("dbs.bin", "wb") as F:
            pickle.dump({"GUEST": ""}, F)
            cursor.execute("CREATE DATABASE IF NOT EXISTS GUEST")
        return {"GUEST": ""}

def ChooseDB(AVAL_DB):
    print("\n<! SELECT A DATABASE !>")
    print("AVAILABLE DATABASES ==> ", [i for i in AVAL_DB])
    DB = input("DATABASE ==> ")
    if DB in AVAL_DB:
        if DB.lower() == "guest":
            return DB
        else:
            PS = input("PASSWORD ==> ")
            if CheckPassword(DB, PS):
                return DB
            else:
                print("<! ACCESS DENIED !>\n<! TRY AGAIN!>\n")
                ChooseDB(AVAL_DB)
    else:
        print("<! NO SUCH DATABASE IN RECORD !>")
        ChooseDB(AVAL_DB)

def DropDatabase():
    print("<! DROPPING DATABASE !>")
    global CURR_DB
    if CURR_DB.lower() == "guest":
        print("<! CANNOT DELETE THIS DATABASE !>")
    else:
        print("<! Deleting Current Database !>")
        PS = input("Enter Password to Confirm ==> ")
        if CheckPassword(CURR_DB, PS):
            del AVAL_DB[CURR_DB]
            cursor.execute("DROP DATABASE " + CURR_DB)
            print("<! DATABASE DROPPED !>\n")
            UpdateFile(AVAL_DB)
            CURR_DB = ChooseDB(AVAL_DB)
            cursor.execute("USE " + CURR_DB)
        else:
            print("<! INVALID PASSWORD !>\n<! OPERATION DENIED !>")

def CheckPassword(DB, PS):
    if DB in AVAL_DB and AVAL_DB[DB] == PS:
        return True
    else:
        return False

def UpdateFile(AVAL_DB): 
    with open('dbs.bin', 'wb') as F:
        pickle.dump(AVAL_DB, F)

AVAL_DB = GetDB()
CURR_DB = ChooseDB(AVAL_DB)
cursor.execute('USE ' + CURR_DB)

while True:
    try: 
        print(f"\n<CURRENT DATABSE : {CURR_DB}>\n")
        choice = input("Enter your choice <Enter O to see Options> :")

        if choice == "O" or choice == "o":
            PrintChoices()    
        elif choice == "1":
            CreateTable()
        elif choice == "2":
            SelectData()
        elif choice == "3":
            InsertData()
        elif choice == "4":
            UpdateData()
        elif choice == "5":
            DeleteData()
        elif choice == "6":
            DropTable()
        elif choice == "7":
            CreateDB()     
        elif choice == "8":
            CURR_DB = ChooseDB(AVAL_DB)
            cursor.execute("USE " + CURR_DB)
        elif choice == "9":
            DropDatabase()       
        elif choice == "0":
            break
        else:
            print("<!  INVALID CHOICE !>")
    except Exception as E:
        print("ERROR:",E)