"""feedback_survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.views.static import serve
from base_app import views as general_views
from feedback_survey import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='dashboard', permanent=False), name='feedback_survey'),
    path('dashboard', general_views.DashboardView.as_view(), name='dashboard'),
    path('survey1', general_views.Survey1View.as_view(), name='survey1'),
    path('survey2', general_views.Survey2View.as_view(), name='survey2'),

    path('course-feedback/', include('base_app.urls', namespace='course_feedback')),
    path('static/<path:path>/', serve, {'document_root': settings.STATIC_FILE_ROOT, }),

]
