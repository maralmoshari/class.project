from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('show/' , views.show_menu , name = 'show') ,
    path('create/' , views.create_menu , name = 'create') ,
]
