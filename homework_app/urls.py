from django.urls import path
from homework_app.views import view_index, html_button 

app_name = "app"

urlpatterns = [
    path('', view_index, name='index'),
    path('', html_button, name='htmlbutton'),
]
