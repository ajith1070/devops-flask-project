# End-to-End DevOps Flask Application

A complete, hands-on DevOps project demonstrating automated testing, Docker image publishing, container orchestration, and deployment to Kubernetes and Amazon EKS.

## Project Architecture

GitHub → GitHub Actions → Pytest → Docker Image Build → Docker Hub → Kubernetes / Amazon EKS

## Technologies Used

- **Programming:** Python, Flask
- **Testing:** Pytest
- **Version Control:** Git, GitHub
- **CI/CD:** GitHub Actions
- **Containerization:** Docker, Docker Hub
- **Orchestration:** Kubernetes
- **Cloud:** AWS, Amazon EKS
- **Operating System:** Linux

## Project Features

- Automated application testing using Pytest.
- CI pipeline triggered by changes pushed to GitHub.
- Automated Docker image build and publishing to Docker Hub.
- Kubernetes deployment with two application replicas.
- ConfigMap and Secret-based application configuration.
- Readiness and liveness probes for application health monitoring.
- Kubernetes Service for application access.
- Persistent volume and persistent volume claim implementation.
- Amazon EKS deployment with application health verification.

## CI/CD Pipeline

GitHub Actions automates the continuous integration workflow by running application tests and building the Docker image. Successful workflow execution publishes the image to Docker Hub, making it available for deployment.

## Kubernetes Deployment

The application was deployed to a Kubernetes cluster with two replicas.

The implementation includes:
- Deployment and replica management.
- Kubernetes Service configuration.
- ConfigMaps and Secrets.
- Readiness and liveness probes.
- Resource requests and limits.
- Persistent volumes and persistent volume claims.
- Application health checks.

## Amazon EKS Deployment

The Flask application was successfully deployed to Amazon Elastic Kubernetes Service (EKS) in the AWS Mumbai region (`ap-south-1`).

The deployment was validated by confirming that both application pods reached the Running state and that the health endpoint returned HTTP 200.

Health endpoint:

`/health`

Expected response:

`{"status":"healthy"}`

## Docker Hub

Published application image:

https://hub.docker.com/r/ajithcr/devops-flask-project

## Automated Tests

Run the test suite from the project directory:

```bash
./venv/bin/pytest -v
```

## Repository Contents

The repository includes the Flask application, automated tests, Docker configuration, GitHub Actions workflow, Kubernetes manifests, and project documentation.

## Skills Demonstrated

- CI/CD pipeline implementation
- Automated testing
- Docker image creation and publishing
- Kubernetes deployment and troubleshooting
- Application health monitoring
- Configuration and secret management
- Persistent storage concepts
- AWS EKS deployment and validation
- Linux command-line operations
- Git-based version control
