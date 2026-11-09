from django.urls import path
from .views import *

urlpatterns = [
    #-----------skills View------------#
    path('skills/', SkillListView.as_view(), name='skill-list'),
    
    #-----------projects View------------#
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
    
    
    #-----------experience View------------#
    path('experience/', ExperienceListView.as_view(), name='experience-list'),
    
    
    #-----------education View------------#
    path('education/', EducationListView.as_view(), name='education-list'),
    
    
    #-----------blog posts View------------#
    path('blog/', BlogPostListView.as_view(), name='blog-post-list'),
    path('blog/<slug:slug>/', BlogPostDetailView.as_view(), name='blog-post-detail'),
    
    
    #-----------contact messages View------------#
    path('contact/', ContactMessageCreateView.as_view(), name='contact-message-create'),
]