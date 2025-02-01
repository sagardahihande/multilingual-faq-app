# Multilingual FAQ API

## **Project Description**
This project is a backend application developed using Django to manage multilingual FAQs with WYSIWYG editor support. It allows users to store, translate, and retrieve FAQs in multiple languages, including English, Hindi, and Bengali. Caching mechanisms ensure improved API performance.

---

## **Features**
- Store FAQs with multilingual support
- Automatic translations using Google Translate
- WYSIWYG editor for rich text answers
- REST API for FAQ management
- Caching with Redis for faster responses
- Admin panel for easy FAQ management

---

## **Installation Steps**

### Prerequisites
- Python 3.9+
- Redis (for caching)
- Git

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sagardahihande/multilingual-faq-app.git
   cd faq_project
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Redis server:**
   - On Linux/MacOS:
     ```bash
     redis-server
     ```
   - On Windows, use Docker:
     ```bash
     docker run -d -p 6379:6379 redis
     ```

5. **Apply database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8000`

---

## **API Usage Examples**

### **Fetch FAQs in English (default)**
```bash
curl http://localhost:8000/api/faqs/
```

### **Fetch FAQs in Hindi**
```bash
curl http://localhost:8000/api/faqs/?lang=hi
```

### **Fetch FAQs in Bengali**
```bash
curl http://localhost:8000/api/faqs/?lang=bn
```

---

## **Running Tests**
Ensure `pytest` is installed:
```bash
pip install pytest
```

Run the tests:
```bash
pytest
```

---

## **Project Structure**
```
multilingual_faqs/
├── faqs/         # FAQ app
├── manage.py     # Django management script
├── requirements.txt  # Project dependencies
└── README.md     # Documentation
```

---

## **Contribution Guidelines**
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m 'feat: Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

---

## **Git Commit Guidelines**
- `feat`: For new features
- `fix`: For bug fixes
- `docs`: For documentation updates
- `test`: For test cases
- `refactor`: Code refactoring

---

## **Docker Support (Optional)**
Create a Docker container for deployment:

### Dockerfile Example
```Dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Build and Run Docker Container
```bash
docker build -t faq-api .
docker run -p 8000:8000 faq-api
```

---

## **Deployment (Optional)**
Deploy to Heroku, AWS, or similar platforms for production use.

---

## **Author**
Sagar Dahihande

