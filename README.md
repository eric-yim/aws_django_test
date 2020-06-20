# aws_django

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html

Requirement: Install Aws EB CLI
```
eb init -p python-3.6 -r us-east-2 aws_django
```
This creates an Elastic Beanstalk application named aws_django in the specified region.

```
eb create aws-django-env
```
This creates an Elastic Beanstalk Environment named aws-django-env.