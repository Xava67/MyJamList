"""
Definition of urls for MyJamList.
"""

from datetime import datetime
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('pdf/', views.pdf_view, name='pdf_view'),
    path('upload-song/', views.upload_song, name='upload_song'),
    path('plan_to_learn/', views.plan_to_learn, name='plan_to_learn'),
    path('learning/', views.learning, name='learning'),
    path('mastering/', views.mastering, name='mastering'),
    path('mastered/', views.mastered, name='mastered'),
    path('my_list/', views.my_list, name='my_list'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
    path('update_song/', views.update_song, name='update_song'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
