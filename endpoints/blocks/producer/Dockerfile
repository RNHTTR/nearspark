FROM python:3.9

ADD producer.py /

RUN pip install kafka-python
RUN pip install requests

# CMD [ "python", "./producer.py" ]