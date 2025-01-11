import sqlite3

con = sqlite3.connect('test1.db')
cur = con.cursor()

# cur.execute("CREATE TABLE user(name, year, title)")
# cur.execute(''' CREATE TABLE exemple1(
#         id INTEGER PRIMARY KEY,
#         name TEXT DEFAULT 'user',
#         age INTEGER DEFAULT 0,
#         title TEXT NOT NULL
#     );''')

# cur.execute(''' INSERT INTO user (name, year, title)
#     VALUES ('Олександра', '2012', 'учениця 7 класу')
#     ;''')

# for i in range(100):
#     cur.execute('''INSERT INTO user (name, year,title)
#             VALUES (?, ?, ?)
#         ''', ('Олександра', i, f'Школяр{i}'))
#     con.commit()

cur.execute("UPDATE user SET name='Тарас' WHERE year=0;")
con.commit()


con.close()
