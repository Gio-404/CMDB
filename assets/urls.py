#!/usr/bin/env python3
# Author:wb-wwb500625
# Create Date:2019/9/11

from django.urls import path
from assets import views

app_name = 'assets'
urlpatterns = [
    path('report/', views.report, name='report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('detail/<int:asset_id>/', views.detail, name="detail"),
    path('', views.dashboard),
]
