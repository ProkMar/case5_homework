import requests
import logging

service_host = 'localhost'
service_port = 5110
type_request = 'train'

url = f'http://{service_host}:{service_port}/{type_request}'

s = requests.session()
response = s.get(url)

logging.basicConfig(
    filename="/case5_homework/retrain_by_cron.log",
    level=logging.INFO)
logging.info(response.text)
