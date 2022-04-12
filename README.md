#### **DATABASE SET UP**

Note: You can use sqlite3 for dev environment and jump to virtualenv setup below.

If you are not going to use this credentials, you should change hgbudva/hgbudva/settings/.env file to match the changes you made.
The instructions will continue with this credentials.
```
DB_NAME = hgbudva
DB_USER = hgbudvaadmin
DB_PASSWORD = QuBxq9e%NVJX!KSs
```



Update your package information from all configured sources.

`sudo apt-get update`

Install postgresql and needed packages

`sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib`

During the Postgres installation, an operating system user named postgres was created to correspond to the postgres PostgreSQL administrative user. We need to change to this user to perform administrative tasks:

`sudo su - postgres`

You should now be in a shell session for the postgres user. Log into a Postgres session by typing:

`psql`

First, we will create a database for our Django project.

`CREATE DATABASE HGBUDVA;`

Next, we will create a database user which we will use to connect to and interact with the database. Set the password to something strong and secure:

`CREATE USER HGBUDVAADMIN WITH PASSWORD 'QuBxq9e%NVJX!KSs';`

We are setting the default encoding to UTF-8, which Django expects. We are also setting the default transaction isolation scheme to “read committed”, which blocks reads from uncommitted transactions. Lastly, we are setting the timezone. By default, our Django projects will be set to use UTC:

`ALTER ROLE HGBUDVAADMIN SET client_encoding TO 'utf8';`

`ALTER ROLE HGBUDVAADMIN SET default_transaction_isolation TO 'read committed';`

`ALTER ROLE HGBUDVAADMIN SET timezone TO 'UTC';`

Now, all we need to do is give our database user access rights to the database we created:

`GRANT ALL PRIVILEGES ON DATABASE HGBUDVA TO HGBUDVAADMIN;`

Exit the SQL prompt to get back to the postgres user’s shell session:

`\q`

Exit out of the postgres user’s shell session to get back to your regular user’s shell session:

`exit`


#### **VIRTUAL ENVIRONMENT SET UP**

You can get the virtualenv package that allows you to create these environments by typing:

`sudo pip install virtualenv`
`apt-get install python3-venv`


cd to where you want to set project up (will be assumed you want project in home dir)

`mkdir -p /var/www/`

`cd /var/www/`

This will install a local copy of Python and pip into a directory called .venv within your project directory. 

_Please do not use .env naming due to our env vars configuration file with that name, which is obeyed from gitignore file._

`python3 -m venv .venv`

Before we install applications within the virtual environment, we need to activate it. You can do so by typing:

`source .venv/bin/activate`

Once your virtual environment is active:

#### **CLONING PROJECT**

`git clone https://github.com/deliteser112/wagtail-python-django-website.git`


`pip install -r requirements.txt`

#### **CREATE LOG DESTINATION FILE**
`mkdir /var/www/hg-budva/hgbudva/logs/`

Project has dependency of this file, so we need to make it manually:
(It is ignored by git)

`touch logs/services.log`

#### **MAKE .ENV FILE**
Change .env.example file contents with actual data or leave untouched.

#### **MAKE AND APPLY MIGRATIONS**

cd ~/hg-budva/hgbudva

`python manage.py makemigrations`

`python manage.py migrate`


#### **ENABLE MODEL TRANSLATIONS**
`python manage.py sync_page_translation_fields`

`python manage.py update_translation_fields`

#### **CREATE SUPER USER WITH THIS COMMAND**

`python manage.py createsuperuser`

#### **RUN DEVELOPMENT SERVER**

`python manage.py runserver 0.0.0.0:8000`

#### **CACHE AND REDIS SET UP** (production)

`sudo apt-get install redis-server`
Note: If no cache need - remove settings for cache in settings.py

#### **OPTIONAL: RUNNING PRODUCTION SERVER**

For running project with nginx and uwsgi follow this tutorial:

Use configs in server/ dir
