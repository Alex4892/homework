from django.shortcuts import render

from .forms import TableForm

import datetime

def view_index(request):
    date_today = datetime.datetime.now()
    today = datetime.date.today()
    first_day_year = datetime.date(today.year, 1, 1)
    delta = datetime.timedelta(days=256)
    prog_day = first_day_year + delta
    context = {
        "date_today": date_today,
        "prog_day": prog_day
    } 
    return render(request, "index.html", context=context)

def html_button(request):
    if request.method == "POST":  
        form = TableForm(request.POST)  
        if form.is_valid():  
            num = form.cleaned_data['num']
            return render(request, 'index.html', {'Number':num, 'range': range(1,11)})
    else:  
        form = TableForm()  
    return render(request, 'index.html', {'form':form})


# def view_calculator(request):
#     for i in range(1,10):
#         for j in range(1,10):
#             print(f"{i} * {j} = {i*j:2}")
#             print()
#         context = {
#         "calculator": calculator
#     } 
#     return render(request, "index.html", context=context)


# Create your views here.
