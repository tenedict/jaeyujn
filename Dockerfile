# 베이스 이미지
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요 패키지 설치
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Django 소스 복사
COPY . .

# static 파일 수집
RUN python manage.py collectstatic --noinput

# 포트 설정
# EXPOSE 8000

# 애플리케이션 실행
# CMD ["gunicorn", "--bind", "34.64.220.15:8000", "canieat.wsgi:application"]

# RUN mkdir -p /app/staticfiles
# RUN python manage.py collectstatic --noinput
