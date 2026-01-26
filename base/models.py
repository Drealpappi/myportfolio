from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=100) # e.g., "Django, PostgreSQL"
    image = models.ImageField(upload_to='project_images/', blank=True)
    github_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField()
    subject = models.CharField(max_length= 200, null=True, blank= True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"message.{self.name}-{self.email}"
