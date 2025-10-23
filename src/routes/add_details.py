
from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse,JSONResponse
from fastapi.templating import Jinja2Templates 


from src.config.db import db
from utils import get_loggedin_user


router=APIRouter()
templates=Jinja2Templates(directory="templates")


@router.get('/add/details')
def add_details_page(request:Request):
    user=get_loggedin_user(request)
    if user:
        return templates.TemplateResponse('add_details.html',{'request':request})
    return RedirectResponse('/login')


@router.post('/add/details')
def add_details(request:Request,date=Form(...),weight=Form(...),bloodPressure=Form(...),heartRate=Form(...),steps=Form(...)):
    
    user = get_loggedin_user(request)
    if user:
        user_id=user.id
        result=db.table('health').insert({
            'user_id':user_id,
            'date':date,
            'weight':weight,
            'bloodpressure':bloodPressure,
            'heartrate':heartRate,
            'steps':steps
        }).execute()
        if result.data:
            return templates.TemplateResponse('add_details_success.html',{'request':request})
        

@router.get('/details/{details_id}')
def show_details(request:Request,details_id):
    if get_loggedin_user(request):
        result=db.table('health').select('*').eq('id',details_id).execute()
        if result.data:
            return templates.TemplateResponse('edit_details.html',{'request':request,'details':result.data[0]})
        



@router.post('/details/{details_id}')
def show_details(request:Request,details_id,date=Form(...),weight=Form(...),bloodPressure=Form(...),heartRate=Form(...),steps=Form(...)):
    if get_loggedin_user(request):
        result=db.table('health').update({
            "date":date,
            "weight":weight,
            'bloodpressure':bloodPressure,
            'heartrate':heartRate,
            'steps':steps
        }).eq("id",details_id).execute()
        if result.data:
            return templates.TemplateResponse('update_details_success.html',{'request':request})
        


@router.get('/details/delete/{details_id}')
def delete_details(request:Request,details_id:int):
    user=get_loggedin_user(request)
    if user:
        result=db.table('health').delete().eq('id',details_id).execute()
        return RedirectResponse ('/dashboard',status_code=303)
    
        



