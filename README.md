
# Spotify ETL Data Pipeline

The Spotify ETL (Extract, Transform, Load) data pipeline project is a testament to the power of data engineering—a journey filled with challenges, solutions, and insights. This pipeline extracts listening history data from Spotify, transforms it into a structured format, and loads it into a SQL Server database for analysis. Whether you're an experienced data engineer or someone curious about ETL pipelines, this project demonstrates the endless possibilities that lie in building robust data pipelines.

## Libraries

To run this project, you'll need to install the following Python libraries using `pip`:

- `selenium`
- `spotipy`
- `pandas`
- `pyodbc`
- `python-dotenv`

You can install them using the following commands:

```bash
pip install selenium
pip install spotipy
pip install pandas
pip install pyodbc
pip install python-dotenv
```

## Configuration

Before you start, make sure to create a `.env` file in the project directory with the following variables:

```dotenv
client_id = 'YOUR_SPOTIFY_CLIENT_ID'
client_secret = 'YOUR_SPOTIFY_CLIENT_SECRET'
EMAIL = 'YOUR_EMAIL'
PASSWORD = 'YOUR_PASSWORD'
redirect_uri = 'http://localhost:5000/callback'
```

Set the `redirect_uri` to match the Redirect URI you've configured in your Spotify Developer Dashboard.

![Screenshot 1](https://github.com/Deep-byte244/spotify-etl-data-pipeline/assets/78338569/7972080a-a0eb-458d-afa3-4a5ae3814a65)

## Database Configuration

To configure the database, replace the credentials in the appropriate section of your code.

## Running the Script

You can run the script manually by executing it as you would with any Python script. However, if you want to schedule it to run automatically at specific intervals, follow these steps:

### Scheduling with Windows Task Scheduler

1. **Open Task Scheduler**: Press `Win + R`, type `taskschd.msc`, and press Enter. This will open the Task Scheduler.

2. **Create a Basic Task**: In the right-hand panel, click on "Create Basic Task..." to launch the Create Basic Task Wizard.

3. **Name and Description**: Give your task a name and an optional description. Click "Next."

4. **Trigger**: Choose the trigger that specifies when the task should run. You can select options like "Daily," "Weekly," or "Monthly" to set a schedule. Follow the wizard to configure the trigger settings (e.g., start time, recurring days).

5. **Action**: Select "Start a program" as the action to perform. Click "Next."

6. **Program/script**: Browse and select the Python executable. This is typically located in the `C:\Users\<YourUsername>\AppData\Local\Programs\Python\<PythonVersion>` folder. Choose the `python.exe` file.

7. **Add arguments (optional)**: If your Python script requires any command-line arguments, you can enter them in this field. For example, if your script is `etl-pipeline.py`, enter `etl-pipeline.py`.

8. **Start in (optional)**: If your script relies on a specific working directory, specify it here like `D:\Data science\Spotify-etl\`. Otherwise, you can leave it blank.

9. **Finish**: Review the summary of your task and click "Finish" to create the scheduled task.

10. **Authorization**: You may be prompted to enter your Windows user account credentials. Make sure to provide the correct username and password.

11. **Verification**: After completing the wizard, you should see your task listed in the Task Scheduler Library. You can right-click on it and select "Run" to test it immediately.

12. **Edit or Further Configuration**: If needed, you can go back to the Task Scheduler, find your task, right-click, and select "Properties" to make changes or configure advanced settings like user account permissions, triggers, or actions.

Your Python script will now run based on the schedule you defined in the Task Scheduler.

Please note that for this to work, your Python script should be designed to execute without any manual interaction, as it will run in the background according to the schedule you've set.

## Screenshots

Here are some screenshots of the project:

For database configuration:

![Screenshot 2](https://github.com/Deep-byte244/spotify-etl-data-pipeline/assets/78338569/5c192cc6-b940-4ddb-ac52-0717b09acde9)

## Logs Maintenance

It's essential to maintain logs to track the execution of your ETL pipeline. You can implement logging in your Python script using Python's `logging` module. Create log files to record important events, errors, or information related to your ETL process.

Example log maintenance code snippet:

```python
import logging

# Configure the logging module
logging.basicConfig(filename='etl_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Log information
logging.info('ETL pipeline started.')

# Log errors
try:
    # Your ETL code here
except Exception as e:
    logging.error(f'An error occurred: {str(e)}')

# Log completion
logging.info('ETL pipeline completed.')
```
## Contact

- LinkedIn: [Deepkumar Patel](https://www.linkedin.com/in/deepkumar-patel05/)
- Kaggle: [deeppatel9095](https://www.kaggle.com/deeppatel9095/)
- medium: [@learnwithdeep](https://medium.com/@learnwithdeep/building-a-robust-spotify-etl-pipeline-a-data-engineering-journey-d5703eaecde8)
  

Feel free to reach out if you have any questions or suggestions. Enjoy exploring the world of data engineering with this Spotify ETL data pipeline project!
