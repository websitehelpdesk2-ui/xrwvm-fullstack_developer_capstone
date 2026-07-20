# djangoapp/urls.py

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for registration
    path(route='register/', view=views.registration, name='register'),
    path(route='register', view=views.registration),

    # path for login
    path(route='login/', view=views.login_user, name='login'),
    path(route='login', view=views.login_user),

    # path for logout
    path(route='logout/', view=views.logout_request, name='logout'),
    path(route='logout', view=views.logout_request),

    # Add the path for get_cars here:
    path(route='get_cars', view=views.get_cars, name='get_cars'),

    # path for dealer reviews view
    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)