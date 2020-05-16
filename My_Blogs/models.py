from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField(max_length= 200, default=False)
    date = models.DateField(blank=True, null=True)
    
    # def get_absolute_url(self):
    #     return reverse("My_Blogs:detail", kwargs={"pk": self.pk})
    
    
    #This function here is to show name of project on the database
    def __str__(self):
        return self.title