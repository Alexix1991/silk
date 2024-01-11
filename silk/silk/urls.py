from django.contrib import admin
from django.urls import path

from duties.views import DutiesAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dutieslist/', DutiesAPIView.as_view())
]
