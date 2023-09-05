# 베이스 이미지를 선택합니다. Python 3.x 버전을 사용하려면 해당 버전을 선택합니다.
FROM python:3.11

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# 애플리케이션 종속성을 설치합니다.
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# 애플리케이션 코드를 복사합니다.
COPY . /app/

# 애플리케이션을 실행합니다.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
