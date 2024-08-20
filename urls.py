from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path('gartensea', PresentationView.as_view()),
    re_path(r'^', IndexView.as_view()),
]