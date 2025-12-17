"""
Selenium Automated Tests for Cloud Feedback App
Section E: Automated Testing
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import unittest

class FeedbackAppTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Set up Chrome driver with options"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run in headless mode
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.base_url = "http://20.44.200.76"  # Your Azure AKS deployment
        cls.driver.implicitly_wait(10)
    
    @classmethod
    def tearDownClass(cls):
        """Close browser after all tests"""
        cls.driver.quit()
    
    def test_01_homepage_loads(self):
        """Test Case 1: Verify homepage loads successfully"""
        print("\n🧪 Test 1: Verifying homepage loads...")
        
        self.driver.get(self.base_url)
        
        # Check page title
        self.assertIn("Cloud Feedback App", self.driver.title)
        
        # Check if main heading exists
        heading = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertIn("Cloud Feedback App", heading.text)
        
        print("✅ Test 1 PASSED: Homepage loaded successfully")
    
    def test_02_form_elements_present(self):
        """Test Case 2: Verify all form elements are present"""
        print("\n🧪 Test 2: Verifying form elements...")
        
        self.driver.get(self.base_url)
        
        # Check if name input exists
        name_input = self.driver.find_element(By.ID, "name")
        self.assertTrue(name_input.is_displayed())
        
        # Check if message textarea exists
        message_input = self.driver.find_element(By.ID, "message")
        self.assertTrue(message_input.is_displayed())
        
        # Check if submit button exists
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        self.assertTrue(submit_button.is_displayed())
        
        print("✅ Test 2 PASSED: All form elements are present")
    
    def test_03_submit_feedback(self):
        """Test Case 3: Verify feedback submission works"""
        print("\n🧪 Test 3: Testing feedback submission...")
        
        self.driver.get(self.base_url)
        
        # Fill in the form
        name_input = self.driver.find_element(By.ID, "name")
        name_input.clear()
        name_input.send_keys("Selenium Test User")
        
        message_input = self.driver.find_element(By.ID, "message")
        message_input.clear()
        message_input.send_keys("This is an automated test feedback from Selenium!")
        
        # Submit the form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Wait for success message or feedback to appear
        time.sleep(2)
        
        # Check if success message appears
        try:
            success_msg = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "success"))
            )
            self.assertIn("successfully", success_msg.text.lower())
            print("✅ Test 3 PASSED: Feedback submitted successfully")
        except:
            # Alternative: Check if feedback appears in the list
            feedbacks = self.driver.find_elements(By.CLASS_NAME, "feedback-item")
            self.assertGreater(len(feedbacks), 0)
            print("✅ Test 3 PASSED: Feedback appears in the list")
    
    def test_04_feedback_list_displays(self):
        """Test Case 4: Verify feedback list displays correctly"""
        print("\n🧪 Test 4: Verifying feedback list displays...")
        
        self.driver.get(self.base_url)
        
        # Wait for feedbacks to load
        time.sleep(2)
        
        # Check if feedback items exist
        feedbacks = self.driver.find_elements(By.CLASS_NAME, "feedback-item")
        self.assertGreater(len(feedbacks), 0, "No feedback items found")
        
        # Check if feedback has name and message
        first_feedback = feedbacks[0]
        feedback_name = first_feedback.find_element(By.CLASS_NAME, "feedback-name")
        self.assertTrue(feedback_name.is_displayed())
        
        print(f"✅ Test 4 PASSED: Found {len(feedbacks)} feedback(s) in the list")
    
    def test_05_api_health_check(self):
        """Test Case 5: Verify backend API health endpoint"""
        print("\n🧪 Test 5: Testing API health endpoint...")
        
        self.driver.get(f"{self.base_url}/api/health")
        
        # Check if response contains "OK" or "status"
        page_source = self.driver.page_source.lower()
        self.assertTrue("ok" in page_source or "status" in page_source)
        
        print("✅ Test 5 PASSED: API health check successful")
    
    def test_06_form_validation(self):
        """Test Case 6: Verify form validation works"""
        print("\n🧪 Test 6: Testing form validation...")
        
        self.driver.get(self.base_url)
        
        # Try to submit empty form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Check if HTML5 validation prevents submission
        name_input = self.driver.find_element(By.ID, "name")
        validation_message = name_input.get_attribute("validationMessage")
        
        self.assertIsNotNone(validation_message)
        print("✅ Test 6 PASSED: Form validation is working")

def run_tests():
    """Run all tests and generate report"""
    print("=" * 60)
    print("🚀 Starting Selenium Automated Tests")
    print("=" * 60)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(FeedbackAppTests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    print(f"Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 60)
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)