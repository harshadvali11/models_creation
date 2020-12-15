"""project12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('display_topic/',views.display_topics,name='display_topics'),
    path('display_webpages/',views.display_webpages,name='display_webpages'),
    path('display_access/',views.display_access,name='display_access'),
    path('delete_webpage/',views.delete_webpage,name='delete_webpage'),
    
    path('update_webpage/',views.update_webpage,name='update_webpage'),
    path('form_create_topic/',views.form_create_topic,name='form_create_topic'),
    path('form_create_webpage/',views.form_create_webpage,name='form_create_webpage'),
    path('form_update_webpage/',views.form_update_webpage,name='form_update_webpage'),
    
    path('form_delete_webpage/',views.form_delete_webpage,name='form_delete_webpage'),
    
    path('select_topic/',views.select_topic,name='select_topic'),
    path('form_display_webpage/',views.form_display_webpage,name='form_display_webpage'),
    
    path('multi_select/',views.multi_select,name='multi_select'),
    
    path('checkbox/',views.checkbox,name='checkbox'),


]
