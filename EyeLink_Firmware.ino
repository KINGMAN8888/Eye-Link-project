#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

const int RELAY_1_PIN = 2; 
const int RELAY_2_PIN = 3; 
const int RELAY_3_PIN = 4; 
const int RELAY_4_PIN = 5; 
const int BUZZER_PIN  = 6; 

LiquidCrystal_I2C lcd(0x27, 16, 2);  

const long BAUD_RATE = 9600;

void setup() {
  Serial.begin(BAUD_RATE);

  pinMode(RELAY_1_PIN, OUTPUT);
  pinMode(RELAY_2_PIN, OUTPUT);
  pinMode(RELAY_3_PIN, OUTPUT);
  pinMode(RELAY_4_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);


  digitalWrite(RELAY_1_PIN, LOW);
  digitalWrite(RELAY_2_PIN, LOW);
  digitalWrite(RELAY_3_PIN, LOW);
  digitalWrite(RELAY_4_PIN, LOW);
  noTone(BUZZER_PIN);


  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Eye-Link Project");
  lcd.setCursor(0, 1);
  lcd.print("System Ready...");
  
  playMelody();
  
  Serial.println("Eye-Link Hardware Ready...");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    lcd.setCursor(0, 1);
    lcd.print("                "); 
    lcd.setCursor(0, 1);

    if (command == "LIGHT_ON") {
      digitalWrite(RELAY_1_PIN, HIGH);
      lcd.print("Light: ON");
      beep(1);
    }
    else if (command == "LIGHT_OFF") {
      digitalWrite(RELAY_1_PIN, LOW);
      lcd.print("Light: OFF");
      beep(1);
    }
    else if (command == "FAN_ON") {
      digitalWrite(RELAY_2_PIN, HIGH);
      lcd.print("Fan: ON");
      beep(1);
    }
    else if (command == "FAN_OFF") {
      digitalWrite(RELAY_2_PIN, LOW);
      lcd.print("Fan: OFF");
      beep(1);
    }
     else if (command == "HEATER_ON") {
      digitalWrite(RELAY_3_PIN, HIGH);
      beep(1);
    }
    else if (command == "HEATER_OFF") {
      digitalWrite(RELAY_3_PIN, LOW);
      beep(1);
    }
    else if (command == "AC_ON") {
      digitalWrite(RELAY_4_PIN, HIGH);
      beep(1);
    }
    else if (command == "AC_OFF") {
      digitalWrite(RELAY_4_PIN, LOW);
      beep(1);
    }

    else if (command.startsWith("MSG:")) {
      String msg = command.substring(4);
      if (msg.length() > 16) msg = msg.substring(0, 16);
      lcd.print(msg);
      beep(1);
    }
  }
}


void beep(int times) {
  for (int i = 0; i < times; i++) {
    tone(BUZZER_PIN, 1000); 
    delay(100);
    noTone(BUZZER_PIN);
    delay(100);
  }
}


void playMelody() {
  tone(BUZZER_PIN, 262, 200);
  delay(200);
  tone(BUZZER_PIN, 330, 200);
  delay(200);
  tone(BUZZER_PIN, 392, 400);
  delay(400);
  noTone(BUZZER_PIN);
}