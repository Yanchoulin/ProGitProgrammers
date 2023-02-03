#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN 2 
#define DHTTYPE    DHT11
DHT_Unified dht(DHTPIN, DHTTYPE);
char userInput;
void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  Serial.begin(115200);
  dht.begin();
  
}
int getDelayTime(){
  String blinkTimerString;
  int blinkTimeInt = 0;
  delay(2000);
  blinkTimerString = Serial.readString();
  blinkTimeInt = blinkTimerString.toInt();
  return blinkTimeInt;
}


void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    userInput = Serial.read();
    if(userInput == 'o'){
      digitalWrite(13, 1);
    }
    if(userInput == 'x'){
      digitalWrite(13, 0);
    }
    if(userInput == 'b'){
      int delayTime = getDelayTime();
      for(int i = 0; i < 10; i++){
        digitalWrite(13, 1);
        delay(delayTime);
        digitalWrite(13, 0);
        delay(delayTime);
      } //Blink
      
    }

  }
  //digitalWrite(13, 1);
  //Serial.println("LED ON");
  delay(100);
  sensors_event_t event;
  dht.temperature().getEvent(&event);
  Serial.print(F("Temperature: "));
  Serial.print(event.temperature);
  Serial.println(F("°C"));
  //digitalWrite(13, 0);
  delay(100); 
  dht.humidity().getEvent(&event);
  Serial.print(F("Humidity: "));
  Serial.print(event.relative_humidity);
  Serial.println(F("%"));
  //Serial.println("LED OFF");
  delay(100);  

}