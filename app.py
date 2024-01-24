import uvicorn
from fastapi import FastAPI

from scraper import Scraper

app = FastAPI()

@app.get("/")
def main():
    return ({"Server": "Running"})

@app.get("/ip")
def get_ip():
    scraper = Scraper()
    ip_address = scraper.ip()
    return ({"ip": ip_address})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)