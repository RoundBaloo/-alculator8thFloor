"""
URL configuration for calculator8thFloor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from calculatorFactPlan import views

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
routerData.register(r'all', views.DataViewSet, basename='calculated-data')
routerData.register(r'input', views.InputedDataViewSet, basename='inputed-data')
routerHead = routers.DefaultRouter()
routerHead.register(r'', views.HeadViewSet, basename='head-funcs')


urlpatterns = [
    path('head/', include(routerHead.urls)),
    path('data/', include(routerData.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 

