FROM python:3.9


WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export --without-hashes -f requirements.txt -o requirements.txt


FROM python:3.9


WORKDIR /code

COPY --from=0 /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:80", "blood_chain.wsgi"]
