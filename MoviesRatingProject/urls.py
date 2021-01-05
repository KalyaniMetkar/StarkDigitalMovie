"""MoviesRatingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from movieratingapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_view.LoginView.as_view(template_name='login.html')),
    path('', views.welcome_view),
    path('api/movies/',views.IndexView.as_view()),
    path('showmovies/', views.show_user_view),
    path('choose/',views.choose_view),
    path('register/',views.user_register),
    path('data/', views.movie_view),
    path('detail/<int:pk>/', views.movie_detail_view),
    path('showposter/', views.poster_view),
    path('logout/',auth_view.LogoutView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
