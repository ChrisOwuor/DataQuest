from django.contrib import admin
from .models import Department, Service, LegalInstrument


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name', 'owner')
    search_fields = ('dept_name',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'dept', 'status',
                    'timeline', 'ecitizen', 'enhancement')
    list_filter = ('status', 'ecitizen', 'enhancement')
    search_fields = ('service_name', 'dept__dept_name')


class LegalInstrumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'requires_change')
    list_filter = ('requires_change',)
    search_fields = ('name',)


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(LegalInstrument, LegalInstrumentAdmin)
