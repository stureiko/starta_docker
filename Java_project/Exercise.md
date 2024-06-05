Создать volumedocker volume create database
Создайте и запустите контейнер PostgreSQL с примонтированным volume в фоновом режиме с автоматическим удалением после остановкиdocker run --rm --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5455:5432 -v database:/var/lib/postgresql/data postgres
Подключиться к PostgreSQL и создать новую БДdocker exec -it my-postgres psql -U postgresCREATE DATABASE my_new_database;
Остановить контейнер и проверить что он удаленdocker stop my_postgres 
Запустите новый контейнер PostgreSQL с примонтированным volume и проверьте что БД подключиласьdocker run --rm --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5455:5432 -v database:/var/lib/postgresql/data postgresdocker exec -it my-postgres psql -U postgresSELECT datname FROM pg_database;
