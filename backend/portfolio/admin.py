from django.contrib import admin
from .models import *


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at','proficiency', 'featured')
    list_filter = ('category', 'featured')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','featured', 'created_at')
    list_filter = ('status','featured', 'created_at')
    search_fields = ('title', 'short_description', 'description')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('technologies',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company_name', 'employment_type', 'start_date', 'is_current')
    list_filter = ('employment_type', 'start_date', 'is_current')
    search_fields = ('position', 'company_name', 'description')
    readonly_fields = ('created_at',)
    ordering = ('-start_date',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('qualification', 'institution', 'field_of_study', 'start_year', 'end_year')
    list_filter = ('start_year','end_year')
    search_fields = ('qualification', 'institution', 'field_of_study')
    readonly_fields = ('created_at',)
    ordering = ('-start_year',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'published_at', 'created_at')
    list_filter = ('status', 'published_at')
    search_fields = ('title', 'summary', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)