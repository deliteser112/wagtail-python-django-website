from datetime import datetime

import os
from os.path import join, dirname
from notify import send_message_to_slack

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Functions for automatically execute operations


def collectstatic():

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("collectstatic cron started ", current_time)

    # activate virtual environment
    os.system('. ' + os.path.join(BASE_DIR, '.venv/bin/activate'))
    # execute python manage.py collectstatic
    os.system('python ' + os.path.join(PROJECT_DIR,
              'manage.py') + ' collectstatic --no-input')

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("collectstatic cron finished ", current_time)
    send_message_to_slack(
        ":books: Collectstatic procedure finished " + current_time)


def database_backup():
    import time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("database backup cron started ", current_time)

    os.system('. ' + os.path.join(BASE_DIR, '.venv/bin/activate'))
    db_backup_filename = 'db_backup_' + current_time + '.json'

    # export database to file
    os.system('python ' + os.path.join(PROJECT_DIR, 'manage.py') +
              ' dumpdata > /var/backups/' + db_backup_filename)

    # scp the file to backup server
    os.system('scp /var/backups/' + db_backup_filename +
              ' root@18.159.71.160:/var/backups/' + db_backup_filename)
    os.system('cd /var/backups/ && rm -f !('+db_backup_filename+')')

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("database backup cron finished ", current_time)
    send_message_to_slack(
        ":dart: Database backup procedure finished " + current_time)


def heartbeat():

    # notify about error and access logs
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("heartbeat cron started ", current_time)

    os.system('. ' + os.path.join(BASE_DIR, '.venv/bin/activate'))
    # deploy check
    deploy_check = os.popen(
        'python ' + os.path.join(PROJECT_DIR, 'manage.py') + ' check --deploy').read()
    slack_msg = ":heart: Heartbeat report! \n"
    slack_msg += ":male-astronaut: Deploy check: \n" + deploy_check + '\n'

    # read error.log and access.log files
    todays_error_log = os.popen('tail -30 /var/log/nginx/error.log').read()
    slack_msg += ":red_circle: Todays nginx error logs: \n" + todays_error_log + '\n'

    todays_access_log = os.popen('tail -5 /var/log/nginx/access.log').read()
    slack_msg += ":heavy_check_mark: Todays last access logs: \n" + todays_access_log + '\n'

    # sending logs to slack channel #hgbr-alerts
    send_message_to_slack(slack_msg)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("heartbeat cron finished ", current_time)


def clear_logs():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("clear logs cron started", current_time)

    # execute commands for removing log files
    os.system('echo "" >' + os.path.join(PROJECT_DIR, 'logs/crons.log'))
    os.system('echo "" >' + os.path.join(PROJECT_DIR, 'logs/services.log'))

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("clear logs cron finished ", current_time)


if __name__ == '__main__':
    collectstatic()
    # database_backup()
    heartbeat()
    # clear_logs()
