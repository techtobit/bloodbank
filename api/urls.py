
from django.contrib import admin
from django.urls import path, include

import Users.urls 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(Users.urls)),
    path('', include('example.urls')),
]
