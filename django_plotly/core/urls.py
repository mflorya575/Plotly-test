from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.chart, name='chart'),
    path('bar/', views.yearly_avg_co2, name='bar'),
]
