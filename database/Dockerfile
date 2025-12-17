# Database Dockerfile - MongoDB with initialization
FROM mongo:7

# Copy initialization script
COPY init-mongo.js /docker-entrypoint-initdb.d/

# Expose MongoDB port
EXPOSE 27017

# MongoDB will automatically run init scripts on first startup