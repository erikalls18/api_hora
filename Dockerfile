FROM python:3.8
RUN pip install flask
RUN mkdir /app
ADD run.py /app/run.py
CMD python3 /app/run.py
