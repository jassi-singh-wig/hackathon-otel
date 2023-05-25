package sparkexample;

import static spark.Spark.*;
import java.util.Map;

public class Hello {

    public static void main(String[] args) {
        get("/", (req, res) -> {
            String x = "test";
            for (int i = 0; i <= 1000000; i++) {
                for (int j = 0; j <= 10; j++) {
             
                    StringBuilder response = new StringBuilder();
                    Map<String, String> envVariables = System.getenv();
                    for (Map.Entry<String, String> entry : envVariables.entrySet()) {
                        response.append(entry.getKey())
                                .append(": ")
                                .append(entry.getValue())
                                .append("\n");
                    }
                    x = response.toString();
                }
            }
            return x;
        });
    }

}