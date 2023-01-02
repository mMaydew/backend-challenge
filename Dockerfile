FROM python:3.11.1-slim-bullseye
WORKDIR /backend
COPY ./backend/ /backend/
RUN pip install -r requirements.txt -r api/requirements.txt
CMD ["python", "api/app.py"]
