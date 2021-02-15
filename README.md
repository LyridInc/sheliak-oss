# sheliak-oss

initial check-in

pre-req:
- Set PostgresURL in env file, ensure the URL is accessible by the serverless functions
- Generate secret string and set them at SECRET_KEY in env file

to start locally:
run these initial setup from empty database:
```
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser --username=$admin_username --email=$admin_email
```
then run
```
python manage.py runserver
```
once the service is running, you can just submit them using lyrid command line client:

lc code submit

which will create serverless build and deployment of the django project
