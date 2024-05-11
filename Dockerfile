FROM python:3.11.1
ENV DJANGO_SETTINGS_MODULE=prod_app.settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /prod_project

COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

COPY prod_project/ ./
RUN ls -la

RUN python manage.py collectstatic --noinput

COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh

COPY create_superuser.py ./
ENTRYPOINT ["./entrypoint.sh"]
EXPOSE 8008
CMD ["gunicorn", "prod_project.wsgi:application", "--bind", "0.0.0.0:8008"]
