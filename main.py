from fastapi import FastAPI
import uvicorn
import ntplib

app = FastAPI()
client = ntplib.NTPClient.request("")

@app.get("/time")
def get_current_time():
    return {"current_time": }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)