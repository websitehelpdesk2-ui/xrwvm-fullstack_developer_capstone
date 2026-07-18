from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),

    # Route for the React frontend registration page
    path('register/', TemplateView.as_view(template_name="index.html")),
    path('register', TemplateView.as_view(template_name="index.html")),

    # Existing frontend routes (e.g., login, home, etc.)
    path('login/', TemplateView.as_view(template_name="index.html")),
    path('', TemplateView.as_view(template_name="index.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)