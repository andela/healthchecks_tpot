#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hc.settings")

    from django.core.management import execute_from_command_line
    from django.db import connection
    print "***",connection.vendor
    execute_from_command_line(sys.argv)
