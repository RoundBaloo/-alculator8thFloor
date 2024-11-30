from django.urls import include, path
from rest_framework import routers
from calculatorFactPlan import views


routerData = routers.DefaultRouter()
routerData.register(r'fact', views.FactDataViewSet, basename='fact-calculated-data')
routerData.register(r'plan', views.PlanDataViewSet, basename='plan-calculated-data')
routerData.register(r'input', views.InputedDataViewSet, basename='inputed-data')
routerHead = routers.DefaultRouter()
routerHead.register(r'', views.HeadViewSet, basename='head-funcs')
routerColumnNames = routers.DefaultRouter()
routerColumnNames.register(r'names', views.TableColumnNamesViewSet, basename='column-names-funcs')

urlpatterns = [
    path('head/', include(routerHead.urls)),
    path('export/fact/excel', views.export_fact_excel),
    path('export/plan/excel', views.export_plan_excel),
    path('export/fact_plan/excel', views.export_fact_plan_excel),
    path('export/report/docx', views.export_report_docx),
    path('export/report/pdf', views.export_report_pdf),
    path('data/', include(routerData.urls)),
    path('fact-data/', views.fact_data_view, name='fact_data'),
    path('', include(routerColumnNames.urls)),
]
