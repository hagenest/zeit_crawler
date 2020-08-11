import sqlite3

# creates a new Database and table. has an optional debugging mode
def create_database(is_debug_mode):

    # connects cursor to sqlite database
    conn = sqlite3.connect("zeit.db")
    c = conn.cursor()

    # changes the output to dictionaries instead of lists
    conn.row_factory = sqlite3.Row

    # Drops table in debug mode
    if is_debug_mode == True:
        c.execute("DROP TABLE IF EXISTS Zeit")

    # creates database table
    c.execute(
        """CREATE TABLE Zeit(
                url TEXT,
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

    # writes test data and prints it if in debug mode
    if is_debug_mode == True:
        testData = (
            "www.zeit.de/test",
            "Test-Artikel",
            "Mr. WasgehtSiedasan",
            "published time" "2020-08-11 13:37:00",
            0,
            "Gesellschaft",
            "test summary",
            "Test-Artikel.txt",
        )
        insert_data(testData)
        print_data()


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


def get_safed_links():

    conn = sqlite3.connect("zeit.db")
    c = conn.cursor()

    conn.row_factory = sqlite3.Row

    c.execute("SELECT url FROM Zeit")
    links = c.fetchall()

    conn.commit()
    conn.close()

    return links
