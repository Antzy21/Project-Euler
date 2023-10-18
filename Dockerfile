FROM python:latest

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir Flask

WORKDIR /usr/app/src

COPY . .

ENTRYPOINT [ "python" ]
CMD [ "flask_api.py" ]

EXPOSE 5000