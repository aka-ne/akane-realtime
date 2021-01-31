from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from tinydb import TinyDB 
import json

# uncomment for deta support
#from db import *

# tinydb setup
db1 = TinyDB('db.json')

#FastAPI instance

app = FastAPI(
  title="Tracking",
    description="Tracking de buses",
    version="0.0.1",)

#Static files mount
app.mount("/static", StaticFiles(directory="static"), name="static")

#Templates Folder
templates = Jinja2Templates(directory="templates")

#Hellow wolrd endpoint
@app.get("/")
async def index():
    return {"hola":"mundo"}

#GPS real time data endpoint

@app.get('/deta1')
async def deta():
    resultado = db1.all()
    for item in resultado:
      lat = item['lat']
      lon = item['lon']
    return {"geometry": {"type": "Point", "coordinates": [lon, lat]}, "type": "Feature", "properties": {}}

# Uncomment for deta support
# @app.get('/deta')
# async def deta():
#     resultado = next(db.fetch())
#     for item in resultado:
#       lat = item['lat']
#       lon = item['lon']
#     return {"geometry": {"type": "Point", "coordinates": [lon, lat]}, "type": "Feature", "properties": {}}

#MapBox template
@app.get("/map", response_class=HTMLResponse, include_in_schema=False)
async def map(request: Request):
    return templates.TemplateResponse("mbox.html",{"request":request})


