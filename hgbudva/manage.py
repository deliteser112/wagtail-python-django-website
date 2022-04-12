#!/usr/bin/env python
import os
import sys

from os.path import join
from dotenv import load_dotenv

dotenv_path = join("hgbudva/settings/.env")
load_dotenv(dotenv_path)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv("DJANGO_SETTINGS_MODULE"))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
