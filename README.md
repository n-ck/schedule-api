
## Schedule API

*Made in Python & Django *


**Instructions for running server:**
1. Create a virtual environment
2. Install all packages: pip install -r requirements.txt
3. Start server: python manage.py runserver


**Django admin credentials:**
- username: admin
- password: password123

**API Endpoints:**
- /api/schedule/get/<id>
- /api/schedule/create
- /api/schedule/delete
  
- /api/appointment/get/<id>
- /api/appointment/create
- /api/appointment/delete
  
  
**Curl:**

```curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/api/schedule/get/1```

```curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/api/appointment/get/1```