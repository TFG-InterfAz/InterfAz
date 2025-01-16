from django.db import models

# Create your models here.
class Prompt(models.Model):
    request = models.TextField(max_length=255)
    response = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.request