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
// int getDelayTime(){
//   String blinkTimerString;
//   int blinkTimeInt = 0;
//   delay(2000);
//   blinkTimerString = Serial.readString();
//   blinkTimeInt = blinkTimerString.toInt();
//   return blinkTimeInt;
// }

void getTemp_Hum(char in){
  if(in == 't'){
    sensors_event_t event;
    dht.temperature().getEvent(&event);
    Serial.println(event.temperature);
  }
  else{
    sensors_event_t event;
    dht.humidity().getEvent(&event);
    Serial.println(event.relative_humidity);

  }

}

void getTempHum(){
    sensors_event_t event;
    dht.temperature().getEvent(&event);
    Serial.print(event.temperature);
    Serial.print(' ');
    
    dht.humidity().getEvent(&event);
    Serial.println(event.relative_humidity);
  }




void loop() {
  // put your main code here, to run repeatedly:
  int delayTime = 100;
  if(Serial.available()>0){
    userInput = Serial.read();
    if(userInput == 't'){
      digitalWrite(13, 1);
      
      getTemp_Hum('t');
    }
    if(userInput == 'h'){
      digitalWrite(13, 0);
      
      getTemp_Hum('h');

    }
    if(userInput == 'b'){
      digitalWrite(13, 1);
      delay(delayTime);
      digitalWrite(13, 0);
      getTempHum();
      delay(delayTime);
    } 
      
    }

  }


