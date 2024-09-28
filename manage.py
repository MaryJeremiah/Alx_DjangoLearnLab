#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from gzip import READ
import os
import sys


def main():
Run administrative tasks. This function is called by the command-line utility when running the command line utility with the command line arguments # type: ignore
READ

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_api.settings')
edad58f (Initial commit of social media API project) # type: ignore
try:
        from django.core.management import execute_from_command_line
except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
