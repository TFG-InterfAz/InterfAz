from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Generated_Html(models.Model):
    title = models.TextField(max_length=255)
    prompt = models.TextField(max_length=255)
    html_code = models.TextField(null=True, blank=True)
    
    class AI_selector(models.TextChoices):
        STARCODER = "SC",  _("StarCoder")
        OLLAMA = "OL",  _("Ollama")
        OPENAI = "OP",  _("OPENAI")
        DEEPSEEK = "DK",  _("DeepSeek")
        CURSOR = "CS",  _("Cursor")
        CLAUDE = "CE",  _("Claude")
        UNKNOWN = "UN",  _("Unknown")

    
    ai = models.CharField(max_length=2, 
        choices = AI_selector.choices,
        default = AI_selector.UNKNOWN,
    )
    
    def __str__(self):
        return self.title