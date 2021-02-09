from django.contrib import admin

from django.contrib import admin

from .models import (assembly_line, productionactual, department, hourly)


class hourlyInline(admin.TabularInline):
    model = hourly

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']

admin.site.register(assembly_line)
admin.site.register(productionactual)
admin.site.register(department)
admin.site.register(hourly)