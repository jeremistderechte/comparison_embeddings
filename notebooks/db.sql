CREATE DATABASE emb;

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE raw_text (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL
);

CREATE TABLE model_embeddings (
    id SERIAL PRIMARY KEY,
    embedding VECTOR,
    model_name TEXT NOT NULL,
    embedding_id INT REFERENCES raw_text(id) ON DELETE CASCADE
);
