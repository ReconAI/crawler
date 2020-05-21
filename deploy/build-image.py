import os

from invoke import run
from invoke.context import Context

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCKERFILE_PATH = BASE_DIR

image_registry_url = '105492073392.dkr.ecr.us-east-2.amazonaws.com'
aws_region = 'us-east-2'

def build_image(ctx, dockerfile, build_tag_name):
    ctx.run(f'docker build -f {dockerfile} -t {build_tag_name} . ', echo=True)
    ctx.run(f'docker tag {build_tag_name} {image_registry_url}/{build_tag_name}', echo=True)
    ctx.run(f'docker push {image_registry_url}/{build_tag_name}', echo=True)


run(f'aws ecr get-login-password --region {aws_region} --profile=recon | docker login --username AWS --password-stdin {image_registry_url}', echo=True)

ctx = Context()
with ctx.prefix(f'cd {DOCKERFILE_PATH}'):
    build_image(ctx, './Dockerfile', 'crawler')

