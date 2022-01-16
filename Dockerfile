FROM python:3.10.1-buster
RUN /usr/local/bin/python -m pip install --upgrade pip && python3 -m venv homework
COPY . /case5_homework
WORKDIR /case5_homework
RUN pip install -r requirements.txt
CMD ["python", "run.py"]
