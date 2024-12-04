## Run the api docker

```bash
cd code/api/
docker build -t flask-app .
docker run -d -p 5005:5005 flask-app
```


## Run the postgres docker

```bash
docker run --name postgres-container -e POSTGRES_PASSWORD=123456 -v <INSERT_PATH>:/var/lib/postgresql/data -p 5432:5432 -d postgres
```

## Run the frontend

```bash
npm run dev
```
