from django.urls import include, path
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from general_components.customTokenObtainPairView import CustomTokenObtainPairView


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

urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('calculatorFactPlan/', include('calculatorFactPlan.urls')),
]
