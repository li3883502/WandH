from django.urls import path
from .views import IndexView

app_name = 'stormsha'
urlpatterns = [
    path('', IndexView.as_view(template_name='stormsha/index.html'), name='index')
]

