import logging
from utils.extract_data import get_token
from utils.transform_data import extract_and_transform_data
from utils.load_data import establish_connection, create_songs_table, insert_songs, view_songs
from dotenv import load_dotenv
import os
from datetime import datetime



# Configure logging
logging.basicConfig(filename='etl.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Load environment variables from .env file
    load_dotenv()

    # Define your Spotify API credentials and other parameters
    client_id=os.environ.get('client_id')
    client_secret=os.environ.get('client_secret')
    USER=os.environ.get('EMAIL')
    PASS=os.environ.get('PASSWORD')
    redirect_uri=os.getenv('redirect_uri')
    
    # Extract and transform data from Spotify
    print('--------START----------')
    recently_played_data = get_token(client_id, client_secret, redirect_uri, USER, PASS)
    df = extract_and_transform_data(recently_played_data)
    current_date = datetime.now().strftime('%Y-%m-%d')
    filename = f'data/raw/data_{current_date}.csv'
    df.to_csv(filename, index=False)
    conn = establish_connection()
    create_songs_table(conn)
    insert_songs(conn, df)
    view_songs(conn)
    conn.close()
    print('---------END----------')

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
