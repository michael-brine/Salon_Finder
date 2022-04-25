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
_budget, budgets = 1, {1: '1-10', 2: '11-30', 3: '31-50'}
app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
def index(request: Request, hx_request: Optional[str] =  Header(None), db: Session = Depends(get_db)):
    #salons = [{'name': 'test', 'rating': 4, 'budget': '1-10', 'website': 'http', 'phone': '408', 'address': '123'}]
    salons = show_all_salons(db)
    context = {'request': request, 'salons': salons}
    if hx_request:
        return templates.TemplateResponse("components/table.html", context)
    return templates.TemplateResponse("index.html", context)

def show_all_salons(db):
    return db.query(Salon).all()

@app.get('/budget/')
def budget():
    return add_budget()

def add_budget():
    _budget = _budget + 1 if _budget != 4 else 1
    return '$' * _budget
# @app.get('/service/')
# def budget(budget_int):
#     # budget = budget_int
#     return budget

@app.get('/query', response_class=HTMLResponse)
def query(request: Request, hx_request: Optional[str] =  Header(None), db: Session = Depends(get_db)):
    output = db.query(Salon)
    if budget is int:
        output = output.filter(Salon.budget == budgets[1])

    context = {'request': request, 'salons': output}
    if hx_request:
        return templates.TemplateResponse("components/table.html", context)
    return templates.TemplateResponse("index.html", context)
