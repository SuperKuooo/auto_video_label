#define GREEN_LIGHT 7
#define RED_LIGHT 6
#define START_BUTTON 5
#define GRAB_BUTTON 4

unsigned long offset = 0;
unsigned long delta = 0;
short state = 0;
char string[32];

void setup() {
  Serial.begin(9600);
  pinMode(GREEN_LIGHT, OUTPUT);
  pinMode(RED_LIGHT, OUTPUT);
  pinMode(START_BUTTON, INPUT);
  pinMode(GRAB_BUTTON, INPUT);
}

void loop() {
  bool start_state = digitalRead(START_BUTTON);
  bool grab_state = digitalRead(GRAB_BUTTON);
  switch (state) {
    case 0:
      if (start_state) {
        digitalWrite(GREEN_LIGHT, HIGH);
        state++;
      }
      break;
    case 1:
      if (!start_state) {
        digitalWrite(GREEN_LIGHT, LOW);
        offset = millis();
        state++;
      }
      break;
    case 2:
      digitalWrite(RED_LIGHT, HIGH);
      if (start_state) {
        digitalWrite(GREEN_LIGHT, LOW);
        digitalWrite(RED_LIGHT, LOW);
        state++;
        Serial.println("Done Collecting");
        delay(1000);
      } else if (grab_state) {
        delta = millis() - offset;
        sprintf(string, "Time: %ul", delta);
        Serial.println(string);
      }
      break;
    case 3:
      if (start_state) {
        state = 0;
      }
      delay(1000);
      break;
  }
}
