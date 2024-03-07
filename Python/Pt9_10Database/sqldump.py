from connect import *
from readsongs import *
 
def dump_data():
    # open the file
    with open("Python/Pt9_10Database/songs.sql") as dumpfile:
        # read the open file(dumpfile) and save it contents to sqlInsertScript variable
        sqlInsertScript = dumpfile.read()
 
        # write the content found/stored in the sqlInsertScript variable
        dbCursor.executescript(sqlInsertScript)
        # now call the all_songs function from the readsongs file to display updated records
        all_songs()
 
dump_data()
     