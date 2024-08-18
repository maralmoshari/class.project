from django.urls import path

from . import views

app_name = 'customer'

urlpatterns = [
    path('show/' , views.show_customer , name = 'customershow') ,

]