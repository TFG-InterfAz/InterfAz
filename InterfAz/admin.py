from django.contrib import admin
from trial.models import Item
from starcoder.models import Prompt
# Register your models here.
admin.site.register(Item)
admin.site.register(Prompt)