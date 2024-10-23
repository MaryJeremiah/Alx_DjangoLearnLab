<<<<<<< HEAD
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
=======
# manage.py

import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_api.settings')
>>>>>>> 04f34d7921d1ca1777f7cbe303bf39e8b8fd0384
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

<<<<<<< HEAD

if __name__ == '__main__':
    main()
=======
if __name__ == '__main__':
    main()






>>>>>>> 04f34d7921d1ca1777f7cbe303bf39e8b8fd0384
