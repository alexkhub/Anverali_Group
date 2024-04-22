from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone', 'role', 'slug')
    list_display_links = ('id', 'username', 'email', 'phone',)
    search_fields = ('id', 'username', 'phone', 'email')
    list_filter = ('role', )


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'expected_salary', 'user', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'user__username')


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'salary_min', 'salary_max', 'user', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'user__username')


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')


admin.site.register(User, UsersAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Skill, SkillsAdmin)
