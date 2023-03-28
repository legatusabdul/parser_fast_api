from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from scraper import PackagePypiParser


templates = Jinja2Templates(directory="templates")


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)

@app.post("/package")
async def package(package: str = Form()):

    scrape = PackagePypiParser(package)        
    scrape.parse()
    scrape.save_to_csv()
    
    file_name = f'{package}.csv'
    file_path = f'output/{file_name}'

    return FileResponse(file_path, media_type='text/csv', filename=file_name)
