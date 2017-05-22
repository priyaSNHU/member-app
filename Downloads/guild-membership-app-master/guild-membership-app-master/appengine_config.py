# appengine_config.py
from google.appengine.ext import vendor
import os

# Add any libraries install in the "lib" folder.
# This is the longhand version that can work in tests.
vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))
