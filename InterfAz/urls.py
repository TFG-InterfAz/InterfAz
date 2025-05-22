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
from ollama import views as ollamaViews
from html_renderizer import views as htmlViews

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ask/starcoder", views.prompt_view, name="prompt_view"),
    path('prompts/starcoder', views.show_prompts, name='show_prompts'),
    path('', home, name='home'),
    path('ask/ollama/', ollamaViews.ollama, name='ollama'),
    path('prompts/ollama', ollamaViews.prompts_list, name='prompts_list'),
    path('store_code', htmlViews.generate_html_view, name='generate_html'),
    path('generated/<int:html_id>/', htmlViews.show_generated_html, name='show_generated_html'),
    path('get_all_html/', htmlViews.get_all_html, name='show_all_html'),
    path('modify_html/<int:html_id>/', htmlViews.modify_html, name='modify_html'),
    path('delete_html/<int:html_id>/', htmlViews.delete_html, name='delete_html'),






]
