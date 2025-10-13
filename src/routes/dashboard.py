
from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse,JSONResponse
from fastapi.templating import Jinja2Templates 


from src.config.db import db
from utils import get_loggedin_user


router=APIRouter()
templates=Jinja2Templates(directory="templates")



@router.get('/dashboard')
def dashboard(request:Request):
    if get_loggedin_user(request):
        result=db.table('health').select('*').execute()
        
        if result.data:
            print(result.data)
            return templates.TemplateResponse('dashboard.html',{'request':request,'details':result.data})