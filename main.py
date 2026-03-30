from fastapi import FastAPI
from datetime import datetime
import uvicorn

app = FastAPI()

@app.get("/")
def get_current_time():
    return {"current_time": datetime.now().isoformat()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)