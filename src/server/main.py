from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse
from typing import List
from os import path
import sys
import time
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


