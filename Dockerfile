FROM python:3.10-buster
ENV NAME_PROJECT=$NAME_PROJECT

WORKDIR /usr/src/app/"${NAME_PROJECT:-fastapi}"

COPY requirements.txt /usr/src/app/"${NAME_PROJECT:-fastapi}"
RUN pip install -r /usr/src/app/"${NAME_PROJECT:-fastapi}"/requirements.txt
COPY . /usr/src/app/"${NAME_PROJECT:-fastapi}"

