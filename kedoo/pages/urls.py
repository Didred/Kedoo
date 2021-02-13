from django.conf.urls import url, include
from . import views

# router = routers.DefaultRouter(trailing_slash=True)
# router.register('api', views.View, basename='api')

# urlpatterns = router.urls

urlpatterns = [
    url(r'^api/reg$', views.reg),
    url(r'^api/login$', views.login),
    url(r'^api/logout$', views.logout),
    url(r'^api/status$', views.status),
]
