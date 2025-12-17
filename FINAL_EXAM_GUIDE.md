# 🎓 DevOps Final Exam - Complete Implementation Guide

## 📋 Project Overview
**3-Tier Cloud Feedback Application**
- **Frontend**: Nginx serving static HTML
- **Backend**: Node.js Express API
- **Database**: MongoDB

---

## 📁 Project Structure
```
cloud-feedback-app/
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   └── nginx.conf
├── backend/
│   ├── Dockerfile
│   ├── server.js
│   ├── server.test.js
│   ├── package.json
│   └── .env
├── database/
│   ├── Dockerfile
│   └── init-mongo.js
├── k8s/
│   ├── namespace.yaml
│   ├── mongodb-deployment.yaml
│   ├── backend-deployment.yaml
│   ├── frontend-deployment.yaml
│   └── services.yaml
├── ansible/
│   ├── hosts.ini
│   └── playbook.yml
├── tests/
│   ├── selenium_tests.py
│   └── requirements.txt
├── .github/workflows/
│   └── ci-cd.yml
└── docker-compose.yml
```

---

## SECTION A: CONTAINERIZATION (10 Marks)

### Task A1: Docker Images ✅

**1. Frontend Dockerfile** (`frontend/Dockerfile`)
```bash
cd frontend
docker build -t feedback-frontend .
```

**2. Backend Dockerfile** (`backend/Dockerfile`)
```bash
cd backend
docker build -t feedback-backend .
```

**3. Database Dockerfile** (`database/Dockerfile`)
```bash
cd database
docker build -t feedback-mongodb .
```

### Task A2: Docker Compose ✅

**Run all services:**
```bash
# Start all containers
docker-compose up -d

# Check running containers
docker-compose ps

# View logs
docker-compose logs -f

# Stop all containers
docker-compose down
```

**Access the application:**
- Frontend: http://localhost
- Backend API: http://localhost:5000/api/health
- MongoDB: localhost:27017

**📸 Screenshot Requirements:**
```bash
# Take screenshot of this command output
docker-compose ps
docker ps
```

---

## SECTION B: CI/CD AUTOMATION (14 Marks)

### Task B1: Pipeline Development ✅

**GitHub Actions Pipeline** (`.github/workflows/ci-cd.yml`)

**Pipeline Stages:**
1. ✅ Build Stage (Frontend + Backend)
2. ✅ Automated Tests
3. ✅ Docker Image Build & Push
4. ✅ Deployment to Kubernetes

### Task B2: Trigger Configuration ✅

**Pipeline triggers on:**
- Push to `main` or `develop` branch
- Pull requests to `main` branch

**Setup GitHub Secrets:**
```bash
# Go to GitHub Repository → Settings → Secrets → Actions
# Add these secrets:
DOCKER_USERNAME=shahzaman14
DOCKER_PASSWORD=your_docker_hub_password
AZURE_CREDENTIALS=your_azure_credentials_json
```

**📸 Screenshot Requirements:**
- GitHub Actions workflow run (all stages green)
- Pipeline execution logs

---

## SECTION C: KUBERNETES ON AZURE (AKS) (12 Marks)

### Task C1: Kubernetes Manifests ✅

**Deploy to AKS:**

```bash
# 1. Create AKS cluster
az group create --name MyResourceGroup --location southeastasia
az aks create --resource-group MyResourceGroup --name feedbackCluster --node-count 2 --generate-ssh-keys

# 2. Get credentials
az aks get-credentials --resource-group MyResourceGroup --name feedbackCluster

# 3. Build and push Docker images
docker build -t shahzaman14/feedback-frontend:latest ./frontend
docker build -t shahzaman14/feedback-backend:latest ./backend
docker build -t shahzaman14/feedback-mongodb:latest ./database

docker push shahzaman14/feedback-frontend:latest
docker push shahzaman14/feedback-backend:latest
docker push shahzaman14/feedback-mongodb:latest

# 4. Deploy to Kubernetes
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/mongodb-deployment.yaml
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/services.yaml

# 5. Get external IP
kubectl get services -n feedback-app
kubectl get pods -n feedback-app
```

### Task C2: AKS Deployment Verification ✅

**Verification Commands:**
```bash
# Check all pods are running
kubectl get pods -n feedback-app

# Check services
kubectl get svc -n feedback-app

# Check deployments
kubectl get deployments -n feedback-app

# View logs
kubectl logs -l app=backend -n feedback-app
kubectl logs -l app=frontend -n feedback-app
kubectl logs -l app=mongodb -n feedback-app

# Describe service to get external IP
kubectl describe svc frontend -n feedback-app
```

**📸 Screenshot Requirements:**
- `kubectl get pods -n feedback-app` (all Running)
- `kubectl get svc -n feedback-app` (with EXTERNAL-IP)
- Browser showing app running on public IP

---

## SECTION D: CONFIGURATION MANAGEMENT USING ANSIBLE (8 Marks)

### Task D1: Inventory Setup ✅

**File:** `ansible/hosts.ini`

**Update with your server IPs:**
```ini
[webservers]
server1 ansible_host=YOUR_SERVER_IP ansible_user=ubuntu

[dbservers]
dbserver1 ansible_host=YOUR_DB_SERVER_IP ansible_user=ubuntu
```

### Task D2: Playbook ✅

**Run Ansible Playbook:**
```bash
# Install Ansible
pip install ansible

# Test connection
ansible all -i ansible/hosts.ini -m ping

# Run playbook
ansible-playbook -i ansible/hosts.ini ansible/playbook.yml

# Run with verbose output
ansible-playbook -i ansible/hosts.ini ansible/playbook.yml -v
```

**What the playbook does:**
- ✅ Installs Docker
- ✅ Installs Node.js & npm
- ✅ Installs Nginx
- ✅ Installs MongoDB
- ✅ Configures firewall
- ✅ Creates application directories

**📸 Screenshot Requirements:**
- Playbook execution output (all tasks OK/Changed)
- `ansible all -m ping` output

---

## SECTION E: SELENIUM AUTOMATED TESTING (6 Marks)

### Task E1: Test Cases ✅

**6 Test Cases Implemented:**
1. ✅ Verify homepage loads
2. ✅ Validate form elements present
3. ✅ Test feedback submission
4. ✅ Verify feedback list displays
5. ✅ API health check
6. ✅ Form validation

### Task E2: Execution Report ✅

**Run Selenium Tests:**
```bash
# Install dependencies
cd tests
pip install -r requirements.txt

# Install Chrome driver
pip install webdriver-manager

# Run tests (make sure app is running)
python selenium_tests.py

# Or run with pytest
pytest selenium_tests.py -v --html=report.html
```

**📸 Screenshot Requirements:**
- Test execution output showing all tests passed
- Test report (if using pytest-html)

---

## 🚀 Complete Deployment Commands

### Local Development
```bash
# Start with Docker Compose
docker-compose up -d

# Access at http://localhost
```

### Production Deployment to AKS
```bash
# 1. Build images
docker-compose build

# 2. Tag for Docker Hub
docker tag feedback-frontend shahzaman14/feedback-frontend:latest
docker tag feedback-backend shahzaman14/feedback-backend:latest
docker tag feedback-mongodb shahzaman14/feedback-mongodb:latest

# 3. Push to Docker Hub
docker push shahzaman14/feedback-frontend:latest
docker push shahzaman14/feedback-backend:latest
docker push shahzaman14/feedback-mongodb:latest

# 4. Deploy to AKS
kubectl apply -f k8s/

# 5. Get public URL
kubectl get svc frontend -n feedback-app
```

---

## 📸 Screenshot Checklist for Submission

### Section A (Containerization)
- [ ] `docker-compose ps` showing all 3 containers running
- [ ] `docker ps` output
- [ ] Browser showing app at http://localhost

### Section B (CI/CD)
- [ ] GitHub Actions workflow file
- [ ] Pipeline run showing all stages completed
- [ ] Docker Hub showing pushed images

### Section C (Kubernetes/AKS)
- [ ] `kubectl get pods -n feedback-app` (all Running)
- [ ] `kubectl get svc -n feedback-app` (with EXTERNAL-IP)
- [ ] Browser showing app on Azure public IP
- [ ] Azure Portal showing AKS cluster

### Section D (Ansible)
- [ ] `ansible/hosts.ini` file
- [ ] `ansible/playbook.yml` file
- [ ] Playbook execution output (successful)

### Section E (Selenium)
- [ ] `selenium_tests.py` code
- [ ] Test execution output (all passed)
- [ ] Test report

---

## 🎯 Final Deliverables

1. **GitHub Repository**: https://github.com/shahzaman14/cloud-feedback-app
2. **Docker Hub Images**:
   - shahzaman14/feedback-frontend:latest
   - shahzaman14/feedback-backend:latest
   - shahzaman14/feedback-mongodb:latest
3. **Azure Public URL**: http://YOUR-EXTERNAL-IP
4. **All Screenshots** in a PDF/Word document
5. **Documentation** explaining each section

---

## 🆘 Troubleshooting

### Docker Compose Issues
```bash
# Remove all containers and volumes
docker-compose down -v

# Rebuild images
docker-compose build --no-cache

# Start fresh
docker-compose up -d
```

### Kubernetes Issues
```bash
# Check pod logs
kubectl logs POD_NAME -n feedback-app

# Describe pod for events
kubectl describe pod POD_NAME -n feedback-app

# Restart deployment
kubectl rollout restart deployment/backend -n feedback-app
```

### Ansible Issues
```bash
# Test SSH connection
ssh ubuntu@YOUR_SERVER_IP

# Run with verbose mode
ansible-playbook -i hosts.ini playbook.yml -vvv
```

---

## ✅ Marks Distribution

- **Section A**: 10 marks (Dockerfiles + Docker Compose)
- **Section B**: 14 marks (CI/CD Pipeline)
- **Section C**: 12 marks (Kubernetes/AKS)
- **Section D**: 8 marks (Ansible)
- **Section E**: 6 marks (Selenium Tests)
- **Total**: 50 marks

Good luck with your exam! 🎓