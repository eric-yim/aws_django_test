# aws_django

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html

Requirement: Install Aws EB CLI
Creates an Elastic Beanstalk application named aws_django in the specified region.
Set up SSH.
Choose an existing keypair.
```
eb init -p python-3.6 -r us-east-2 aws_django
```

Creates an Elastic Beanstalk Environment named aws-django-env.
```
eb create aws-django-env
```

Copy application location. Something like... eb-django-app-dev.elasticbeanstalk.com into aws_django/settings.py
If you forget the host name, check it on aws.com > services > elastic beanstalk > environments
```
...
ALLOWED_HOSTS = ['eb-django-app-dev.elasticbeanstalk.com']

```

Deploy.
```
eb deploy
```

===================================================================================
To collect static files, add STATIC_ROOT to settings.py
```
...
STATIC_URL = '/static/'
STATIC_ROOT = 'static'
```
Run following (within virtual environment).
```
(venv) ~/aws_django$ python manage.py collectstatic
```