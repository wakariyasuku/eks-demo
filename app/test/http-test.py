import requests

def test_http_request():
    try:
        response = requests.get('http://localhost:8501')
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        print("HTTP request test passed!")
    except Exception as e:
        print(f"HTTP request test failed: {e}")
        exit(1)

if __name__ == "__main__":
    test_http_request()
