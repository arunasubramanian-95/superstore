import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()
def get_connection():
    try:
        connection = psycopg2.connect(
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD")
        )
        return connection

    except Exception as e:
        print(f"Connection Failed: {e}")
        return None


if __name__ == "__main__":
        conn = get_connection()
        if conn:
            print("Connection Successful")
            conn.close()