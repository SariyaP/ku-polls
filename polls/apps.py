"""This module is for apps."""
from django.apps import AppConfig


class PollsConfig(AppConfig):
    """Configuration for polls."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
