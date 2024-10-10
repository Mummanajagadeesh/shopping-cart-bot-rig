#define A1 D2
#define A2 D3
#define EN1 D4

#define A3 D5
#define A4 D6
#define EN2 D7

void setup(){
  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);
  pinMode(A3, OUTPUT);
  pinMode(A4, OUTPUT);
  pinMode(EN1, OUTPUT);
  pinMode(EN2, OUTPUT);
}

void loop(){

  digitalWrite(A1, LOW);
  digitalWrite(A2, LOW);
  digitalWrite(A3, LOW);
  digitalWrite(A4, LOW);
  delay(2000);

  digitalWrite(A1, HIGH;
  digitalWrite(A2, LOW);
  digitalWrite(A3, HIGH;
  digitalWrite(A4, LOW);
  delay(10000);

  digitalWrite(A1, LOW);
  digitalWrite(A2, LOW);
  digitalWrite(A3, LOW);
  digitalWrite(A4, LOW);
  delay(2000);

  digitalWrite(A1, LOW);
  digitalWrite(A2, HIGH);
  digitalWrite(A3, LOW);
  digitalWrite(A4, HIGH);
  delay(10000);

}