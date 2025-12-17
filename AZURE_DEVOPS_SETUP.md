# 🔵 Azure DevOps Pipeline Setup Guide

## 📋 Prerequisites
- Azure DevOps account (free at dev.azure.com)
- GitHub repository with your code
- Docker Hub account
- Azure subscription with AKS cluster

---

## 🚀 Step-by-Step Setup

### Step 1: Create Azure DevOps Organization & Project

1. **Go to Azure DevOps**
   - Visit: https://dev.azure.com
   - Sign in with Microsoft account

2. **Create Organization** (if needed)
   - Click "New organization"
   - Name: `YourOrganization`

3. **Create Project**
   - Click "New project"
   - Project name: `cloud-feedback-app`
   - Visibility: Private
   - Version control: Git
   - Click "Create"

---

### Step 2: Connect GitHub Repository

1. **Go to Project Settings**
   - Click gear icon (⚙️) at bottom left
   - Select "Service connections"

2. **Create GitHub Connection**
   - Click "New service connection"
   - Select "GitHub"
   - Click "Next"
   - Choose "Grant authorization"
   - Authorize Azure Pipelines
   - Service connection name: `GitHubConnection`
   - Click "Save"

---

### Step 3: Configure Docker Hub Connection

1. **Create Docker Registry Connection**
   - In Service connections, click "New service connection"
   - Select "Docker Registry"
   - Click "Next"

2. **Configure Docker Hub**
   - Registry type: Docker Hub
   - Docker ID: `shahzaman14`
   - Docker Password: `your_docker_hub_password`
   - Service connection name: `DockerHubConnection`
   - Grant access to all pipelines: ✅
   - Click "Save"

---

### Step 4: Configure Azure Service Connection

1. **Create Azure Resource Manager Connection**
   - In Service connections, click "New service connection"
   - Select "Azure Resource Manager"
   - Click "Next"

2. **Authentication Method**
   - Choose "Service principal (automatic)"
   - Click "Next"

3. **Configure Connection**
   - Scope level: Subscription
   - Subscription: Select your Azure subscription
   - Resource group: `MyResourceGroup`
   - Service connection name: `AzureServiceConnection`
   - Grant access to all pipelines: ✅
   - Click "Save"

---

### Step 5: Create the Pipeline

1. **Go to Pipelines**
   - Click "Pipelines" in left menu
   - Click "Create Pipeline" or "New pipeline"

2. **Connect to Code**
   - Select "GitHub (YAML)"
   - Select your repository: `shahzaman14/cloud-feedback-app`
   - Authorize if prompted

3. **Configure Pipeline**
   - Select "Existing Azure Pipelines YAML file"
   - Branch: `main`
   - Path: `/azure-pipelines.yml`
   - Click "Continue"

4. **Review and Run**
   - Review the pipeline YAML
   - Click "Run"

---

### Step 6: Configure Pipeline Variables (Optional)

1. **Edit Pipeline**
   - Go to Pipelines → Select your pipeline
   - Click "Edit"
   - Click "Variables" (top right)

2. **Add Variables** (if needed)
   ```
   dockerRegistryServiceConnection: DockerHubConnection
   azureSubscription: AzureServiceConnection
   azureResourceGroup: MyResourceGroup
   kubernetesCluster: feedbackCluster
   ```

3. **Save**

---

## 🎯 Running the Pipeline

### Method 1: Automatic Trigger (Push)
```bash
# Make a change to your code
git add .
git commit -m "Trigger pipeline"
git push origin main

# Pipeline will automatically start
```

### Method 2: Manual Run
1. Go to Pipelines
2. Select your pipeline
3. Click "Run pipeline"
4. Select branch: `main`
5. Click "Run"

### Method 3: Pull Request Trigger
1. Create a new branch
2. Make changes
3. Push to GitHub
4. Create Pull Request to `main`
5. Pipeline runs automatically

---

## 📊 Monitoring Pipeline Execution

### View Pipeline Run
1. Go to Pipelines
2. Click on your pipeline
3. Click on the running/completed run
4. View stages and jobs

### View Logs
1. Click on any stage
2. Click on any job
3. View detailed logs
4. Download logs if needed

### View Test Results
1. In pipeline run, click "Tests" tab
2. View test results
3. Download test reports

---

## 📸 Taking Screenshots for Submission

### Screenshot 1: Pipeline Overview
```
Pipelines → Select pipeline → Latest run
Shows: All 5 stages with green checkmarks
```

### Screenshot 2: Build Stage Details
```
Click on "Build" stage → View jobs
Shows: BuildFrontend and BuildBackend completed
```

### Screenshot 3: Test Stage Details
```
Click on "Test" stage → View jobs
Shows: Tests executed and results
```

### Screenshot 4: Docker Build & Push
```
Click on "DockerBuildPush" stage
Shows: 3 images built and pushed
```

### Screenshot 5: Deploy to AKS
```
Click on "DeployToAKS" stage
Shows: Kubernetes deployment successful
```

### Screenshot 6: Verification
```
Click on "Verify" stage
Shows: Health check passed
```

---

## 🔍 Verifying Deployment

### Check Docker Hub
1. Go to https://hub.docker.com
2. Login with your account
3. Check repositories:
   - `shahzaman14/feedback-frontend`
   - `shahzaman14/feedback-backend`
   - `shahzaman14/feedback-mongodb`
4. Verify tags: `latest` and build number

### Check AKS Deployment
```bash
# Get AKS credentials
az aks get-credentials --resource-group MyResourceGroup --name feedbackCluster

# Check pods
kubectl get pods -n feedback-app

# Check services
kubectl get svc -n feedback-app

# Get external IP
kubectl get svc frontend -n feedback-app
```

---

## 🛠️ Troubleshooting

### Issue: Service Connection Failed
**Solution:**
1. Go to Project Settings → Service connections
2. Click on the connection
3. Click "Verify"
4. If failed, click "Edit" and re-authorize

### Issue: Docker Push Failed
**Solution:**
1. Verify Docker Hub credentials
2. Check service connection: `DockerHubConnection`
3. Ensure Docker Hub account is active
4. Check image name format

### Issue: AKS Deployment Failed
**Solution:**
1. Verify AKS cluster exists:
   ```bash
   az aks list --resource-group MyResourceGroup
   ```
2. Check Azure service connection
3. Verify kubectl has permissions
4. Check if namespace exists

### Issue: Pipeline Not Triggering
**Solution:**
1. Check trigger configuration in YAML
2. Verify GitHub connection
3. Check branch name matches trigger
4. Ensure webhook is configured

---

## 📋 Pipeline Status Indicators

| Status | Meaning |
|--------|---------|
| 🟢 Green checkmark | Stage/Job completed successfully |
| 🔴 Red X | Stage/Job failed |
| 🟡 Yellow circle | Stage/Job in progress |
| ⚪ Gray circle | Stage/Job not started |
| 🔵 Blue circle | Stage/Job queued |

---

## 🎓 Best Practices

1. **Use Service Connections**
   - Never hardcode credentials
   - Use service connections for security

2. **Version Your Images**
   - Tag with build ID
   - Keep 'latest' tag updated

3. **Test Before Deploy**
   - Always run tests before deployment
   - Use stage dependencies

4. **Monitor Deployments**
   - Check logs regularly
   - Set up alerts for failures

5. **Use Environments**
   - Separate dev/staging/prod
   - Require approvals for production

---

## ✅ Verification Checklist

Before submission, verify:
- [ ] Pipeline file (`azure-pipelines.yml`) exists
- [ ] All service connections configured
- [ ] Pipeline runs successfully
- [ ] All 5 stages complete
- [ ] Docker images pushed to Docker Hub
- [ ] Application deployed to AKS
- [ ] Screenshots captured
- [ ] Documentation complete

---

## 🚀 Quick Reference Commands

### Azure CLI
```bash
# Login
az login

# List AKS clusters
az aks list --resource-group MyResourceGroup

# Get credentials
az aks get-credentials --resource-group MyResourceGroup --name feedbackCluster
```

### Kubectl
```bash
# Get pods
kubectl get pods -n feedback-app

# Get services
kubectl get svc -n feedback-app

# View logs
kubectl logs -l app=backend -n feedback-app

# Describe pod
kubectl describe pod POD_NAME -n feedback-app
```

### Docker
```bash
# Login to Docker Hub
docker login

# List images
docker images

# Push image
docker push shahzaman14/feedback-frontend:latest
```

---

## 📞 Support Resources

- **Azure DevOps Docs**: https://docs.microsoft.com/azure/devops
- **Azure Pipelines**: https://docs.microsoft.com/azure/devops/pipelines
- **AKS Documentation**: https://docs.microsoft.com/azure/aks
- **Docker Hub**: https://hub.docker.com

---

**Setup Complete!** 🎉

Your Azure DevOps CI/CD pipeline is now ready for Section B submission.