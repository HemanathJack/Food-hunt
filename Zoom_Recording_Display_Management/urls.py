"""
URL configuration for Zoom_Recording_Display_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from ZoomApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name="login"),
    path('register/', views.register, name="register"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('create_recipe', views.create_recipe, name='create_recipe'),
    path('recipe/<int:recipe_pk>/update/', views.update_recipe, name='update_recipe'),
    path('recipe/<int:pk>', views.delete_recipe, name='delete_recipe'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("", views.home, name='home'),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)