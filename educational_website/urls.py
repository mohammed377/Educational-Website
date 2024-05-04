from django.contrib import admin
from django.urls import path, include  # Import include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include URLs from the api app
]

# Add other URL patterns below if needed
