import static spark.Spark.*;

import java.net.InetAddress;
import java.net.UnknownHostException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class WebService {
    public static void main(String[] args) {
        // Устанавливаем порт
        port(3256);

        // Определяем маршрут для корневого URL
        get("/", (request, response) -> {
            response.type("application/json");

            // Получаем IP-адрес
            String ipAddress = getIpAddress();

            // Получаем текущее время
            String currentTime = getCurrentTime();

            // Формируем JSON ответ
            return "{\"ip\":\"" + ipAddress + "\", \"time\":\"" + currentTime + "\"}";
        });
    }

    // Метод для получения IP-адреса
    private static String getIpAddress() {
        try {
            InetAddress ip = InetAddress.getLocalHost();
            return ip.getHostAddress();
        } catch (UnknownHostException e) {
            return "Unknown";
        }
    }

    // Метод для получения текущего времени
    private static String getCurrentTime() {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        return now.format(formatter);
    }
}
