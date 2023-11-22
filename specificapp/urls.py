from specificapp.views import *

from django.urls import path

app_name='something'

urlpatterns=[

    path('bittu/',bittu,name='bittu'),
    path('Ramesh/',Ramesh,name='Ramesh'),
]