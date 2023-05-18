# library
```
docker build -t library .
```
```
docker run -d -t -i -e host=192.168.56.106 -e port=5432 -e user_name=admin -e password=admin -e db_name=pg --name
mylibrary -p 8000:8000 library
```
```
pip freeze > requirements.txt
```
```
# venv — Создание виртуальных сред

python -m venv C:\Users\Alinka\Documents\projects\FastAPI\docker_compose\venv

venv\Scripts\Activate.ps1
```