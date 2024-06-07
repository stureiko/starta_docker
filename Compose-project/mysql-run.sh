docker run --name mysql -e MYSQL_ROOT_PASSWORD=password -d -p 3306:3306 -v mysql-database:/var/lib/mysql mysql:latest
