// this is the primary code to run that accepts input from the Rasperry Pi server serial
// the code constantly waits for an input so that it can be proccessed 
//  codes as follow, must be converted to bytes by python
#define FORWARD 3
#define BACK 2
#define COAST 1

//these can be used at the same time as a the previous ones
#define RIGHT 1
#define LEFT -1
#define STRAIGHT 0

#define STEER 0 //these are subject to change
#define DRIVE 1

#include <AFMotor.h>

void setup() {
    Serial.begin(9600);
    
}

void loop() {

}
