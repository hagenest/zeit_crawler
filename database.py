import sqlite3

# creates a new table (and database if needed)
def create_table():

    # connects cursor to sqlite database
    conn = sqlite3.connect("leitmedien.db")
    c = conn.cursor()

    # creates database table
    c.execute(
        """CREATE TABLE News(
                url TEXT PRIMARY KEY,
                title TEXT,
                newspaper TEXT,
                author TEXT,
                scraped TEXT,
                isPremium INT,
                category TEXT,
                summary TEXT
                )"""
    )

    # closes connection to database
    conn.commit()
    conn.close()


# takes in a tupel with data and inserts it into the table
# remember to enter it in the correct order!
def insert_data(data):

    conn = sqlite3.connect("leitmedien.db")
    c = conn.cursor()

    c.execute(
        """INSERT INTO News(
                url, title, newspaper, author, scraped, isPremium, category, summary)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?)""",
        data,
    )

    conn.commit()
    conn.close()


# gets saved links for specified newspaper
def get_saved_links(newspaper):

    conn = sqlite3.connect("leitmedien.db")
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()

    c.execute("SELECT url FROM News WHERE newspaper IS ?", (newspaper,))
    links = c.fetchall()

    conn.close()

    return links
