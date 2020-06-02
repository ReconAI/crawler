## Purpose of the project
The purpose of the this project is to construct a tool that automatically searches and
fetches new video data from the Youtube and Vimeo in order to train more general
neural networks for machine vision.

## Project structure
The project consists of web and workers parts.
The web part is responsible for finding and displaying videos.
Workers download and create preview video.
All created files are stored on AWS S3.

The project uses AWS EC2, AWS SQS, AWS S3, AWS ECR, AWS RDS

### Installation to development

1) Create virtual environment (python3 -m venv ~/my_env_dir)
2) Activate environment (source ~/my_env_dir/bin/activate)
3) install dev packages (pip install -r requirements/dev.txt)
4) Create "local.py" settings file and place it to "crawler/settings" dir. You can use "local_example.py" as a basis.
5) Change keys:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY

6) Run migrations script (python manage.py migrate --settings=crawler.settings.local). 
Now web part is done and can be run by command:  
python manage.py runserver 0.0.0.0:8000

Workers part:
7) Change some keys
CELERY_BROKER_URL  
PROXIES   
SQS_CRAWLER_DOWNLOAD_VIDEO_FILE_QUEUE_NAME
8) Run workers   
DJANGO_SETTINGS_MODULE=crawler.settings.local celery -A crawler worker --loglevel=INFO -Q "your_SQS_CRAWLER_DOWNLOAD_VIDEO_FILE_QUEUE_NAME"


## Deploy
Deployment project is semi-manual.
2 scripts are used:
build-image - creates an image and puts it in AWS ECR
deploy-to-aws - downloads images and deploys on a specific EC2 instance


## Settings
Settings are located at "crawler/settings"
The main ones are

AWS_ACCESS_KEY_ID
DATABASES
PROXIES
AWS_SECRET_ACCESS_KEY


### Recommendations:
Make deploy using a CI/CD system (e.g. Gitlab) at future

