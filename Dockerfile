FROM acidrain/python-poetry:3.12

ENV https_proxy http://192.168.9.233:10810
ENV http_proxy http://192.168.9.233:10810
ENV all_proxy http://192.168.9.233:10810
ENV no_proxy 10.0.0.0/8,192.168.0.0/16,192.168.9.233,172.0.0.0/8
ENV TZ Asia/Shanghai
# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry install --no-root --no-interaction --no-ansi --only=main

# Creating folders, and files for a project:
COPY ./src /code

ENTRYPOINT [ "poetry","run", "python", "app.py" ]

