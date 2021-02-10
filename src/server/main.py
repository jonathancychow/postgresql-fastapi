from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.server.utils import get_credentials
import psycopg2
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

app = FastAPI()
user, db, password, host, port = get_credentials()
con = psycopg2.connect(database=db, user=user,
                       password=password, host=host, port=port)
cur = con.cursor()


@app.get("/")
def read_root():
    return 'server is running'


@app.get("/connect")
async def connect2db():
    user, db, password, host, port = get_credentials()
    con = psycopg2.connect(database=db, user=user,
                           password=password, host=host, port=port)
    con.close()
    logging.info("Database opened successfully")
    return JSONResponse(
        status_code=200,
        content={
            'info': 'Database opened successfully'
        }
    )


@app.post("/add")
async def add2db(distance: int, intensity: int, totaltime: str, date: str):
    logging.info('Distanec %s, Intensity %s, Time %s, Date %s' %
                 (distance, intensity, totaltime, date))
    global cur, con
    cur.execute("INSERT INTO RUNRECORD (TOTALTIME, DISTANCE, INTENSITY, DATE) "
                "VALUES ('%s', %s, %s, %s)"
                % (totaltime, distance, intensity, date))
    con.commit()
    return JSONResponse(
        status_code=200,
        content={
            'info': 'Record Added',
            'Distance': distance,
            'Intensity': intensity,
            'Time': totaltime,
            'Date': date
        }
    )


@app.post("/createTable")
async def createTable():
    global cur, con
    cur.execute('''CREATE TABLE RUNRECORD
          (ID SERIAL PRIMARY KEY,
          TOTALTIME TIME NOT NULL,
          DISTANCE INT NOT NULL,
          INTENSITY INT NOT NULL,
          DATE DATE NOT NULL);''')
    logging.info("Table created successfully")
    con.commit()
    return JSONResponse(
        status_code=200,
        content={
            'info': 'Table Created'
        }
    )


@app.get("/readAll")
async def readAll():
    global cur
    cur.execute("SELECT json_agg(RUNRECORD)::jsonb FROM RUNRECORD")
    output = cur.fetchall()
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
    global cur
    cur.execute("SELECT json_agg(RUNRECORD)::jsonb "
                "FROM RUNRECORD WHERE INTENSITY >= %s GROUP BY INTENSITY" % (level))
    # cur.execute("SELECT * FROM RUNRECORD WHERE intensity <= 10 ORDER BY intensity")
    output = cur.fetchall()
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
    global cur
    cur.execute("SELECT json_agg(RUNRECORD)::jsonb "
                "FROM RUNRECORD WHERE DISTANCE >= %s GROUP BY DISTANCE" % (distance))
    output = cur.fetchall()
    logging.info("Read from table successfully")
    return JSONResponse(
        status_code=200,
        content={
            'info': 'Read database successfully',
            'entry': output
        }
    )


@app.get("/read/time")
async def readtime(time: str = "'24:00:00'"):
    global cur
    cur.execute("SELECT json_agg(RUNRECORD)::jsonb "
                "FROM RUNRECORD WHERE TOTALTIME <= %s GROUP BY TOTALTIME" % (time))
    output = cur.fetchall()
    logging.info("Read from table successfully")
    return JSONResponse(
        status_code=200,
        content={
            'info': 'Read database successfully',
            'Criteria': 'All entry under %s' % time,
            'entry': output
        }
    )
