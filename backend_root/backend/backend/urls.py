"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path
from api.auth_views import LogOutView, CookieTokenRefreshView
from .views import frontend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogOutView.as_view(), name='logout'),
]

if settings.DEBUG or getattr(settings, "SERVE_MEDIA", False):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

template_dirs = settings.TEMPLATES[0].get("DIRS", [])
frontend_index = (
    Path(template_dirs[0]) / "index.html"
    if template_dirs
    else None
)

# Enable SPA fallback only when a frontend build exists.
if frontend_index and frontend_index.exists():
    urlpatterns += [
        re_path(r'^(?!api/|admin/|media/).*$', frontend),
    ]
