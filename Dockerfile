FROM python:3.9.0

WORKDIR /home/

RUN echo 'test1'

RUN git clone https://github.com/IHAGI-c/GIS_class_2.git

WORKDIR /home/GIS_class_2/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=GIS_class2_1.settings.deploy && python manage.py collectstatic --noinput --settings=GIS_class2_1.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=GIS_class2_1.settings.deploy GIS_class2_1.wsgi --bind 0.0.0.0:8000"]