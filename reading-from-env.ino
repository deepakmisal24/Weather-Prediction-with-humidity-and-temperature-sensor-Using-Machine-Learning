#include<DHT.h>
#define DHTPIN D1 
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
void setup() {
  Serial.begin(115200);
  delay(2000); 
  Serial.println("DHT11 Sensor Test");
  dht.begin();
}
void loop() {
  delay(2000); 
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
  return;
}

Serial.print(humidity,2);
Serial.print(", ");
Serial.println(temperature,2);
}