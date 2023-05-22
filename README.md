### setup
```sh
$ git clone git@github.com:nonamenme/docker-fastapi-postgres.git
$ cd docker-fastapi-postgres
$ cp .env.example .env
```

### command
・Image build
```sh
$ docker-compose build
```

・Container start up
```sh
$ docker-compose up -d
```

・Container stop
```sh
$ docker-compose stop
```

・Container remove
```sh
$ docker-compose down
```

### APIURL
http://localhost:8000
### SwaggerUI
http://localhost:8000/docs

### migration execution
```sh
$ docker-compose exec -T fastapi alembic upgrade head
```

### create migration file
```sh
$ docker-compose exec -T fastapi alembic revision --autogenerate -m "add columns"
```
