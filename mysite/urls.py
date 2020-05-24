from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from blog.views.register import RegisterView

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog:home')),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls'))
]
