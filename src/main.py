from typing import Optional
from fastapi import FastAPI, Request, Header, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.session import engine, get_db
from db.base import Base
from sqlalchemy.orm import Session
from db.models.salons import Salon
from db.models.hours import Hour
from db.models.amenities import Amenities
from db.models.services import Services

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/index/', response_class=HTMLResponse)
def index(request: Request, hx_request: Optional[str] =  Header(None), db: Session = Depends(get_db)):
    # salons = [{'name': 'test', 'rating': 4, 'budget': '1-10', 'website': 'http', 'phone': '408', 'address': '123'}]
    salons = db.query(Salon).all()
    context = {'request': request, 'salons': salons}
    if hx_request:
        return templates.TemplateResponse("components/table.html", context)
    return templates.TemplateResponse("index.html", context)

