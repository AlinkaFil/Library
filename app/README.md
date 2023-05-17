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
