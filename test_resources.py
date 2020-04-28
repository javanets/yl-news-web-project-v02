from requests import get, post, delete

print(get('http://localhost:8080/api/v2/news').json())

print(get('http://localhost:8080/api/v2/news/1').json())

print(get('http://localhost:8080/api/v2/news/999').json())

print(get('http://localhost:8080/api/v2/news/q'))
