FROM python:3.7
WORKDIR /app
COPY . /app
RUN pip install pipenv
RUN pipenv install
EXPOSE 80
CMD ["pipenv", "run", "python", "main.py"]
