"""Core Urls: API urls"""

# Python imports
# Django imports
from django.urls import path

# 3rd party apps
# Local app imports
from .views import Spellcheck

app_name = 'core'

urlpatterns = [
	path('spellcheck/', Spellcheck.as_view(),
         name='spellcheck'),
]