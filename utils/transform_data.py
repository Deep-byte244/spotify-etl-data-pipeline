import logging
import pandas as pd



def extract_and_transform_data(data):
    try:
        logging.info("Calling extract_and_transform_data function ")
        
        song_df = None
        song_names = []
        artist_names = []
        played_at_list = []
        date = []
        time = []
        context_type = []
        song_id = []
        song_duration = []

        # Extracting only the relevant bits of data from the JSON object
        for song in data["items"]:
            song_id.append(song["track"]["id"])
            song_names.append(song["track"]["name"])
            artist_names.append(song["track"]["album"]["artists"][0]["name"])
            played_at_list.append(song["played_at"])
            date.append(song["played_at"][0:10])
            time.append(song["played_at"][11:19])
            context_type.append(1 if song["context"] and song["context"]["type"] == "playlist" else 0)
            song_duration.append(song["track"]["duration_ms"])
            
        # Prepare a dictionary to turn it into a Pandas DataFrame
        song_dict = {
            "song_id": song_id,
            "song_name": song_names,
            "artist_name": artist_names,
            "played_at": played_at_list,
            "date": date,
            "time": time,
            "duration": song_duration,
            "context_type": context_type
        }

        song_df = pd.DataFrame(song_dict, columns=["song_id", "song_name", "artist_name", "played_at", "date", "time", "duration", "context_type"])   
        # Log a success message
        logging.info("Data extraction and transformation completed successfully")
        
    except Exception as e:
        # Log the error message
        logging.error(f"Error during data extraction and transformation: {str(e)}")

    return song_df
