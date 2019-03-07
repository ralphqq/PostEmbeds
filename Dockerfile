FROM python:3.6-alpine

RUN adduser -D pembeds

WORKDIR /home/pembeds

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY pembeds.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP pembeds.py

RUN chown -R pembeds:pembeds ./
USER pembeds

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]