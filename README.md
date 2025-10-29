# 🚀 Cloud Feedback App - Complete Deployment Pipeline

A simple Node.js feedback application demonstrating a complete cloud deployment pipeline using Docker, Kubernetes, and Azure.

## 📋 Project Overview

This project demonstrates:
- **Backend**: Node.js with Express.js
- **Frontend**: Simple HTML served by Express
- **Database**: MongoDB (Atlas)
- **Containerization**: Docker
- **Orchestration**: Kubernetes (AKS)
- **CI/CD**: GitHub integration

## 🏗️ Architecture

```
User → Azure Load Balancer → AKS Cluster → Docker Containers → MongoDB Atlas
```

## 🚀 Quick Start

### 1. Local Development

```bash
# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your MongoDB Atlas connection string

# Run locally
npm start
# Visit http://localhost:3000
```

### 2. Docker Local Testing

```bash
# Build Docker image
docker build -t feedback-app .

# Run with Docker (requires MongoDB Atlas connection)
docker run -p 3000:3000 --env-file .env feedback-app
```

### 3. Docker Hub Deployment

```bash
# Tag image
docker tag feedback-app <your-dockerhub-username>/feedback-app:v1

# Push to Docker Hub
docker push <your-dockerhub-username>/feedback-app:v1
```

### 4. Azure Kubernetes Service (AKS)

```bash
# Login to Azure
az login

# Create resource group
az group create --name MyResourceGroup --location eastus

# Create AKS cluster
az aks create --resource-group MyResourceGroup --name feedbackCluster --node-count 1 --generate-ssh-keys

# Get credentials
az aks get-credentials --resource-group MyResourceGroup --name feedbackCluster

# Update deployment.yaml with your Docker Hub image
# Update deployment.yaml with your MongoDB Atlas connection string

# Deploy to Kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Get public IP
kubectl get service feedback-app-service
```

## 📁 Project Structure

```
cloud-feedback-app/
├── server.js              # Main Express application
├── package.json           # Node.js dependencies
├── Dockerfile             # Docker configuration
├── deployment.yaml        # Kubernetes deployment
├── service.yaml          # Kubernetes service (LoadBalancer)
├── .env                  # Environment variables (not in git)
├── .gitignore           # Git ignore rules
├── .dockerignore        # Docker ignore rules
└── README.md            # This file
```

## 🔧 Configuration

### Environment Variables

- `MONGO_URI`: MongoDB Atlas connection string
- `PORT`: Application port (default: 3000)

### MongoDB Atlas Setup

1. Create account at [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Create a new cluster
3. Create database user
4. Get connection string
5. Update `.env` file

## 🧪 Testing

### Local Testing
```bash
# Test health endpoint
curl http://localhost:3000/health

# Test feedback submission
curl -X POST http://localhost:3000/submit \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "name=Test User&message=Hello World"

# Get feedbacks
curl http://localhost:3000/feedbacks
```

### Docker Testing
```bash
# Build and test (requires MongoDB Atlas)
docker build -t feedback-app .
docker run -p 3000:3000 --env-file .env feedback-app
```

### Kubernetes Testing
```bash
# Check deployment status
kubectl get deployments
kubectl get pods
kubectl get services

# View logs
kubectl logs -l app=feedback-app

# Port forward for testing
kubectl port-forward service/feedback-app-service 8080:80
```

## 📊 Monitoring

### Health Checks
- Application: `GET /health`
- Kubernetes: Liveness and readiness probes configured

### Logs
```bash
# Docker logs
docker logs <container-id>

# Kubernetes logs
kubectl logs -l app=feedback-app -f
```

## 🔒 Security Features

- Non-root user in Docker container
- Resource limits in Kubernetes
- Environment variable management
- Input validation

## 🚀 Deployment Commands Summary

```bash
# 1. Local Development
npm install && npm start

# 2. Docker Build & Test
docker build -t feedback-app .
docker run -p 3000:3000 --env-file .env feedback-app

# 3. Docker Hub Push
docker tag feedback-app <username>/feedback-app:v1
docker push <username>/feedback-app:v1

# 4. AKS Deployment
az aks create --resource-group MyResourceGroup --name feedbackCluster --node-count 1
az aks get-credentials --resource-group MyResourceGroup --name feedbackCluster
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get service feedback-app-service

# 5. GitHub Setup
git init
git add .
git commit -m "Initial commit - Feedback App"
git branch -M main
git remote add origin https://github.com/<username>/cloud-feedback-app.git
git push -u origin main
```

## 📝 Lab Report Checklist

- [ ] GitHub repository created and pushed
- [ ] Docker image built and pushed to Docker Hub
- [ ] AKS cluster created and application deployed
- [ ] Public IP obtained and application accessible
- [ ] Screenshots of Docker run and AKS deployment
- [ ] All commands documented and tested

## 🔗 Links

- **GitHub Repo**: `https://github.com/<username>/cloud-feedback-app`
- **Docker Hub**: `https://hub.docker.com/r/<username>/feedback-app`
- **Azure Public URL**: `http://<public-ip>` (from LoadBalancer)

## 🎯 Learning Objectives Achieved

✅ Node.js application development  
✅ Docker containerization  
✅ Kubernetes orchestration  
✅ Azure cloud deployment  
✅ CI/CD pipeline understanding  
✅ MongoDB Atlas cloud database  
✅ Load balancer configuration  
✅ Health monitoring setup