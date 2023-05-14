"""
Django command to wait for the database to be available.
"""
import time

from django.core.management.base import BaseCommand
from django.db import OperationalError
from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        self.stdout.write("waiting for db...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("db unavailable waiting 1s")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('db available!'))
