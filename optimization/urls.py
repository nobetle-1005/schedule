from django.contrib import admin
from django.urls import path
from optimization import views
from . import views
app_name="optimization"


urlpatterns = [
    path('result/', views.result,name="result"),

]
