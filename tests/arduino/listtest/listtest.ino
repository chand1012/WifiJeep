#define STEER 13
#define DRIVE 12

unsigned int s;
unsigned int d;
unsigned int n;

void setup()
{
    pinMode(STEER, OUTPUT);
    pinMode(DRIVE, OUTPUT);
    Serial.begin(9600);
    n = 0;
    s = 0;
    d = 1;
}

void loop()
{
    if(Serial.available()){
        n = Serial.read() - '0';
        if (n>=4 || n==0 ) {
            s = n;
        } else {
            d = n;
        }
    }

    if (d!=1) {
        digitalWrite(DRIVE, HIGH);
    } else {
        digitalWrite(DRIVE, LOW);
    }

    if (s!=0) {
        digitalWrite(STEER, HIGH);
    } else {
        digitalWrite(STEER, LOW);
    }
    
}