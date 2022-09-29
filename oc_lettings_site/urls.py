from django.contrib import admin
from django.urls import path, include


# sentry installation test
def trigger_error(request):
    division_by_zero = 1 / 0
    print(division_by_zero)


urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),  # sentry installation test
]
