import requests
import json
from datetime import datetime

def main():
    url = "http://localhost:8000/contacts"
    current_time = datetime.now().isoformat()
    body = {
        "id": 1,
        "name": "テスト太郎",
        "email": "test1@test.com",
        "url": "http://test.com",
        "gender": 1,
        "message": "テストメッセージ",
        "is_enabled": True,
        "created_at": current_time,
    }

    res=requests.post(url, data=json.dumps(body))
    print(res.json())

if __name__ == "__main__":
    main()