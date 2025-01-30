"""
URL configuration for InterfAz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from starcoder import views
from ollama import views as v2
from openai_integration import views as openai_view

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ask/starcoder", views.prompt_view, name="prompt_view"),
    path('prompts/starcoder', views.show_prompts, name='show_prompts'),
    path('', home, name='home'),
    path('ask/ollama/', v2.ollama, name='ollama'),
    path('prompts/ollama', v2.prompts_list, name='prompts_list'),
    path('ask/openai/', openai_view.openai, name='openai'),
    path('prompts/openai', openai_view.prompts_list, name='show_openai_prompts'),


]
