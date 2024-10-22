#include <ESP8266WiFi.h>

const char* ssid = "Redmi Note 12 Pro 5G";  // Your mobile hotspot SSID
const char* password = "football";  // Your mobile hotspot password

void setup() {
    Serial.begin(9600);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("Connected to WiFi");
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());  // Prints the NodeMCU's IP address
    Serial.print("Gateway IP: ");
    Serial.println(WiFi.gatewayIP());  // Prints the gateway IP address
}

void loop() {
    // Nothing to do here
}
