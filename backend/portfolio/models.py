from django.db import models


#------------Skill Model------------#
class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming Language'),
        ('frontend', 'Frontend Development'),
        ('backend', 'Backend Development'),
        ('mobile', 'Mobile Development'),
        ('database', 'Database'),
        ('design', 'UI/UX Design'),
        ('tool', 'Tools & Technologies'),
    ]
    
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    proficiency = models.PositiveIntegerField(default=50)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  #present when the skill is created also (unique=true)-prevents dublicate
    
    def __str__(self): #display name of skill instead of object label
        return self.name
    
#------------Project Model------------#
class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('planned', 'Planned'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    technologies=models.ManyToManyField(Skill, related_name='projects')
    github_url=models.URLField(blank=True, null=True)
    live_url=models.URLField(blank=True, null=True)
    cover_image=models.ImageField(upload_to='project/covers/')
    featured=models.BooleanField(default=False)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
#------------Experience Model------------#    
class Experience(models.Model):
    EMPLOYMENT_TYPE = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('collaboration', 'Collaboration'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
        ('volunteer', 'Volunteer'),
    ]
    
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE)
    start_date = models.DateField()
    location = models.CharField(max_length=200, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.position} at {self.company_name}"
    
#------------Education Model------------#
class Education(models.Model):
    institution = models.CharField(max_length=200) 
    qualification = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True, null=True)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    location = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.qualification} at {self.institution}"

#------------Blog Model------------#
class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=500)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='blog/covers/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
#------------Contact-Message Model------------#   
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}" 