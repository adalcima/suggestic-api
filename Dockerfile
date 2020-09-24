FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r flask_app/requirements.txt

EXPOSE 5000

# run the command
CMD ["python", "flask_app/app.py"]
