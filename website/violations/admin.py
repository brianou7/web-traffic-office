from django.contrib import admin

from .models import Infraction, Violation


admin.site.register(Infraction)
admin.site.register(Violation)