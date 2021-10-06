"""Core Apps: Django app configuration"""

# Python imports
# Django imports
from django.apps import AppConfig

# 3rd party apps
# Local app imports

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
