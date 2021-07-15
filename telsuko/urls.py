"""telsuko URL Configuration

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
from information.views import HomeView,SignUpView
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('information/',include('information.urls')),
    path('',HomeView.as_view(),name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='security/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
  

  #change_password////
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='security/password_change.html',success_url='/'),name='password_change'),
    #path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    #reset_password////
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='security/password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='security/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='security/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='security/password_reset_complete.html'),name='password_reset_complete'),
    path('accounts/', include('allauth.urls')), # <--
    




]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
