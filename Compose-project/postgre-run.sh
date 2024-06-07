docker run --name my_postgres -e POSTGRES_PASSWORD=password -d -p 5432:5432 -v database:/var/lib/postgresql/data postgres
