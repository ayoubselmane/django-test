- Clone the repository
- Create a virtual environment (example conda create -n yourenvname)
- navigate via the terminal to the folder you cloned and run:
- pip install -r requirement.txt to install all the packages you need to run the project
- create a .env file inside the receipt_tracker directory where you put you credential data for example to use a postgres database (uncomment it on settings.py DATABASES) you need the following:
-SECRET_KEY=django-insecure-728k0bs%91o$^sp%aa_ji@2fmtwpdk7r1na#*$%l2+%)7tnpo3
 DB_NAME=database_name
 DB_USER=database_user
 DB_PASSWORD=database_password
 DB_HOST=localhost
 DB_PORT=5432
- run the development server to start the project, you can do so by:
- python manage.py runserver
- this will run it on your local machine, if you want to run it on your local network run:
- python manage.py runserver 0.0.0.0:8000
- add your local ip address to the allowed host (i have added the address of 192.168.1.10 as an example but add your own there) to let anyone on your newtork access the app.  
