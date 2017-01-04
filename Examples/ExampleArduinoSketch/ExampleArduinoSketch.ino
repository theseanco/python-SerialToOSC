void setup() {
  Serial.begin(115200);
}


void loop() {
  Serial.print("msg= ");
  Serial.print(analogRead(A1));
  Serial.print(" ");
  Serial.println(analogRead(A0));
  delay(10);        // delay in between reads for stability
}
