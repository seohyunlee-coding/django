# 🖼️ Python Image Blog Project

Django REST Framework와 Python을 사용하여 이미지 업로드 및 블로그 게시글 관리를 학습용으로 구현한 Python Image Blog 프로젝트.

## 📂 프로젝트 구성

프로젝트의 주요 파일 및 디렉토리 구조는 다음과 같음

```bash
django-imageBlog/
├── README.md
├── .gitignore
├── mysite/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── venv/
│   │   ├── Scripts/
│   │   ├── Lib/
│   │   └── pyvenv.cfg
│   ├── mysite/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── wsgi.py
│   │   ├── settings.py
│   │   └── urls.py
│   └── blog/
│       ├── __init__.py
│       ├── apps.py
│       ├── admin.py
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── urls.py
│       ├── tests.py
│       ├── migrations/
│       │   ├── __init__.py
│       │   ├── 0001_initial.py
│       │   └── 0002_post_image.py
│       ├── templates/
│       │   └── blog/
│       │       ├── base.html
│       │       └── post_list.html
│       └── static/
│           └── css/
│               └── blog.css
```

## ⚙️ 프로그램 설치방법
### 1. Python 버전 확인
- Python 3.13 버전이 설치되어 있는지 확인합니다.

```bash
python --version
```

### 2. 프로젝트 클론
- GitHub에서 프로젝트를 로컬로 복제합니다.

```bash
git clone https://github.com/seohyunlee-coding/Python-Image-Blog
cd django-imageBlog/mysite
```

### 3. 가상환경 생성 및 활성화 (Windows 기준)
```bash
python -m venv .\venv
venv\Scripts\activate
```

### 4. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

### 5. 개발 서버 실행
```bash
python manage.py runserver
```

- 로컬 서버: http://127.0.0.1:8000/
- PythonAnywhere로 배포한 사이트: https://cwijiq.pythonanywhere.com/
  
## 🚀 API 테스트 방법
### 1. /api_root 경로에서 테스트

### 2. curl로 테스트
```bash
curl -X POST -S -H "Accept: application/json" -H "Authorization: Token [토큰]" \
-F "title=제목" \
-F "text=API 내용" \
-F "created_date=2022-06-07T18:34:00+09:00" \
-F "published_date=2022-06-07T18:34:00+09:00" \
-F "author=1" \
-F "image=@C:/Users/dev/Desktop/스크린샷_2025-10-09_185522.png;type=image/png" \
http://127.0.0.1:8000/api_root/Post/
```

## 🛠️ 사용한 기술
- Python 3.13
- Django 5.27
- Django REST Framework (DRF)
- Pillow (이미지 처리)
- curl (API 요청 테스트)
- PythonAnywhere (배포)

## 🐛 버그 및 디버그 팁
- 이미지 업로드 시 파일 경로와 이름 확인
- DRF API에서 author는 정수 PK 전달 필요
- Pillow 설치 누락 시 ImageField 오류 발생

## 📚 참고 및 출처
- Django 공식 문서: https://docs.djangoproject.com/en/5.2/ 
- Django REST Framework 문서: https://www.django-rest-framework.org/
- Pillow 문서: https://pillow.readthedocs.io/en/stable/

## 👨‍💻 프로그래머 정보
- 이름: 이서현
- 이메일: cwijiq3085@gmail.com
- GitHub: seohyunlee-coding
