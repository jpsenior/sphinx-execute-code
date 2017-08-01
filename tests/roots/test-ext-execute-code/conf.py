import os
import sys

master_doc = 'index'
exclude_patterns = ['_build']
sys.path.insert(0, os.path.abspath('.'))
import sphinx_execute_code
extensions = ['sphinx_execute_code']