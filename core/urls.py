from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('Users.urls',
    namespace="user-urls")),
    
    path('api/v1/vote/', include('Vote.urls',
    namespace="votes")),
]
