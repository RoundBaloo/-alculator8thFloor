from django.urls import path
from . import views


urlpatterns = [
    path('fact/', views.fact_export, name='fact_export'),
    path('plan/', views.plan_export, name='plan_export'),
    path('fact_plan/', views.fact_plan_export, name='fact_plan_export'),
]
