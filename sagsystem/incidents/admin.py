from django.contrib import admin

from .models import Incidents


class IncidentsConfig(admin.ModelAdmin):
    fields = ('date', 'worker', 'department', 'comment', 'file', 'adder',)
    list_display = ('date', 'worker', 'department',)


admin.site.register(Incidents, IncidentsConfig)
