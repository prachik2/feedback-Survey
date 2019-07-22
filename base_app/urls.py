from django.urls import path

from . import views

app_name = "base_app"

urlpatterns = [
    path('survey1/', views.Survey1View.as_view(), name='survey1'),
    path('survey2/', views.Survey2View.as_view(), name='survey2'),
    path('create-survey1/', views.CreateSurvey1.as_view(), name='create_survey1'),
    path('create-survey2/', views.CreateSurvey2.as_view(), name='create_survey2'),

]