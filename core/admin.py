from django.contrib import admin
from core.models import *

class StudentAttributeInline(admin.TabularInline):
    model = StudentAttribute

class QuestionStepInline(admin.TabularInline):
    model = QuestionStep

class QuestionSkillInline(admin.TabularInline):
    model = QuestionSkill

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at', 'updated_at')
    inlines = [QuestionStepInline]

class StudentAdmin(admin.ModelAdmin):
    list_display = ('client_student_id', 'created_at', 'updated_at')
    inlines = [StudentAttributeInline]

class StudentAttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'created_at', 'updated_at')

class QuestionSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'created_at', 'updated_at')

class QuestionStepAdmin(admin.ModelAdmin):
    list_display = ('description', 'question', 'created_at', 'updated_at')
    inlines = [QuestionSkillInline]

class TutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

class HpitTransactionAdmin(admin.ModelAdmin):
    list_display = ('anon_student_id', 'session_id', 'stu_response_type', 'stu_response_subtype')

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentAttribute, StudentAttributeAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionStep, QuestionStepAdmin)
admin.site.register(QuestionSkill, QuestionSkillAdmin)
admin.site.register(HpitTransaction, HpitTransactionAdmin)

# If nothing special/overriding, then, you can use the admin.ModelAdmin (example below)
# admin.site.register(QuestionStep, admin.ModelAdmin)

