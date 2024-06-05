# Используем официальный образ OpenJDK в качестве базового
FROM openjdk:11-jre-slim

# Устанавливаем рабочий каталог в контейнере
WORKDIR /app

# Копируем собранный jar-файл в контейнер
COPY target/spark-web-service-1.0-SNAPSHOT-jar-with-dependencies.jar app.jar

# Указываем команду для запуска приложения
ENTRYPOINT ["java", "-jar", "app.jar"]

# Указываем порт, который будет прослушивать приложение
EXPOSE 3256
