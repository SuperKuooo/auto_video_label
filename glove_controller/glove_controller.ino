#define GREEN_LIGHT 7
#define RED_LIGHT 6
#define START_BUTTON 5
#define GRAB_BUTTON 4

unsigned long offset = 0;
unsigned long delta = 0;
short state = 0;

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
  char string[64];
  switch (state) {
    case 0:
      if (start_state) {
        state = 1;
        digitalWrite(GREEN_LIGHT, HIGH);
        digitalWrite(RED_LIGHT, LOW);
      }
      break;
    case 1:
      if (!start_state) {
        state = 2;
        digitalWrite(GREEN_LIGHT, LOW);
        digitalWrite(RED_LIGHT, HIGH);
        sprintf(string, "Start Time: %ul", millis());
        Serial.println(string);
      }
      break;
    case 2:
      if (start_state) {
        state = 3;
        digitalWrite(GREEN_LIGHT, HIGH);
        digitalWrite(RED_LIGHT, HIGH);
        Serial.println("Done Collecting");
      } else if (grab_state) {
        state = 4;
        sprintf(string, "Grab Time: %ul", millis());
        Serial.println(string);
      }
      break;
    case 3:
      if (!start_state){
        state = 0;
        digitalWrite(GREEN_LIGHT, LOW);
        digitalWrite(RED_LIGHT, LOW);
      }
      break;
    case 4:
      if (!grab_state){
        state = 2;
        sprintf(string, "Release Time: %ul", millis());
        Serial.println(string);
      }
      break;
  }
}
