from fastapi import FastAPI
import uvicorn
import ntplib
import pytz
from datetime import datetime

app = FastAPI()

@app.get("/time")
def get_current_time():
    client= ntplib.NTPClient()
    response= client.request("cl.pool.ntp.org",version=3)
    response.offset
    chile_tz = pytz.timezone('America/Santiago')
    current_time = datetime.fromtimestamp(response.tx_time, chile_tz)
    return {"Año-Mes-Día": f"{current_time.year}-{current_time.month}-{current_time.day}",
            "Hora:Minutos:Segundo": f"{current_time.hour}:{current_time.minute}:{current_time.second}"
            }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    