from django.urls import path
from .views import RegisterView, LoginView, DonarListView, DonarProfileView, ReportView, FeedbackView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('donars/', DonarListView.as_view() , name='donars'),
    path('profile/<int:pk>/',DonarProfileView.as_view() , name='profile'),
    path('report/', ReportView.as_view() , name='report'),
    path('feedback/', FeedbackView.as_view() , name='feedback'),
]

