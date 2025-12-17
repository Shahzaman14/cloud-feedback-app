// MongoDB initialization script
db = db.getSiblingDB('feedbackdb');

// Create collection
db.createCollection('feedbacks');

// Create indexes
db.feedbacks.createIndex({ "created_at": -1 });
db.feedbacks.createIndex({ "name": 1 });

// Insert sample data
db.feedbacks.insertMany([
  {
    name: "Demo User",
    message: "Welcome to the Cloud Feedback App! This is a sample feedback from the database.",
    created_at: new Date()
  },
  {
    name: "Test User",
    message: "This 3-tier architecture includes Frontend (Nginx), Backend (Node.js), and Database (MongoDB)!",
    created_at: new Date()
  }
]);

print('✅ Database initialized successfully with sample data');