import sqlite3, re
import xml.etree.ElementTree as ET

"""
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
"""

class MyTracker:
    conn, cur = None, None
    def __init__(self, SQLITE_DB_NAME = "test.sqlite"):
        # create table 
        self.conn = sqlite3.connect(SQLITE_DB_NAME)
        self.cur = self.conn.cursor()

    def clearTable(self):
        self.cur.execute('DROP TABLE IF EXISTS Artist')
        self.cur.execute('DROP TABLE IF EXISTS Genre')
        self.cur.execute('DROP TABLE IF EXISTS Album')
        self.cur.execute('DROP TABLE IF EXISTS Track')
    
    def createTable(self):
        self.cur.execute('''CREATE TABLE Artist (
                id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name    TEXT UNIQUE
            );''')
        self.cur.execute('''CREATE TABLE Genre (
                id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name    TEXT UNIQUE
            );''')
        self.cur.execute('''CREATE TABLE Album (
                id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                artist_id  INTEGER,
                title   TEXT UNIQUE
            );''')
        self.cur.execute('''CREATE TABLE Track (
                id  INTEGER NOT NULL PRIMARY KEY 
                    AUTOINCREMENT UNIQUE,
                title TEXT  UNIQUE,
                album_id  INTEGER,
                genre_id  INTEGER,
                len INTEGER, rating INTEGER, count INTEGER
            );''')
    
    def lookup(self, d, key):
        found = False
        for child in d:
            if found : return child.text
            if child.tag == 'key' and child.text == key :
                found = True
        return None
        
    def parseLibrary(self, FILE_NAME = 'Library.xml'):
        stuff = ET.parse(FILE_NAME)
        all = stuff.findall('dict/dict/dict')
        print('Dict count:', len(all))
        for entry in all:
            if self.lookup(entry, 'Track ID') is None: continue

            name = self.lookup(entry, 'Name')
            artist = self.lookup(entry, 'Artist')
            album = self.lookup(entry, 'Album')
            count = self.lookup(entry, 'Play Count')
            genre = self.lookup(entry, 'Genre')
            rating = self.lookup(entry, 'Rating')
            length = self.lookup(entry, 'Total Time')

            if name is None or artist is None or album is None or genre is None: 
                continue
            print(name, artist, album, genre, count, rating, length)
            
            # insert into artist
            self.cur.execute('''INSERT OR IGNORE INTO Artist (name) 
                VALUES ( ? )''', ( artist, ) )
            self.cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
            artist_id = self.cur.fetchone()[0]

            # insert into genre
            self.cur.execute('''INSERT OR IGNORE INTO Genre (name) 
                VALUES ( ? )''', ( genre, ) )
            self.cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
            genre_id = self.cur.fetchone()[0]

            # insert album
            self.cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
                VALUES ( ?, ? )''', ( album, artist_id ) )
            self.cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
            album_id = self.cur.fetchone()[0]

            # insert track
            self.cur.execute('''INSERT OR REPLACE INTO Track
                (title, album_id, genre_id, len, rating, count) 
                VALUES ( ?, ?, ?, ?, ?, ? )''', 
                ( name, album_id, genre_id, length, rating, count ) )

            # commit change
            self.conn.commit()
        
if __name__ == '__main__':
    mt = MyTracker()
    mt.clearTable()
    mt.createTable()
    mt.parseLibrary()
