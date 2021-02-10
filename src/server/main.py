from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse
from src.server.utils import get_credentials
from typing import List
from os import path
import sys
import time
import psycopg2
from . import schemas
# from schemas import *
from .config import settings
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

app = FastAPI()

@app.get(
    "/test",
    responses={
        401: {'model': schemas.Unauthorized},
        404: {'model': schemas.AnyError},
    }
)
def test_function():
    a = 1
    return JSONResponse(
        status_code=404,
        content={
            'info': '404'
        }
    )

@app.get("/")
def read_root():
    return 'server is running'

@app.get("/connect")
async def connect2db():
    user, db, password, host, port = get_credentials()
    con = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)
    con.close()
    logging.info("Database opened successfully")
    return JSONResponse(
        status_code=200,
        content={
            'info': 'Database opened successfully'
        }
    )

@app.post("/add")
async def add2db(distance: int, intensity: int, totaltime:str):
    logging.info('Distanec %s, Intensity %s, Time %s' %  (distance, intensity, totaltime))
    user, db, password, host, port = get_credentials()
    con = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)
    cur = con.cursor()
    cur.execute("INSERT INTO RUNRECORD (TOTALTIME, DISTANCE, INTENSITY) VALUES ('%s', %s, %s)"%(totaltime, distance, intensity));
    con.commit()
    con.close()
    return JSONResponse(
        status_code=200,
        content={
            'info': 'Record Added',
            'Distance': distance,
            'Intensity': intensity,
            'Time': totaltime
        }
    )

@app.post("/createTable")
async def createTable():
    user, db, password, host, port = get_credentials()
    con = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)
    cur = con.cursor()
    cur.execute('''CREATE TABLE RUNRECORD
          (ID SERIAL PRIMARY KEY,
          TOTALTIME TIME NOT NULL,
          DISTANCE INT NOT NULL,
          INTENSITY INT NOT NULL);''')
    logging.info("Table created successfully")
    con.commit()
    con.close()
    return JSONResponse(
        status_code=200,
        content={
            'info': 'Table Created'
        }
    )

@app.get("/readAll")
async def readAll():
    user, db, password, host, port = get_credentials()
    con = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)
    cur = con.cursor()
    cur.execute("SELECT json_agg(RUNRECORD)::jsonb FROM RUNRECORD")
    output = cur.fetchall()
    con.close()
    logging.info("Read from table successfully")
    return JSONResponse(
        status_code=200,
        content={
            'info': 'Read database successfully',
             'entry': output
        }
    )

@app.get("/read/intensity")
async def readintensity(level=int):
    user, db, password, host, port = get_credentials()
    con = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)
    cur = con.cursor()
    cur.execute("SELECT json_agg(RUNRECORD)::jsonb FROM RUNRECORD WHERE INTENSITY >= %s"%(level))
    output = cur.fetchall()
    con.close()
    logging.info("Read from table successfully")
    return JSONResponse(
        status_code=200,
        content={
            'info': 'Read database successfully',
             'entry': output
        }
    )

@app.get("/read/distance")
async def readdistance(distance=int):
    user, db, password, host, port = get_credentials()
    con = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)
    cur = con.cursor()
    cur.execute("SELECT json_agg(RUNRECORD)::jsonb FROM RUNRECORD WHERE DISTANCE >= %s"%(distance))
    output = cur.fetchall()
    con.close()
    logging.info("Read from table successfully")
    return JSONResponse(
        status_code=200,
        content={
            'info': 'Read database successfully',
             'entry': output
        }
    )
