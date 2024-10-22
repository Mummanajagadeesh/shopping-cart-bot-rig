#include <ESP8266WiFi.h>
#include <ESPAsyncTCP.h>
#include <ESPAsyncWebServer.h>

const char* ssid = "Redmi Note 12 Pro 5G";
const char* password = "football"; 

const int motorFL1 = D1;
const int motorFL2 = D2;
const int motorFR1 = D3;
const int motorFR2 = D4;
const int motorBL1 = D5;
const int motorBL2 = D6;
const int motorBR1 = D7;
const int motorBR2 = D8;

AsyncWebServer server(80);

void setup() {
    Serial.begin(115200);
    pinMode(motorFL1, OUTPUT);
    pinMode(motorFL2, OUTPUT);
    pinMode(motorFR1, OUTPUT);
    pinMode(motorFR2, OUTPUT);
    pinMode(motorBL1, OUTPUT);
    pinMode(motorBL2, OUTPUT);
    pinMode(motorBR1, OUTPUT);
    pinMode(motorBR2, OUTPUT);

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");

    server.on("/move", HTTP_POST, [](AsyncWebServerRequest *request){
        String direction;
        if (request->hasParam("direction", true)) {
            direction = request->getParam("direction", true)->value();
        }

        if (direction == "forward") {
            moveForward();
        } else if (direction == "left") {
            moveLeft();
        } else if (direction == "right") {
            moveRight();
        } else if (direction == "stop") {
            stopCart();
        }

        request->send(200, "text/plain", "Move command received");
    });

    server.begin();
}

void moveForward() {
    digitalWrite(motorFL1, HIGH); digitalWrite(motorFL2, LOW);
    digitalWrite(motorFR1, HIGH); digitalWrite(motorFR2, LOW);
    digitalWrite(motorBL1, HIGH); digitalWrite(motorBL2, LOW);
    digitalWrite(motorBR1, HIGH); digitalWrite(motorBR2, LOW);
}

void moveLeft() {
    digitalWrite(motorFL1, LOW); digitalWrite(motorFL2, HIGH);
    digitalWrite(motorFR1, HIGH); digitalWrite(motorFR2, LOW);
    digitalWrite(motorBL1, HIGH); digitalWrite(motorBL2, LOW);
    digitalWrite(motorBR1, LOW); digitalWrite(motorBR2, HIGH);
}

void moveRight() {
    digitalWrite(motorFL1, HIGH); digitalWrite(motorFL2, LOW);
    digitalWrite(motorFR1, LOW); digitalWrite(motorFR2, HIGH);
    digitalWrite(motorBL1, LOW); digitalWrite(motorBL2, HIGH);
    digitalWrite(motorBR1, HIGH); digitalWrite(motorBR2, LOW);
}

void stopCart() {
    digitalWrite(motorFL1, LOW);
    digitalWrite(motorFL2, LOW);
    digitalWrite(motorFR1, LOW);
    digitalWrite(motorFR2, LOW);
    digitalWrite(motorBL1, LOW);
    digitalWrite(motorBL2, LOW);
    digitalWrite(motorBR1, LOW);
    digitalWrite(motorBR2, LOW);
}

void loop() {}
