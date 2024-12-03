#include <ESP8266WiFi.h>

const char* ssid = "Redmi Note 12 Pro 5G";
const char* password = "football";
WiFiServer server(80);

void setup() {
  Serial.begin(115200);

  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);
  pinMode(D5, OUTPUT);
  pinMode(D6, OUTPUT);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  Serial.println(WiFi.localIP()); 

  server.begin();
}

void loop() {
  WiFiClient client = server.available(); 

  if (client) {
    Serial.println("Client connected");

    while (client.connected()) {
      if (client.available()) {
        String line = client.readStringUntil('\n');
        Serial.println("Received data: " + line);

        int r1 = line.substring(0, line.indexOf(',')).toInt();
        line = line.substring(line.indexOf(',') + 1);
        int r2 = line.substring(0, line.indexOf(',')).toInt();
        line = line.substring(line.indexOf(',') + 1);
        int l1 = line.substring(0, line.indexOf(',')).toInt();
        int l2 = line.substring(line.indexOf(',') + 1).toInt();

        Serial.printf("R1: %d, R2: %d, L1: %d, L2: %d\n", r1, r2, l1, l2);

        analogWrite(D1, r1);
        analogWrite(D2, r2);
        analogWrite(D3, l2);
        analogWrite(D4, l1);
        digitalWrite(D5, 1);
        digitalWrite(D6, 1);
        
      }
    }
    client.stop();
    Serial.println("Client disconnected");
  }
}
