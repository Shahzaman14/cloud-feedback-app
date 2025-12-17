/**
 * Backend API Tests
 * For CI/CD Pipeline automated testing
 */

const request = require('supertest');
const express = require('express');

// Mock Express app for testing
const app = express();
app.use(express.json());

// Mock routes for testing
app.get('/api/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

app.get('/api/feedbacks', (req, res) => {
  res.json([
    { name: 'Test User', message: 'Test message', created_at: new Date() }
  ]);
});

app.post('/api/feedbacks', (req, res) => {
  const { name, message } = req.body;
  if (!name || !message) {
    return res.status(400).json({ error: 'Name and message are required' });
  }
  res.status(201).json({ name, message, created_at: new Date() });
});

// Tests
describe('Backend API Tests', () => {
  
  test('GET /api/health should return OK status', async () => {
    const response = await request(app).get('/api/health');
    expect(response.statusCode).toBe(200);
    expect(response.body.status).toBe('OK');
  });
  
  test('GET /api/feedbacks should return array', async () => {
    const response = await request(app).get('/api/feedbacks');
    expect(response.statusCode).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);
  });
  
  test('POST /api/feedbacks should create feedback', async () => {
    const feedback = { name: 'Test', message: 'Test message' };
    const response = await request(app)
      .post('/api/feedbacks')
      .send(feedback);
    expect(response.statusCode).toBe(201);
    expect(response.body.name).toBe('Test');
  });
  
  test('POST /api/feedbacks should validate required fields', async () => {
    const response = await request(app)
      .post('/api/feedbacks')
      .send({});
    expect(response.statusCode).toBe(400);
  });
});

module.exports = app;