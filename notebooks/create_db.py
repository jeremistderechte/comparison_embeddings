import psycopg2
from psycopg2 import sql
from config import settings


def create_tables() -> None:
    db_host = settings.host_ip
    db_user = settings.user_name
    db_password = settings.password
    db_port = settings.host_port
    db_name = settings.db_name

    try:
        conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS model_embeddings CASCADE")
        cursor.execute("DROP TABLE IF EXISTS raw_text CASCADE")

        cursor.execute("CREATE EXTENSION IF NOT EXISTS vector")

        cursor.execute(
            """
            CREATE TABLE raw_text (
                id SERIAL PRIMARY KEY,
                text TEXT NOT NULL
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE model_embeddings (
                id SERIAL PRIMARY KEY,
                embedding vector,
                model_name TEXT NOT NULL,
                embedding_id INT REFERENCES raw_text(id) ON DELETE CASCADE
            )
            """
        )

        conn.commit()
        cursor.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
