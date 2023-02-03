
import json
import http
import sqlite3
import sys
import ssl
import time
import urllib.request, urllib.parse, urllib.error

api_key = False

if api_key is False:
    serviceurl = ""
else:
    serviceurl = ""

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode= ssl.CERT_NONE

fh = open("where.data")
count = 0
for line in fh:
    if count > 200:
        print('Retrieved 200 locations, restart to retrieve more')
        break
    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address = ?",
                (memoryview(address.encode()),))
    
    try:
        data = cur.fetchone()[0]
        print("Found in database", address)
        continue
    except:
        pass

    






# conn = sqlite3.connect('rosterdb.sqlite')
# cur = conn.cursor()

# # Do some setup
# cur.executescript('''
# DROP TABLE IF EXISTS User;
# DROP TABLE IF EXISTS Member;
# DROP TABLE IF EXISTS Course;

# CREATE TABLE User (
#     id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name   TEXT UNIQUE
# );

# CREATE TABLE Course (
#     id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     title  TEXT UNIQUE
# );

# CREATE TABLE Member (
#     user_id     INTEGER,
#     course_id   INTEGER,
#     role        INTEGER,
#     PRIMARY KEY (user_id, course_id)
# )
# ''')

# fname = input('Enter file name: ')
# if ( len(fname) < 1 ) : fname = 'roster_data.json'

# # [
# #   [ "Charley", "si110", 1 ],
# #   [ "Mea", "si110", 0 ],

# str_data = open(fname).read()
# json_data = json.loads(str_data)

# for entry in json_data:

#     name = entry[0];
#     title = entry[1];
#     role_id = entry[2];

#     #print name, title

#     cur.execute('''INSERT OR IGNORE INTO User (name) 
#         VALUES ( ? )''', ( name, ) )
#     cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
#     user_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR IGNORE INTO Course (title) 
#         VALUES ( ? )''', ( title, ) )
#     cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
#     course_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR REPLACE INTO Member
#         (user_id, course_id, role) VALUES ( ?, ? ,? )''', 
#         ( user_id, course_id, role_id) )

# conn.commit()

# cur.executescript('''
#     SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
#     User JOIN Member JOIN Course 
#     ON User.id = Member.user_id AND Member.course_id = Course.id
#     ORDER BY X
# ''')
