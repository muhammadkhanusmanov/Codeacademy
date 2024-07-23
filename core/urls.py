from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from polls.views import Signup,Signin


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        terms_of_service="http://127.0.0.1:8000",
        contact=openapi.Contact(email=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',Signup.as_view()),
    path('signin/',Signin.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]