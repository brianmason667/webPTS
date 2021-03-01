from django.contrib import admin

from django.contrib import admin

from .models import (AssemblyLine, ProductionActual, Product, Department, Hourly, Machine, Defect, Downtime, Shift, DefectInstance, DowntimeInstance, Run)


class hourlyInline(admin.TabularInline):
    model = Hourly

admin.site.register(AssemblyLine)
admin.site.register(ProductionActual)
admin.site.register(Department)
admin.site.register(Hourly)
admin.site.register(Machine)
admin.site.register(Defect)
admin.site.register(Downtime)
admin.site.register(Product)
admin.site.register(Shift)
admin.site.register(DefectInstance)
admin.site.register(DowntimeInstance)
admin.site.register(Run)