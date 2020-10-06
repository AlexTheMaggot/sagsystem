from django.contrib import admin

from .models import Departments, Functions, Workers


class DepartmentsConfig(admin.ModelAdmin):

    fields = ('name', 'department_slug')
    prepopulated_fields = {'department_slug': ('name',)}
    list_display = ('name', )


admin.site.register(Departments, DepartmentsConfig)


class FunctionsConfig(admin.ModelAdmin):
    fields = ('name', 'function_slug')
    prepopulated_fields = {'function_slug': ('name',)}
    list_display = ('name',)


admin.site.register(Functions, FunctionsConfig)


class WorkersConfig(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'department', 'function', 'worker_slug')
    prepopulated_fields = {'worker_slug': ('first_name', 'last_name')}
    list_display = ('first_name', 'last_name', 'department', 'function')


admin.site.register(Workers, WorkersConfig)
