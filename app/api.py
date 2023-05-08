from fastapi.responses import HTMLResponse

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from starlette.responses import RedirectResponse

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    
    # return RedirectResponse(url='/docs')    

@app.get("/images/{image}")
async def serve_image(image: str) -> dict:
    img = "static/images/"+image
    return FileResponse(img)

@app.get("/users/{image}")
async def serve_image(image: str) -> dict:
    img = "static/users/"+image
    return FileResponse(img)
                
@app.get("/products/{image}")
async def serve_image(image: str) -> dict:
    img = "static/products/"+image
    return FileResponse(img)