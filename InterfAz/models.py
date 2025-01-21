from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Prompt(models.Model):
    request = models.TextField(max_length=255)
    response = models.TextField(null=True, blank=True)
    
    class AI(models.TextChoices):
        STARCODER = "SC", _("StarCoder")
        OLLAMA = "OL", _("Ollama")
        UNKNOWN = "AI", _("Unknown")
    
    ai = models.CharField(max_length=2, 
        choices = AI.choices,
        default = AI.UNKNOWN,
    )

    def __str__(self):
        return self.request