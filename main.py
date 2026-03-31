from fastapi import FastAPI
import uvicorn
import requests
from bs4 import BeautifulSoup


app = FastAPI()

@app.get("/time")
def get_current_time():
    url= "https://www.horaoficial.cl/"
    response = requests.get(url)
    soup = BeautifulSoup(response.txt, 'html.parser')
    for equisde in soup.find_all("div"):
        print(equisde.getText)
    return {"current_time": "ola"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)