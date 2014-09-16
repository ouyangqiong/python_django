from django.db import models
from django.contrib import admin

# Create your models here.
class Reporter(models.Model):
    full_name=models.CharField(max_length=70)
    
    def __str__(self):
        return self.full_name
class Article(models.Model):
    pub_date=models.DateField()
    headline=models.CharField(max_length=200)
    content=models.TextField()
    reporter=models.ForeignKey(Reporter)
    
    def __str__(self):
        return self.headline
class ReporterAdmin(admin.ModelAdmin):
    list_display=('full_name',)
admin.site.register(Reporter, ReporterAdmin)