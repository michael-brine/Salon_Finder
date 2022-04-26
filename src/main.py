from turtle import color
from typing import Optional
from fastapi import FastAPI, Request, Header, Depends
from fastapi.staticfiles import StaticFiles
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
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
def index(request: Request, hx_request: Optional[str] =  Header(None), db: Session = Depends(get_db)):
    salons = db.query(Salon, Hour.open_time, Hour.close_time).filter(Hour.day == 2).join(Hour, Salon.salon_id == Hour.salon_id).all()
    context = {'request': request, 'salons': salons}
    if hx_request:
        return templates.TemplateResponse("components/table.html", context)
    return templates.TemplateResponse("index.html", context)


@app.get('/query',)
def query(budget, days, request: Request, hx_request: Optional[str] =  Header(None), db: Session = Depends(get_db),
 coloring='off', blowout='off', hair_treatment='off', kids_haircut='off', bridal_service='off', hair_extension='off',
 hairsyling='off', makeup='off', mens_haircut='off', womens_haircut='off', mask_required='off', accepts_card='off',
 accepts_andriod='off', accepts_apple='off', good_for_kids='off', car_parking='off', bike_parking='off', free_wifi='off',
 wheelchair_access='off', restrooms='off', appointments='off'):

    budgets = {'0': '1-10', '1': '11-30', '2': '31-50'}
    service_names = ['coloring', 'blowout', 'hair_treatment', 'kids_haircut', 'bridal_service', 'hair_extension',
    'hairsyling', 'makeup', 'mens_haircut', 'womens_haircut',]
    amenties_names = ['mask_required', 'accepts_card',
    'accepts_andriod', 'accepts_apple', 'good_for_kids', 'car_parking', 'bike_parking', 'free_wifi',
    'wheelchair_access', 'restrooms', 'appointments']

    l = locals()

    q = db.query(Salon, Hour.open_time, Hour.close_time)
    q = dynamic_filter(q, make_filters(service_names, l), Services)
    q = dynamic_filter(q, make_filters(amenties_names, l), Amenities)
    q = q.filter(Salon.budget == budgets[budget]).filter(Hour.day == int(days))\
    .join(Services, Salon.salon_id == Services.salon_id)\
    .join(Amenities, Salon.salon_id == Amenities.salon_id)\
    .join(Hour, Salon.salon_id == Hour.salon_id)\
    .all()

    context = {'request': request, 'salons': q}

    if hx_request:
        return templates.TemplateResponse("components/table.html", context)
    return templates.TemplateResponse("index.html", context)

def make_filters(names, l):
    filters = {}
    for n in names:
        if l[n] == 'on':
            filters[n] = True
    return filters

def dynamic_filter(q, filters, table):
    for attr, value in filters.items():
        q = q.filter(getattr(table, attr) == value)
    return q