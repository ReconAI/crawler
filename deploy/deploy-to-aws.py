import os

from fabric import Connection

DEV_EC2_HOST = 'ubuntu@3.136.160.174'

DEPLOY_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(DEPLOY_DIR)

pem_filename = os.path.join(DEPLOY_DIR, 'recon.pem')

image_registry_url = '105492073392.dkr.ecr.us-east-2.amazonaws.com'
aws_region = 'us-east-2'
build_tag_name = 'crawler'
workers_build_tag_name = 'crawler-workers'

conn = Connection(
    DEV_EC2_HOST, connect_kwargs={
        "key_filename": pem_filename,
    },
)

result = conn.run('mkdir -p ~/crawler')

# authorize docker
cmd = f'/home/ubuntu/venv/crawler/bin/aws ecr get-login-password --region {aws_region} --profile=recon | docker login --username AWS --password-stdin {image_registry_url}'

conn.run(cmd, echo=True)

with conn.prefix('cd /home/ubuntu/crawler/'):
    conn.run('docker stop $(docker ps -a -q)', echo=True)  # stop all containers
    conn.run(f'docker rmi -f {image_registry_url}/{build_tag_name}', echo=True)  # delete old image
    conn.run(f'docker pull {image_registry_url}/{build_tag_name}', echo=True)
    conn.run(f'docker run -d -p 8000:8000 {image_registry_url}/{build_tag_name}', echo=True)

    conn.run(f'docker pull {image_registry_url}/{workers_build_tag_name}', echo=True)
    worker_command = '"celery" "-A" "crawler" "worker" "--loglevel=INFO" "-Q" "prod-crawler-download-video-file-queue"'
    conn.run(f'docker run -d {image_registry_url}/{workers_build_tag_name} {worker_command}', echo=True)
