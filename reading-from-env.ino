#include <DHT.h>
#define DHTPIN D1
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

unsigned long previousMillis = 0;
const unsigned long intervalMinutes = 2; // <-- CHANGE THIS (in minutes)
const unsigned long intervalMillis = intervalMinutes * 60 * 1000;

void setup() {
  Serial.begin(115200);
  delay(2000);
  Serial.println("timestamp,humidity,temperature"); // CSV Header
  dht.begin();
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= intervalMillis) {
    previousMillis = currentMillis;

    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();

    if (isnan(humidity) || isnan(temperature)) {
      Serial.println("Failed to read from DHT sensor!");
      return;
    }

    unsigned long timestamp = millis() / 1000; // seconds since start

    // Output in CSV format
    Serial.print(timestamp);
    Serial.print(",");
    Serial.print(humidity);
    Serial.print(",");
    Serial.println(temperature);
  }
}
