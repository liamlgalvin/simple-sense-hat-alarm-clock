from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from lights import Lights
from mappers import ColourMapper
#from sense_hat import SenseHat
from alarm import Alarm

sense_hat = None #SenseHat()
app = FastAPI()
alarm_time = None
colourMapper = ColourMapper()
lights = Lights(sense_hat)
alarm = Alarm(lights)


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")




# Alarm methods



#controller methods

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,
                                                     "alarm_time": alarm_time, 
            "colour": colourMapper.reverse_map_colour(lights.colour),
            "intensity": lights.intensity,
            "lights_on": lights.lights_on})


@app.post("/set-alarm/{time}")
async def setAlarm(time: float):
    global alarm_time
    #validation 0-23
    if time > 23 or time < 0:
        return {"error": "time must be between 0 - 23"}
        
    alarm_time = time
    return {"message": "alarm set for {}".format(alarm_time)}


@app.delete("/delete-alarm/")
async def removeTime():
    global alarm_time
    alarm_time = None
    return {"message": "alarm deleted"}


@app.post("/inc-intensity/")
async def increment_intensity():
   lights.inc_intensity()

@app.post("/dec-intensity/")
async def decrement_intensity():
   lights.dec_intensity()

@app.post("/inc-intensity/")
async def increment_intensity():
   lights.inc_intensity()

@app.post("/change-colour/{colour}")
async def change_colour_endpoint(colour):
   lights.change_colour(colourMapper.map_colour(colour))

@app.post("/toggle-lights-on/")
async def lights_on_endpoint():
   lights.toggle_lights_on()  


