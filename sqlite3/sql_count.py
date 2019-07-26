import sqlite3, re

# create table 
conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')

# using local file instead of get data via internet
fp = open("mbox.txt", "r")

for line in fp:
    m_list = re.findall("^From: [a-zA-Z0-9.]+@([a-zA-Z0-9.]+)", line.strip())
    
    if len(m_list) is 0: continue
    
    for org in m_list:
        cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts(org, count) VALUES (?, 1)', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
conn.commit()

ret = cur.execute('SELECT * FROM Counts ORDER BY count DESC LIMIT 10')

for org, count in ret:
    print("org", org, "count", count)
