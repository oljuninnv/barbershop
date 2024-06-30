from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import *

from main.form import VisitingForm
from .models import *
from django.views.generic import *

# Create your views here.

def index(request): # Главная страница
    workers  = Worker.objects.all()
    
    # Отрисовка HTML-шаблона index.html с данными
    # внутри переменной index
    return render (request,'main/index.html',
                   context={
                            'title':'Главная страница',
                            'workers':workers
                            },
                   )
    
def records(request):
    visiting = Visiting.objects.all()
    all_time = ['09:00', '10:40', '12:40', '14:20', '16:00', '17:40', '18:20', '19:50']
    date = datetime.today().strftime("%Y-%m-%d")
    max_date = datetime.today() + timedelta(days=30)

    if request.method == 'GET':         
        selected_date = request.GET.get('InputDate')
        request.session['selected_date'] = selected_date
        request.session['selected_name'] = request.GET.get('InputName')
        request.session['selected_phone'] = request.GET.get('InputPhone')
        if Visiting.objects.filter(date=request.session['selected_date']).all():
            appointments = Visiting.objects.filter(date=request.session['selected_date']).all()
            for obj in appointments:
                print(obj)
                if obj.customer_name is not None:
                    
                    all_time.remove(obj.time.strftime("%H:%M"))
        
            return render(request, 'main/record.html', {
                'title': 'Запись',
                        'visiting': visiting,
                        'all_time': all_time,
                        'date': date,
                        'max_date': max_date,
                        'step_1': False,
                        'step_2': True,
                    
            })
                
        else:
            return render(request, 'main/record.html', {
                'title': 'Запись',
                'visiting': visiting,
                'all_time': all_time,
                'date': date,
                'max_date': max_date,
                'step_1': True,
                'er_msg': "Выберите другую дату: на этот день записаться не получится",
            })
    else:
        return render(request, 'main/record.html', {
            'title': 'Запись',
            'visiting': visiting,
            'all_time': all_time,
            'date': date,
            'max_date': max_date,
            'step_1': True,
            'er_msg': "",
        })

# def records(request): # Страница записи
#      visiting = Visiting.objects.all()
#      form = VisitingForm()
#      return render(request, 'main/record.html', {
#              'title': 'Запись',
#              'form':form,})

def thanks(request):
    if request.method == 'POST':
        workers = Worker.objects.all()
        selected_date = request.session['selected_date']
        selected_time = request.POST['InputTime']
        customer_name = request.session['selected_name']
        customer_phone = request.session['selected_phone']

        if Visiting.objects.filter(date=selected_date, time=selected_time).exists():
            appointment = Visiting.objects.get(date=selected_date, time=selected_time)
            appointment.customer_name = customer_name
            appointment.customer_phone = customer_phone
            appointment.save()
            return render(request, 'main/thanks.html', {'customer_name': customer_name, 'customer_phone': customer_phone, 'time': selected_time, 'worker': appointment.worker})
        else:
            return render(request, 'main/thanks.html')
    else:
        return HttpResponse("Ошибка, попробуйте заново")