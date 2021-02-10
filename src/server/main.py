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
def connect2db():
    user, db, password, host, port = get_credentials()
    con = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)
    con.close()
    print("Database opened successfully")
    return JSONResponse(
        status_code=200,
        content={
            'info': 'Database opened successfully'
        }
    )

@app.get("/add")
def connect2db():
    user, db, password, host, port = get_credentials()
    con = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)
    cur = con.cursor()
    cur.execute("INSERT INTO RUNRECORD (ID, TOTALTIME, DISTANCE, INTENSITY) VALUES (1, '00:24:32', 10, 8)");
    con.commit()
    con.close()
    return JSONResponse(
        status_code=200,
        content={
            'info': 'Record Added'
        }
    )

@app.get("/createTable")
def connect2db():
    user, db, password, host, port = get_credentials()
    con = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)
    cur = con.cursor()
    cur.execute('''CREATE TABLE RUNRECORD
          (ID INT PRIMARY KEY NOT NULL,
          TOTALTIME TIME NOT NULL,
          DISTANCE INT NOT NULL,
          INTENSITY INT NOT NULL);''')
    con.commit()
    con.close()
    return JSONResponse(
        status_code=200,
        content={
            'info': 'User Added'
        }
    )


