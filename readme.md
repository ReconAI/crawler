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

