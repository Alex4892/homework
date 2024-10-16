from django.urls import path
from homework_app.views import view_index 

app_name = "app"

urlpatterns = [
    path('', view_index, name='index'),
    # path('', html_button, name='htmlbutton'),
]
