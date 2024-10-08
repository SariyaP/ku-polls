from django.contrib import admin
from django.urls import include, path
from polls import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/polls/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
]