"""
Django Command to wait for db to be available
"""
import time

from django.core.management import BaseCommand
from psycopg2 import OperationalError as Psycog2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        """EntryPoint for Command"""
        self.stdout.write("waiting for database....")
        db_check = False
        while db_check is False:
            try:
                self.check(databases=["default"])
                db_check = True
            except (Psycog2Error, OperationalError):
                self.stdout.write("Db is unavailable. Retrying in 1 second .....")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database is up and running"))
