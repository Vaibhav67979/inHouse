
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="Login"),
    path('home/', include('properties.urls')),
    path('contact/', views.contact, name="Contact"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('login', views.handleLogin, name="handleLogin"),
    path('properties/', include('properties.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
