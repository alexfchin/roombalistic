#include "Servo.h"

Servo myServo;

void setup() {
  myServo.attach(9);


}

void loop() {
  myServo.write(180);
}
