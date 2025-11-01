# 🖼️ Python Image Blog Project

Django REST Framework와 Python을 사용하여 이미지 업로드 및 블로그 게시글 관리를 학습용으로 구현한 Python Image Blog 프로젝트

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
- Python 3.13 버전이 설치되어 있는지 확인합니다

```bash
python --version
```

### 2. 프로젝트 클론
- GitHub에서 프로젝트를 로컬로 복제합니다

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
  
## 🚀 API 사용 및 테스트 방법

이 프로젝트는 DRF의 TokenAuthentication을 사용하도록 설정되어 있습니다. 서버의 기본 설정(`REST_FRAMEWORK`)에서 전역으로 인증을 요구하도록 되어 있으므로, API를 호출하려면 먼저 토큰을 발급받아 Authorization 헤더에 포함시켜야 합니다.

### 주요 API 엔드포인트
- 토큰 발급: `POST /api-token-auth/` (username, password로 요청)
- 게시글 목록 조회: GET /api/posts
- 게시글 생성: POST /api_root/Post/
- 게시글 수정: PATCH /api_root/Post/{id}/
- 게시글 삭제: DELETE /api_root/Post/{id}/
- 게시글 검색: GET /api/posts/search/?q={query}

- API 루트(router): `GET /api_root/`  

### 1) 토큰 발급 (예)
- 요청: `POST http://127.0.0.1:8000/api-token-auth/`  
- 바디(JSON):

```json
{"username":"youruser","password":"yourpass"}
```

응답 예: `{"token":"abcdef123..."}`


### 2) 보호된 API 호출
토큰을 받은 뒤 요청 헤더에 다음을 추가하세요:

```
Authorization: Token <your_token_here>
```

- curl 예 (게시물 리스트 조회):

```bash
curl -H "Authorization: Token abcdef123..." http://127.0.0.1:8000/api/posts/
```

### 3) 토큰 관리
- 기본 DRF Token은 사용자당 하나가 생성됩니다(`Token.objects.get_or_create(user=...)`). 동일한 사용자로 반복 요청하면 기존 토큰을 재사용합니다.  
- 토큰을 무효화하려면 Django shell 또는 전용 엔드포인트로 토큰을 삭제할 것.


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
