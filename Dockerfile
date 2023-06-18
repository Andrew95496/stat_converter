FROM python:3.10

ADD void/void.py .

RUN pip install pandas openpyxl configparser

CMD ["python3", "./void.py"]