const int ledPin = 13;
int n;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  n = 7;
}

void loop() {
  if(Serial.available()){
    n = Serial.read() - '0';
  }
  if (n==0){
    digitalWrite(ledPin, LOW);
  } else {
    digitalWrite(ledPin, HIGH);
  }

}