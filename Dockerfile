FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /test
WORKDIR /test
COPY . /test/
RUN pip install -r requiremets.txt
