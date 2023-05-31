FROM python:3.10

ADD VOID.py .

RUN pip install pandas openpyxl 

CMD ["python3", "./main.py"]