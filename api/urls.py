
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
import Users.urls 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0.1/', include(Users.urls)),
    path('', include('example.urls')),
]
urlpatterns = format_suffix_patterns(urlpatterns)