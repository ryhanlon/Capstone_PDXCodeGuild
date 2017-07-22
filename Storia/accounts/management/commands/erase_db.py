import os
import shutil
from glob import glob

from Storia.settings import BASE_DIR
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Finds all migration files and all files with .db then deletes them.
    NOTE: Does not manage schema changes. #TODO
    """
    help = 'Permanent destroys migrations and database, FLUSH ONLY!'

    def handle(self, *args, **options):
        path = f'{BASE_DIR}/**/migrations'
        migrations = glob(path)

        for migration in migrations:
            shutil.rmtree(migration)

        # db_path = '{BASE_DIR}/**/db.sqlite3'
        # for db in glob(db_path):
        #     os.remove(db)

        call_command('flush')
        # call_command('makemigrations', 'insights')
        # call_command('migrate')
        # call_command('createsuperuser')

        self.stdout.write(self.style.SUCCESS('Successfully destroyed migrations and db'))


