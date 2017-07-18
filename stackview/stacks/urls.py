from django.conf.urls import url

from .views import OverviewView, CreateStackView


app_name = 'stacks'
urlpatterns = [
    url(r'^$', OverviewView.as_view(), name='overview'),
    url(r'^create/$', CreateStackView.as_view(), name='create'),
]

