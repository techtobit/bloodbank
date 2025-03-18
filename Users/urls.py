from django.urls import path
from .views import RegisterView, DonarListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('donars/', DonarListView.as_view() , name='donars')
]
