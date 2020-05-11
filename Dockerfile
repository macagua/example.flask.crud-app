FROM python:3.6

# install postgres client and python-dev
RUN apt-get update && apt-get install -y postgresql-client python3-dev

WORKDIR /usr/src/app

# install requirements first
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy the application
COPY . .

# install the application
RUN pip install -e .

EXPOSE 8087

CMD ["python", "bookmanager.py"]

