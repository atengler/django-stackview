from django.conf.urls import url

from .views import LoginView, UserUpdateView


app_name = 'identity'
urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^user/(?P<pk>\d+)/update/$', UserUpdateView.as_view(), name='user_update')
]

