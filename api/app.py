from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from endpoints.process_move import process_move, router

app = FastAPI()
templates = Jinja2Templates(directory="../templates")
app.include_router(router)
app.mount("/static", StaticFiles(directory="../templates/static"), name="static")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})