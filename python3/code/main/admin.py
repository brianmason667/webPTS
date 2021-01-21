# from django.contrib import admin

# # Register your models here.

# from .models import Question
# from .models import Choice

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)

from django.contrib import admin

from .models import (users, assembly_lines, pauid, departments, hourly)


class hourlyInline(admin.TabularInline):
    model = hourly
    extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']

admin.site.register(users)
admin.site.register(assembly_lines)
admin.site.register(pauid)
admin.site.register(departments)
admin.site.register(hourly)