import os
import sys

# Add your project directory to the Python path
path = '/home/Kidy/ecommerce_project/ecommerce_backend'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'ecommerce_api.settings'

# Import and configure Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
