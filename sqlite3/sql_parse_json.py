import sqlite3, json

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

with open('roster_data.json') as fp:
    data = json.load(fp)
    for name, title, role in data:
        print("name = ", name, " title = ", title, " role = ", role)

        # insert User
        cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
        # get user_id
        row = cur.execute('SELECT id FROM User WHERE name = ?', (name,))
        user_id = row.fetchone()[0]
        print("user_id = ", user_id)

        # insert Course
        cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
        # get course_id
        row = cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
        course_id = row.fetchone()[0]
        print("course_id = ", course_id)

        # insert junction table
        cur.execute('INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (user_id, course_id, role))

conn.commit()
