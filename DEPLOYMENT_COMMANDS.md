# 🚀 Complete Deployment Commands for Lab Report

## Prerequisites Setup

### 1. MongoDB Atlas Setup
1. Go to [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Create free account and cluster
3. Create database user
4. Get connection string
5. Update `.env` file with your connection string

### 2. Docker Hub Account
1. Create account at [Docker Hub](https://hub.docker.com)
2. Note your username for image tagging

## 📋 Step-by-Step Commands

### STEP 1: Local App Setup & Testing

```bash
# Install dependencies
npm install

# Configure MongoDB Atlas connection in .env file first!
# Then test locally
npm start
# Visit http://localhost:3000 to test the app
```

### STEP 2: Docker Build & Local Testing

```bash
# Build Docker image
docker build -t feedback-app .

# Run Docker container (connects to MongoDB Atlas)
docker run -p 3000:3000 --env-file .env feedback-app

# Test in browser: http://localhost:3000
# Stop container: Ctrl+C
```

### STEP 3: Docker Hub Push

```bash
# Replace <your-dockerhub-username> with your actual Docker Hub username
docker tag feedback-app <your-dockerhub-username>/feedback-app:v1
docker push <your-dockerhub-username>/feedback-app:v1

# Example:
# docker tag feedback-app johndoe/feedback-app:v1
# docker push johndoe/feedback-app:v1
```

### STEP 4: Azure Kubernetes Service (AKS) Deployment

```bash
# Login to Azure
az login

# Create resource group
az group create --name MyResourceGroup --location eastus

# Create AKS cluster (this takes 5-10 minutes)
az aks create --resource-group MyResourceGroup --name feedbackCluster --node-count 1 --generate-ssh-keys

# Get cluster credentials
az aks get-credentials --resource-group MyResourceGroup --name feedbackCluster

# IMPORTANT: Update deployment.yaml before applying
# 1. Replace <your-dockerhub-username> with your Docker Hub username
# 2. Replace MongoDB connection string with your Atlas connection string

# Deploy to Kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Get public IP (may take 2-3 minutes to assign)
kubectl get service feedback-app-service

# Check deployment status
kubectl get pods
kubectl get deployments
```

### STEP 5: GitHub Repository Setup

```bash
# Initialize git repository
git init

# Add all files
git add .

# Initial commit
git commit -m "Initial commit - Cloud Feedback App"

# Set main branch
git branch -M main

# Add remote origin (replace <username> with your GitHub username)
git remote add origin https://github.com/<username>/cloud-feedback-app.git

# Push to GitHub
git push -u origin main
```

## 🔍 Verification Commands

### Check Docker Image
```bash
docker images | grep feedback-app
```

### Check Kubernetes Deployment
```bash
kubectl get all
kubectl describe service feedback-app-service
kubectl logs -l app=feedback-app
```

### Test Application
```bash
# Get external IP
kubectl get service feedback-app-service

# Test health endpoint
curl http://<EXTERNAL-IP>/health

# Test in browser
# Open http://<EXTERNAL-IP> in browser
```

## 📸 Screenshots to Take for Lab Report

1. **Local Docker Run**: Terminal showing `docker run` command and success message
2. **Docker Hub**: Your pushed image on Docker Hub website
3. **AKS Cluster**: Azure portal showing your AKS cluster
4. **Kubectl Output**: Terminal showing `kubectl get service` with EXTERNAL-IP
5. **Application Running**: Browser showing your app running on Azure public IP
6. **GitHub Repository**: Your GitHub repo with all files

## 🎯 Final Deliverables for Lab Report

### Links to Include:
- **GitHub Repo**: `https://github.com/<username>/cloud-feedback-app`
- **Docker Hub Image**: `https://hub.docker.com/r/<username>/feedback-app`
- **Azure Public URL**: `http://<EXTERNAL-IP>` (from kubectl get service)

### Commands Summary for Report:
```bash
# Local Development
npm install && npm start

# Docker
docker build -t feedback-app .
docker run -p 3000:3000 --env-file .env feedback-app
docker tag feedback-app <username>/feedback-app:v1
docker push <username>/feedback-app:v1

# Azure Kubernetes
az aks create --resource-group MyResourceGroup --name feedbackCluster --node-count 1
az aks get-credentials --resource-group MyResourceGroup --name feedbackCluster
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get service feedback-app-service

# GitHub
git init && git add . && git commit -m "Initial commit"
git remote add origin https://github.com/<username>/cloud-feedback-app.git
git push -u origin main
```

## ⚠️ Important Notes

1. **Replace Placeholders**: Update all `<username>`, `<your-dockerhub-username>`, and MongoDB connection strings
2. **Wait Times**: AKS creation takes 5-10 minutes, LoadBalancer IP assignment takes 2-3 minutes
3. **Costs**: Remember to delete Azure resources after lab to avoid charges:
   ```bash
   az group delete --name MyResourceGroup --yes --no-wait
   ```

## 🆘 Troubleshooting

### If pods are not running:
```bash
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

### If external IP is pending:
```bash
# Wait 2-3 minutes, then check again
kubectl get service feedback-app-service -w
```

### If MongoDB Atlas connection fails:
- Check your Atlas connection string in .env file
- Ensure IP whitelist includes 0.0.0.0/0 (allow access from anywhere) for testing
- Verify username/password in connection string
- Make sure your Atlas cluster is running (not paused)