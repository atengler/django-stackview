from django.conf.urls import url

from .views import HomePageView, CreateStackView, UserUpdateView


app_name = 'stacks'
urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^create/$', CreateStackView.as_view(), name='create'),
    url(r'^user/(?P<pk>\d+)/update/$', UserUpdateView.as_view(), name='user_update')
]

