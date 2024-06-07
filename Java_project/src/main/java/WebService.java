import java.net.InetAddress;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

import static spark.Spark.get;
import static spark.Spark.port;

public class WebService {
    private static final String DB_URL = "jdbc:mysql://mysql:3306/testdb";
    private static final String DB_USER = "root";
    private static final String DB_PASSWORD = "password";

    public static void main(String[] args) {
        // Устанавливаем порт
        port(3256);

        // Определяем маршрут для корневого URL
        get("/", (request, response) -> {
            response.type("application/json");

            String lastRecord = getLastRecordAndUpdate();

            return lastRecord;
        });
    }

    private static String getLastRecordAndUpdate() {
        String result = "";
        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
             Statement stmt = conn.createStatement()) {

            // Получаем последнюю запись
            ResultSet rs = stmt.executeQuery("SELECT * FROM test_table ORDER BY id DESC LIMIT 1");
            if (rs.next()) {
                result = String.format("{\"id\": \"%d\", \"date_time\": \"%s\", \"ip\": \"%s\"}", 
                        rs.getInt("id"), rs.getString("date_time"), rs.getString("ip"));
            }

            // Добавляем новую запись с текущей датой, временем и IP
            String currentTime = getCurrentTime();
            String ipAddress = getIpAddress();
            String insertSQL = "INSERT INTO test_table (date_time, ip) VALUES (?, ?)";
            try (PreparedStatement pstmt = conn.prepareStatement(insertSQL)) {
                pstmt.setString(1, currentTime);
                pstmt.setString(2, ipAddress);
                pstmt.executeUpdate();
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
        return result;
    }

    private static String getIpAddress() {
        try {
            InetAddress ip = InetAddress.getLocalHost();
            return ip.getHostAddress();
        } catch (Exception e) {
            return "Unknown";
        }
    }

    private static String getCurrentTime() {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        return now.format(formatter);
    }
}
