from django.urls import include, path
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from calculatorFactPlan import views
from general_components.customTokenObtainPairView import CustomTokenObtainPairView

from django.conf import settings
from django.conf.urls.static import static



router = routers.DefaultRouter()
router1 = routers.DefaultRouter()
routerData = routers.DefaultRouter()
routerData.register(r'fact', views.FactDataViewSet, basename='fact-calculated-data')
routerData.register(r'plan', views.PlanDataViewSet, basename='plan-calculated-data')
routerData.register(r'input', views.InputedDataViewSet, basename='inputed-data')
routerHead = routers.DefaultRouter()
routerHead.register(r'', views.HeadViewSet, basename='head-funcs')

urlpatterns = [
    path('head/', include(routerHead.urls)),
    path('export/fact/excel', views.export_fact_excel),
    path('export/plan/excel', views.export_plan_excel),
    path('export/fact_plan/excel', views.export_fact_plan_excel),
    path('export/report', views.export_report),
    path('data/', include(routerData.urls)),
    path('fact-data/', views.fact_data_view, name='fact_data'),
]
