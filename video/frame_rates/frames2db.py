import psycopg2
import os

def insert_frames_into_db(frames, timestamps, video_filename):
    # Database connection parameters
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')

    # Connect to the database
    conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = conn.cursor()

    # SQL query to insert a frame
    insert_query = """
    INSERT INTO video_frames (video_filename, frame_data, timestamp) 
    VALUES (%s, %s, %s);
    """

    # Insert each frame and its timestamp into the database
    for frame, timestamp in zip(frames, timestamps):
        cursor.execute(insert_query, (video_filename, frame, timestamp))

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

# Now, call this function where you need it, for example, after capturing frames:
# insert_frames_into_db(base64_frames, timestamps, video_filename)
