from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    tech_stack = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    repo = models.CharField(max_length=100, blank=True, null=True)
    link_post = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title