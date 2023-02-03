#include <Arduino.h>

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(13, 1);
  Serial.println("LED ON");
  delay(500);
  digitalWrite(13, 0);
  Serial.println("LED OFF");
  delay(500);  

}