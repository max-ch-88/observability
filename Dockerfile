FROM python:3.9.17-slim-bullseye
WORKDIR /app
RUN apt update && \
    apt install -y git && \
    pip install flask flask_sqlalchemy && \
    git clone https://github.com/Zenahr/flask-sqlite3-todo-crud.git /app && \
    mkdir /app/instance && \
    mv /app/todo.db /app/instance/todo.db
EXPOSE 5050/tcp
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5050"]