from mutant import *
from fastapi import FastAPI, status, Response
from contextlib import asynccontextmanager
from typing import List
from pydantic import BaseModel
import json
import databases
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select


DB_PATH = "database.db"
DATABASE_URL = "postgresql://default:WahU5oSNL3pK@ep-solitary-sound-a4cexntd-pooler.us-east-1.aws.neon.tech:5432/verceldb"
database = databases.Database(DATABASE_URL)
Base = declarative_base()


class Dna(Base):
    __tablename__ = 'dna'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dna = Column(String, nullable=False)


class Stats(Base):
    __tablename__ = 'stats'
    id = Column(Integer, primary_key=True, autoincrement=True)
    count_mutant_dna = Column(Integer, default=0)
    count_human_dna = Column(Integer, default=0)


engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the database
    await database.connect()
    query = "SELECT COUNT(*) FROM stats"
    result = await database.fetch_one(query)
    if result[0] == 0:
        # Insert default stats if table is empty
        query = "INSERT INTO stats(count_mutant_dna, count_human_dna) VALUES (0, 0)"
        await database.execute(query)

    yield
    # Close the connection
    await database.disconnect()

app = FastAPI(lifespan=lifespan)


class Mutant(BaseModel):
    dna: List[str]


@app.get("/stats")
async def get_stats():
    await database.connect()
    query = "SELECT count_mutant_dna, count_human_dna FROM stats WHERE id = 1"
    stats = await database.fetch_one(query)
    await database.disconnect()
    if stats['count_human_dna'] != 0:
        ratio = stats['count_mutant_dna'] / stats['count_human_dna']
    else:
        ratio = stats['count_mutant_dna']
    return {
        "count_mutant_dna": stats['count_mutant_dna'],
        "count_human_dna": stats['count_human_dna'],
        "ratio": "{:.1f}".format(ratio) # return only one decimal
    }


@app.post("/mutant", status_code=status.HTTP_200_OK)
async def get_mutant(mutant: Mutant, response: Response):
    await database.connect()
    dna = json.dumps(mutant.dna)
    query = "INSERT INTO dna(dna) VALUES (:dna)"
    await database.execute(query, values={"dna": dna})
    
    if is_mutant(mutant.dna):
        query = "UPDATE stats SET count_mutant_dna = count_mutant_dna + 1 WHERE id = 1"
        await database.execute(query)
        await database.disconnect()
        return True
    else:
        query = "UPDATE stats SET count_human_dna = count_human_dna + 1 WHERE id = 1"
        await database.execute(query)
        response.status_code = status.HTTP_403_FORBIDDEN
        await database.disconnect()
