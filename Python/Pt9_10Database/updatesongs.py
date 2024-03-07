from connect import *

def update_songs():
    try:
        # songID is a primary key field
        
        songID = int(input("Enter the songID to update a record: "))
        dbCursor.execute(f"SELECT * FROM songs WHERE songID = {songID}")
        
        # fetchone - fetches a unique(one) record
        row = dbCursor.fetchone()
        # None is a single object to check if a value is present
        if row == None:
            print(f"No record with the songID {songID} exists")
        else:
            fieldname= input("Enter the field (Artist or Title or Genre) ").title()
            fieldValue = input(f"Enter the value for {fieldname}: ")
           
            
           
            dbCursor.execute(f"UPDATE songs SET {fieldname} = ? WHERE SongID = ?",(fieldValue,songID))
            dbCon.commit()
    except sql.OperationalError as e:
            print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
            print(f"Not working because: {pe}")
    finally:
            print("DB operation performed")
if __name__ == "__main__":
        update_songs()
    
        