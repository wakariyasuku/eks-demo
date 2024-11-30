import requests
import time

def test_http_request():
    try:
        # Streamlit アプリケーションが起動するまで待機
        print("Waiting for Streamlit app to start...")
        time.sleep(30)  # 10秒待機（必要に応じて調整）

        # HTTPリクエストを送信
        response = requests.get('http://localhost:8501')
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        print("HTTP request test passed!")
    except Exception as e:
        print(f"HTTP request test failed: {e}")
        exit(1)

if __name__ == "__main__":
    test_http_request()
