from fastapi import FastAPI, status, Response
from contextlib import asynccontextmanager
from typing import List
from pydantic import BaseModel
import sqlite3
import json
from mutant import *

DB_PATH = "database.db"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the database
    database_connection = sqlite3.connect(DB_PATH)
    database_connection.execute(
        """CREATE TABLE IF NOT EXISTS dna (id INTEGER PRIMARY KEY AUTOINCREMENT, dna TEXT, mutant INTEGER)""")
    database_connection.execute(
        """CREATE TABLE IF NOT EXISTS stats (id INTEGER PRIMARY KEY AUTOINCREMENT, count_mutant_dna INTEGER DEFAULT 0, 
        count_human_dna INTEGER DEFAULT 0)""")
    database_connection.execute(
        """INSERT INTO stats(count_mutant_dna, count_human_dna) VALUES (0, 0)""")
    app.state.db = database_connection
    yield
    # Close the connection
    database_connection.close()

app = FastAPI(lifespan=lifespan)


class Mutant(BaseModel):
    dna: List[str]


@app.get("/stats")
async def get_stats():
    cursor = app.state.db.execute(
        "SELECT count_mutant_dna, count_human_dna from stats")
    stats = cursor.fetchone()
    if stats[0] != 0 and stats[1] != 0:
        ratio = stats[0] / stats[1]
    else:
        ratio = 0
    return {
        "count_mutant_dna": stats[0],
        "count_human_dna": stats[1],
        "ratio": ratio
    }


@app.post("/mutant", status_code=status.HTTP_200_OK)
async def get_mutant(mutant: Mutant, response: Response):
    app.state.db.execute(
        """INSERT INTO dna(dna) VALUES (?)""", (json.dumps(mutant.dna), ))
    app.state.db.commit()
    if is_mutant(mutant.dna):
        app.state.db.execute(
            """UPDATE stats SET count_mutant_dna = count_mutant_dna + 1 WHERE id = 1""")
        app.state.db.commit()
        return True
    else:
        app.state.db.execute(
            """UPDATE stats SET count_human_dna = count_human_dna + 1 WHERE id = 1""")
        app.state.db.commit()
        response.status_code = status.HTTP_403_FORBIDDEN
