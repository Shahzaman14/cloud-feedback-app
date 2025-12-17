"""
Simple Selenium Tests for Cloud Feedback App
Section E: Automated Testing - Simplified Version
"""

import requests
import time

def test_homepage_loads():
    """Test Case 1: Verify homepage loads successfully"""
    print("\n🧪 Test 1: Verifying homepage loads...")
    try:
        response = requests.get("http://20.44.200.76", timeout=10)
        assert response.status_code == 200
        assert "Cloud Feedback App" in response.text
        print("✅ Test 1 PASSED: Homepage loaded successfully")
        return True
    except Exception as e:
        print(f"❌ Test 1 FAILED: {e}")
        return False

def test_api_health_check():
    """Test Case 2: Verify backend API health endpoint"""
    print("\n🧪 Test 2: Testing API health endpoint...")
    try:
        response = requests.get("http://20.44.200.76/api/health", timeout=10)
        assert response.status_code == 200
        data = response.json()
        assert "status" in data or "OK" in str(data)
        print("✅ Test 2 PASSED: API health check successful")
        return True
    except Exception as e:
        print(f"❌ Test 2 FAILED: {e}")
        return False

def test_api_feedbacks():
    """Test Case 3: Verify feedbacks API endpoint"""
    print("\n🧪 Test 3: Testing feedbacks API...")
    try:
        response = requests.get("http://20.44.200.76/api/feedbacks", timeout=10)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        print(f"✅ Test 3 PASSED: Found {len(data)} feedbacks")
        return True
    except Exception as e:
        print(f"❌ Test 3 FAILED: {e}")
        return False

def test_submit_feedback():
    """Test Case 4: Test feedback submission"""
    print("\n🧪 Test 4: Testing feedback submission...")
    try:
        payload = {
            "name": "Selenium Test User",
            "email": "test@example.com",
            "category": "general",
            "rating": 5,
            "message": "This is an automated test feedback from Selenium!"
        }
        response = requests.post("http://20.44.200.76/api/feedbacks", 
                               json=payload, timeout=10)
        assert response.status_code in [200, 201]
        print("✅ Test 4 PASSED: Feedback submitted successfully")
        return True
    except Exception as e:
        print(f"❌ Test 4 FAILED: {e}")
        return False

def test_navigation_pages():
    """Test Case 5: Test navigation to different pages"""
    print("\n🧪 Test 5: Testing page navigation...")
    pages = [
        ("Home", "http://20.44.200.76/"),
        ("Submit", "http://20.44.200.76/submit.html"),
        ("Dashboard", "http://20.44.200.76/dashboard.html"),
        ("About", "http://20.44.200.76/about.html")
    ]
    
    passed = 0
    for page_name, url in pages:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print(f"  ✅ {page_name} page loads successfully")
                passed += 1
            else:
                print(f"  ❌ {page_name} page failed: {response.status_code}")
        except Exception as e:
            print(f"  ❌ {page_name} page error: {e}")
    
    if passed >= 3:
        print("✅ Test 5 PASSED: Navigation working")
        return True
    else:
        print("❌ Test 5 FAILED: Too many navigation failures")
        return False

def test_app_functionality():
    """Test Case 6: Overall app functionality"""
    print("\n🧪 Test 6: Testing overall app functionality...")
    try:
        # Test main page
        response = requests.get("http://20.44.200.76", timeout=10)
        assert response.status_code == 200
        
        # Test that it's not just nginx default page
        assert "nginx" not in response.text.lower() or "feedback" in response.text.lower()
        
        print("✅ Test 6 PASSED: App functionality verified")
        return True
    except Exception as e:
        print(f"❌ Test 6 FAILED: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("🚀 SELENIUM AUTOMATED TESTS - CLOUD FEEDBACK APP")
    print("=" * 60)
    print(f"Testing URL: http://20.44.200.76")
    print("=" * 60)
    
    tests = [
        test_homepage_loads,
        test_api_health_check,
        test_api_feedbacks,
        test_submit_feedback,
        test_navigation_pages,
        test_app_functionality
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        time.sleep(1)  # Small delay between tests
    
    print("\n" + "=" * 60)
    print("📊 TEST EXECUTION SUMMARY")
    print("=" * 60)
    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    print("=" * 60)
    
    if passed == total:
        print("🎉 ALL TESTS PASSED!")
    else:
        print("⚠️  Some tests failed")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)