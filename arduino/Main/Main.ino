// this is the primary code to run that accepts input from the Rasperry Pi server serial
// the code constantly waits for an input so that it can be proccessed 
// integer codes as follow, must be converted to bytes by python
#define FORW 2 // can't use FORWARD as its a command in the adafruit
#define BACK 3 // motor library
#define COAST 1

//these can be used at the same time as a the previous ones
#define RIGHT 4
#define LEFT 5
#define STRAIGHT 0

#define STEER 1 //these are subject to change
#define DRIVE 3 //they define the motor number on the motor shield

#define DRIVEPOWER 255
#define STEERPOWER 128

#include <AFMotor.h>

AF_DCMotor drive(DRIVE); 
AF_DCMotor steer(STEER);

unsigned int steerState = STRAIGHT; //states will hold unless otherwise told
unsigned int driveState = COAST;
unsigned int recv;
unsigned int d;
unsigned int s;
unsigned int n;

void setup() {
    Serial.begin(9600);
    drive.setSpeed(DRIVEPOWER);
    steer.setSpeed(STEERPOWER);
    Serial.write("Initialized.");
}

void loop() {
    if(Serial.available()){ //read the serial
        recv = Serial.read() - '0';
        if (recv>=RIGHT || recv==STRAIGHT ) {
            s = recv;
        } else if (recv>STRAIGHT && recv<RIGHT) {
            d = recv;
        } else {
            n = recv;
        }
    }
     
    if (s==STRAIGHT){ //interpret the numbers
        steer.run(RELEASE);
    } else if (d==COAST) {
        drive.run(RELEASE);
    } else if (d==BACK) {
        drive.run(BACKWARD);
    } else if (d==FORW) {
        steer.run(FORWARD);
    } else if (s==LEFT) {
        steer.run(BACKWARD);
    } else if (s==RIGHT) {
        steer.run(FORWARD);
    } 
}
// Tested: Yay it works!
// may port to a single L293D