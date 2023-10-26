from fastapi import FastAPI, Request, Response, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

def delete_image(path):
    if os.path.exists(path):
        os.remove(path)
@app.post("/upload/")
async def upload_file(file: UploadFile):
    # ファイルを保存する場合
    path="./static/face/"+file.filename
    with open(path, "wb") as f:
        f.write(file.file.read())
    return {"filename": file.filename}
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("edit.html", {
        "request": request
    })
@app.get("/face/{image_path}")
def image(image_path: str):
    path="./static/face/"+image_path
    with open(path, "rb") as f:
        face=f.read()
        delete_image(path)
        return Response(content=face, media_type="image/png")
@app.get("/back/{pas}")
def image(pas: str):
    with open("./static/back/"+pas, "rb") as f:
        return Response(content=f.read(), media_type="image/png")

@app.get("/upload")
async def index(request: Request):
    return templates.TemplateResponse("upload.html", {
        "request": request
    })

@app.get("/dele/{pas}")
async def image(pas: str,request: Request):
    os.remove("./static/face/"+pas)
    return templates.TemplateResponse("finish.html", {
        "request": request
    })