# DevOps Flask Application

A hands-on project covering CI, Docker image publishing, and Kubernetes deployment.

## Architecture
GitHub → GitHub Actions → Pytest → Docker → Docker Hub → Local Kubernetes

## Technologies
- Python, Flask, Pytest
- Git, GitHub, GitHub Actions
- Docker, Docker Hub
- Kubernetes, Linux
- AWS and ECR exploration

## CI/CD
GitHub Actions runs automated tests and builds the Docker image.
Pushes to the main branch publish the image to Docker Hub.

## Kubernetes
The application runs locally with two replicas, resource requests and limits,
health probes, ConfigMap and Secret environment variables, persistent storage,
and a Kubernetes Service.

## Tests
Run `./venv/bin/pytest -v`

## Deployment scope
The application has been deployed to a local Kubernetes cluster.
AWS infrastructure and ECR were explored separately. The application
has not been deployed to Amazon EKS.

## Docker Hub
https://hub.docker.com/r/ajithcr/devops-flask-project
