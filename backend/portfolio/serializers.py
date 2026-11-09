from rest_framework import serializers
from .models import *


#------------Skill Serializer------------#
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'proficiency', 'featured', 'created_at']
        
#------------Project Serializer------------#
class ProjectSerializer(serializers.ModelSerializer):
    technologies = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'slug', 'short_description', 'description', 'technologies', 
                  'github_url', 'live_url', 'cover_image', 'featured', 'status', 'created_at']
        read_only_fields = ['id', 'created_at', ]
        
#------------Experience Serializer------------#
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'company_name', 'position', 'employment_type', 'start_date', 
                  'location', 'end_date', 'description', 'is_current', 'created_at']
        read_only_fields = ['id', 'created_at']
        
#------------Education Serializer------------#
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'institution', 'qualification', 'field_of_study', 'start_year', 
                  'end_year', 'is_current', 'location', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']    
        
       
 #------------BlogPost Serializer------------#
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'summary', 'content', 'status', 'published_at', 'created_at']
        read_only_fields = ['id', 'created_at']
        
        
#------------ContactMessage Serializer------------#
class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'is_read', 'created_at']
        read_only_fields = ['id', 'is_read', 'created_at']              
                    
        