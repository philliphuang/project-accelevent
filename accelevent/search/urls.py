from django.conf.urls import url
from . import views
from search.views import ResultView


urlpatterns = [
    url(r'^results$', ResultView.as_view(), name='results'),
]

