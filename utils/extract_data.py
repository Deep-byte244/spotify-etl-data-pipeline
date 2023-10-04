import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure logging
logging.basicConfig(filename='spotify_etl.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_token(client_id, client_secret, redirect_uri, username, password):
    try:
        logging.info("Start Process call get_token function ")
        # Set up the Chrome WebDriver
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Enable headless mode
        # Create a WebDriver instance with the Chrome options
        driver = webdriver.Chrome(options=chrome_options)
        # Navigate to the Spotify authorization URL with the appropriate scope
        auth_url = f'https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope=user-read-recently-played'
        driver.get(auth_url)

        # Wait for the user to authorize the app
        time.sleep(10)

        # Find and interact with the login elements
        username_element = driver.find_element(By.ID, 'login-username')
        password_element = driver.find_element(By.ID, 'login-password')
        login_button = driver.find_element(By.ID, 'login-button')

        # Send username and password keys (text input) to the elements
        username_element.send_keys(username)
        password_element.send_keys(password)

        # Click the login button
        login_button.click()

        time.sleep(10)  # Wait for the authorization code to appear in the URL

        # Get the current URL (which should contain the authorization code)
        current_url = driver.current_url
        authorization_code = current_url.split('code=')[1]

        # Close the browser
        driver.quit()

        # Use the authorization code to obtain an access token
        sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
        token_info = sp_oauth.get_access_token(authorization_code)

        # Use the obtained access token to make API requests
        sp = spotipy.Spotify(auth=token_info['access_token'])
        recently_played = sp.current_user_recently_played()

        return recently_played  # You can modify this to return any data you need

    except Exception as e:
        # Log any exceptions that occur during the process
        logging.error(f"Error in authentication process: {str(e)}")
        return None
