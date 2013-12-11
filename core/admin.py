from django.contrib import admin
from core.models import *

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at', 'updated_at')

# Register your models here.
admin.site.register(Student, admin.ModelAdmin)
admin.site.register(StudentAttribute, admin.ModelAdmin)
admin.site.register(Tutor, admin.ModelAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionStep, admin.ModelAdmin)
admin.site.register(QuestionSkill, admin.ModelAdmin)
