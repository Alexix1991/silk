from django.contrib import admin

from .models import (
    Crops,
    Duties,
)


admin.site.register(Duties)
admin.site.register(Crops)
