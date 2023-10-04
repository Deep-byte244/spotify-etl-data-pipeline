import pyodbc
import logging
import pandas as pd

# Define the connection string

def establish_connection():
    try:
        # Create a connection to the SQL Server database
        #Change server and db 
        conn = pyodbc.connect(r'Driver=ODBC Driver 18 for SQL Server;Server=(LocalDB)\MSSQLLocalDB;Database=spotify;Trusted_Connection=yes;')
        logging.info(f"Database connection: Connected")
        return conn
    except Exception as e:
        logging.error(f"Database connection error: {str(e)}")
        raise

def create_songs_table(conn):
    try:
        cursor = conn.cursor()

        # Define the SQL statement to create the "songs" table if it doesn't exist
        create_table_sql = '''
        IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'songs')
        BEGIN
            CREATE TABLE songs (
                song_id VARCHAR(50),
                song_name VARCHAR(255),
                artist_name VARCHAR(255),
                played_at DATETIME,
                date DATE,
                time TIME,
                duration VARCHAR(10),
                context_type INT
            );
        END
        '''

        # Execute the SQL statement to create the table
        cursor.execute(create_table_sql)

        # Commit the changes
        conn.commit()

        logging.info("Table 'songs' created if it didn't exist.")
    except Exception as e:
        logging.error(f"Table creation error: {str(e)}")
        raise

def insert_songs(conn, df):
    try:
        cursor = conn.cursor()
        
        for index, row in df.iterrows():
            song_id = row['song_id']
            song_name = row['song_name']
            artist_name = row['artist_name']
            played_at = row['played_at']
            date = row['date']
            time = row['time']
            duration = row['duration']
            context_type = row['context_type']
            
            # SQL statement to insert a song record
            insert_sql = "INSERT INTO songs (song_id, song_name, artist_name, played_at, date, time, duration, context_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            
            # Execute the SQL statement
            cursor.execute(insert_sql, (song_id, song_name, artist_name, played_at, date, time, duration, context_type))
        
        # Commit the changes
        conn.commit()
        logging.info(f"{len(df)} records inserted successfully.")
        print(f"{len(df)} records inserted successfully.")
    except Exception as e:
        logging.error(f"Insertion error: {str(e)}")
        print(f"Insertion error: {str(e)}")
        raise

def view_songs(conn):
    try:
        cursor = conn.cursor()
        
        # SQL statement to retrieve all records from the "songs" table
        select_sql = "SELECT * FROM songs"
        
        # Execute the SQL statement
        cursor.execute(select_sql)
        
        # Fetch and display the records
        rows = cursor.fetchall()
        if len(rows) == 0:
            print("No songs found.")
        else:
            print("Songs:")
            for row in rows:
                print(f"Song Name: {row.song_name}, Artist Name: {row.artist_name}, Played At: {row.played_at}, Date: {row.date}, Time: {row.time}, Context Type: {row.context_type}")
    except Exception as e:
        logging.error(f"Viewing songs error: {str(e)}")
        print(f"Viewing songs error: {str(e)}")
        raise
