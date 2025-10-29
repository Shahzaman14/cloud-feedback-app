const express = require('express');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

// Simple in-memory storage (no database needed)
let feedbacks = [
  {
    name: "Demo User",
    message: "Welcome to the feedback app! This is a sample feedback.",
    timestamp: new Date()
  }
];

console.log('✅ Using in-memory storage (no database required)');

// Routes
// Serve HTML form
app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cloud Feedback App</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: #f5f5f5; }
            .container { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #333; text-align: center; }
            form { margin-bottom: 30px; }
            input, textarea { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }
            button { background: #007bff; color: white; padding: 12px 30px; border: none; border-radius: 5px; cursor: pointer; }
            button:hover { background: #0056b3; }
            .feedback-item { background: #f8f9fa; padding: 15px; margin: 10px 0; border-radius: 5px; border-left: 4px solid #007bff; }
            .feedback-name { font-weight: bold; color: #007bff; }
            .feedback-time { font-size: 0.8em; color: #666; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Cloud Feedback App</h1>
            <p>Submit your feedback and see it appear below in real-time!</p>
            
            <form action="/submit" method="POST">
                <input type="text" name="name" placeholder="Your Name" required>
                <textarea name="message" placeholder="Your Feedback Message" rows="4" required></textarea>
                <button type="submit">Submit Feedback</button>
            </form>
            
            <h2>📝 Recent Feedback</h2>
            <div id="feedbacks">
                <p>Loading feedbacks...</p>
            </div>
        </div>
        
        <script>
            // Load feedbacks on page load
            async function loadFeedbacks() {
                try {
                    const response = await fetch('/feedbacks');
                    const feedbacks = await response.json();
                    const container = document.getElementById('feedbacks');
                    
                    if (feedbacks.length === 0) {
                        container.innerHTML = '<p>No feedback yet. Be the first to submit!</p>';
                        return;
                    }
                    
                    container.innerHTML = feedbacks.map(feedback => 
                        \`<div class="feedback-item">
                            <div class="feedback-name">\${feedback.name}</div>
                            <div>\${feedback.message}</div>
                            <div class="feedback-time">\${new Date(feedback.timestamp).toLocaleString()}</div>
                        </div>\`
                    ).join('');
                } catch (error) {
                    document.getElementById('feedbacks').innerHTML = '<p>Error loading feedbacks</p>';
                }
            }
            
            loadFeedbacks();
        </script>
    </body>
    </html>
  `);
});

// Get all feedbacks
app.get('/feedbacks', (req, res) => {
  try {
    // Sort by timestamp (newest first) and limit to 20
    const sortedFeedbacks = feedbacks
      .sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp))
      .slice(0, 20);
    res.json(sortedFeedbacks);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch feedbacks' });
  }
});

// Submit new feedback
app.post('/submit', (req, res) => {
  try {
    const { name, message } = req.body;
    
    if (!name || !message) {
      return res.status(400).send('Name and message are required');
    }
    
    // Add new feedback to in-memory array
    const newFeedback = {
      name: name,
      message: message,
      timestamp: new Date()
    };
    
    feedbacks.push(newFeedback);
    
    console.log(`✅ New feedback from ${name}: ${message}`);
    res.redirect('/');
  } catch (error) {
    console.error('Error saving feedback:', error);
    res.status(500).send('Error saving feedback');
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
  console.log(`📱 Open http://localhost:${PORT} in your browser`);
});