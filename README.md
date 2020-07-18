# aws_django_test

Base files for a Django site deployed on AWS Elastic Beanstalk with Postgres. This repository contains 1 <i>application</i> named <b>projects</b> with sample <i>views</i>, <i>urls</i>, and <i>static files</i>.

https://docs.djangoproject.com/en/2.1/intro/
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html

Pre-requisite: Install Aws EB CLI

Note in requirements.txt use aws-psycopg2 rather than psycopg2
https://pypi.org/project/aws-psycopg2/


- - -
### Creating Elastic Beanstalk Environment and Application

Create an Elastic Beanstalk application named *aws_django* in the specified region.

```
eb init -p python-3.6 -r us-east-2 aws_django
```
Choose an existing keypair.

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
- - -
### Set Environment Variables in AWS Console.

Elastic Beanstalk>ENVIRONMENT_NAME>Configuration>Software>Environment properties

This is useful for storing sensitive information, which can be called with os.environ[VARIABLE] in python.

This should match the variables named in aws-django/settings.py

- - -
Deploy.
```
eb deploy
```

