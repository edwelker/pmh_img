#!/usr/bin/env python
import os
import sys

sys.path.insert(0, '/home/welkere/python')
sys.path.insert(0, '/home/welkere/python/pmh_img')

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pmh_img.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'pmh_img.settings'

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pmh_img.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
