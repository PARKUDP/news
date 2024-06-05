FROM python:3.10-slim

WORKDIR /app

COPY app/ .

RUN pip install --upgrade pip
RUN pip install Flask==1.1.2 Jinja2==2.11.3 itsdangerous==2.0.1 Werkzeug==2.0.1
RUN pip3 install markupsafe==2.0.1
RUN pip install --no-cache-dir beautifulsoup4
RUN pip install --no-cache-dir flask_cors
RUN pip install --no-cache-dir requests
RUN pip install lxml

CMD ["flask", "run", "--host=0.0.0.0"]
