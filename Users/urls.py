from django.urls import path
from .views import RegisterView, DonarListView, DonarProfileView, ReportView, FeedbackView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('donars/', DonarListView.as_view() , name='donars'),
    path('profile/<int:pk>/',DonarProfileView.as_view() , name='profile'),
    path('report/', ReportView.as_view() , name='report'),
    path('feedback/', FeedbackView.as_view() , name='feedback'),
]

