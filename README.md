🖼️ Python Image Blog Project

Django REST Framework와 Python을 사용하여 이미지 업로드 및 블로그 게시글 관리를 학습용으로 구현한 Python Image Blog 프로젝트

📂 프로젝트 구성

프로젝트의 주요 파일 및 디렉토리 구조는 다음과 같음음

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


⚙️ 프로그램 설치방법

Python 버전 확인
Python 3.13 버전이 설치되어 있는지 확인합니다. (본 프로젝트는 파이썬 3.13과 django)

python --version


프로젝트 클론
GitHub에서 프로젝트를 로컬로 복제합니다.

git clone https://github.com/seohyunlee-coding/Python-Image-Blog
cd django-imageBlog/mysite


가상환경 생성 및 활성화 (Windows 기준)

python -m venv .\venv
venv\Scripts\activate


데이터베이스 마이그레이션

python manage.py migrate


개발 서버 실행

python manage.py runserver


로컬 서버는 기본적으로 http://127.0.0.1:8000/에서 실행됨
배포된 사이트 주소 [django Image Blog 사이트](https://cwijiq.pythonanywhere.com/)


🚀 api 테스트 방법
1. /api_root 경로에서 테스트

POST 생성

2. curl 테스트 방법
```
curl -X POST -S -H "Accept: application/json" -H "Authorization: Token [토큰]" ^
-F "title=제목" ^
-F "text=API 내용" ^
-F "created_date=2022-06-07T18:34:00+09:00" ^
-F "published_date=2022-06-07T18:34:00+09:00" ^
-F "author=1" ^
-F "image=@\"C:/Users/dev/Desktop/스크린샷 2025-10-09 185522.png\";type=image/png" ^
http://127.0.0.1:8000/api_root/Post/
```


🛠️ 사용한 기술

Python 3.13

Django 5.27

Django REST Framework (DRF)

Pillow (이미지 처리)

curl (API 요청 테스트)

PythonAnywhere로 배포

🐛 버그 및 디버그 팁

이미지 업로드 시 파일 경로와 이름 확인

DRF API에서 author는 정수 PK를 전달해야 함

Pillow 설치 누락 시 ImageField 오류 발생

📚 참고 및 출처

Django 공식 문서: https://docs.djangoproject.com/en/5.2/

Django REST Framework 문서: https://www.django-rest-framework.org/

Pillow 문서: https://pillow.readthedocs.io/en/stable/

👨‍💻 프로그래머 정보

이름: 이서현

이메일: cwijiq3085@gmail.com

GitHub: https://github.com/seohyunlee-coding
