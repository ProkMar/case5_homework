FROM python:3.10.1-buster
COPY . /case5_homework
WORKDIR /case5_homework
RUN /usr/local/bin/python -m pip install --upgrade pip && \
python3 -m venv homework && pip install -r requirements.txt
ENTRYPOINT ["python3" , "/case5_homework/run.py" ]
