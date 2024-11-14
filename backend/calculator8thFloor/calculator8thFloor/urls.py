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

schema_view = get_schema_view(
       openapi.Info(
           title="Your API Title",
           default_version='v1',
           description="Your API Description",
           terms_of_service="https://www.gnu.org/licenses/lgpl.html",
           contact=openapi.Contact(email="contact@snippets.local"),
           license=openapi.License(name="BSD License"),
       ),
   )


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
    path('data/', include(routerData.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
