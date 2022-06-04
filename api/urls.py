from django.urls import path
from . import views

urlpatterns = [
    path('campaign/', views.CampaignList.as_view()),
    path('campaign/<int:pk>', views.CampaignListSingle.as_view()),
    path('survey/', views.SurveyList.as_view()),
    
]

