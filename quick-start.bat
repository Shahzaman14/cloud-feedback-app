@echo off
echo =========================================
echo 🚀 Cloud Feedback App - Quick Start
echo =========================================

REM Check if Docker is running
docker info >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker is not running. Please start Docker Desktop first.
    pause
    exit /b 1
)

echo.
echo 📦 Building Docker images...
docker-compose build

echo.
echo 🚀 Starting all services...
docker-compose up -d

echo.
echo ⏳ Waiting for services to start...
timeout /t 10 /nobreak >nul

echo.
echo ✅ Checking service status...
docker-compose ps

echo.
echo =========================================
echo ✅ Application is ready!
echo =========================================
echo.
echo 🌐 Access your application:
echo    Frontend: http://localhost
echo    Backend API: http://localhost:5000/api/health
echo    MongoDB: localhost:27017
echo.
echo 📊 View logs:
echo    docker-compose logs -f
echo.
echo 🛑 Stop services:
echo    docker-compose down
echo.
echo =========================================
pause