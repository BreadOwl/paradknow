# FROM python:3
# ENV PYTHONUNBUFFERED 1
# WORKDIR /paradknow
# ADD ./paradknow
# RUN pip install -r requirements.txt
FROM python:3.11-slim
WORKDIR /paradknow
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "paradknow.wsgi:application"]
