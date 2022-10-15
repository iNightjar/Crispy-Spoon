from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token 

# route the urls for api application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # url for token request
    path('tokenrequest/', obtain_auth_token),
]
