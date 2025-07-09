from django.contrib import admin
from django.urls import path, include
from puppies.views import home, CustomLoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('puppy/', include('puppies.urls')),
    path('login/', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('', include('django.contrib.auth.urls')),  # Handles logout, password reset, etc.
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
