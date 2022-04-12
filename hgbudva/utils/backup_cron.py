from django.core import management
from django_cron import CronJobBase, Schedule


class Backup(CronJobBase):
    RUN_AT_TIMES = ["03:00"]
    schedule = Schedule(run_at_times = RUN_AT_TIMES)
    code = "media_db_backup"

    def do(self):
        management.call_command("dbbackup", "-c", "-z")
        management.call_command("mediabackup", "-c", "-z")
