import sqlite3

# creates a new Database and table
def create_database():

    # connects cursor to sqlite database
    conn = sqlite3.connect("zeit.db")
    c = conn.cursor()

    # creates database table
    c.execute(
        """CREATE TABLE Zeit(
                url TEXT PRIMARY KEY,
                title TEXT,
                author TEXT,
                scraped TEXT,
                published TEXT,
                isPremium INT,
                category TEXT,
                summary TEXT,
                filename TEXT
                )"""
    )

    # closes connection to database
    conn.commit()
    conn.close()


# takes in a tupel with data and inserts it into the table
# remember to enter it in the correct order!
def insert_data(data):

    conn = sqlite3.connect("zeit.db")
    c = conn.cursor()

    c.execute(
        """INSERT INTO Zeit(
                url, title, author, scraped, published, isPremium, category, summary, filename) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        data,
    )

    conn.commit()
    conn.close()


# DEBUG for testing purposes only
def print_data():

    conn = sqlite3.connect("zeit.db")
    c = conn.cursor()

    c.execute("SELECT * FROM Zeit")
    data = c.fetchall()
    for row in data:
        print(row)

    conn.commit()
    conn.close()


def get_saved_links():

    conn = sqlite3.connect("zeit.db")
    c = conn.cursor()

    c.execute("SELECT url FROM Zeit")
    links = c.fetchall()

    conn.commit()
    conn.close()

    return links
