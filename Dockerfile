FROM python:3.10

ADD void.py .

RUN pip install pandas openpyxl configparser

CMD ["python3", "./void.py"]