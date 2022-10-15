from django.contrib import admin
from django.urls import path,include

# route the urls for api application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

]
