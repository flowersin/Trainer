/*
  Treat Dispenser Code, allows to send an amount of portions (int, 1-9) via serial

  Wiring:
    Relay:
      the control pins are hooked up to Ground, 5v DC and relayPin defined below.
      The contactor pins are hooked up to connect/disconnect the drive motor to 5v 1A dc from the original power supply
    Switch:
      Rewired the original switch to be connected to switchPin and ground.

  And that's pretty much it.
  
  Written by Ellie Schaefer, 2025-12-03

*/


int relayPin = 11; // Define pin that relay signal uses
int switchPin = 12; // Define input pin for the switch

int treatSize = 0; // Initialize the treatsize, or amount of portions to dispense.

void setup() {
  // put your setup code here, to run once:
  pinMode(switchPin, INPUT_PULLUP); // Setup Switch
  pinMode(relayPin, OUTPUT); // Setup Relay Signal (One/High is defualt state)

  digitalWrite(relayPin, LOW); // Set relay to low, we don't want it running.
  
  Serial.begin(9600); // Initialize the serial connection
    while (!Serial) {
    ; // Empty loop, wait for serial port to connect. Needed for native USB port only
  }
}

void loop() {
  while(Serial.available() == 0) {
  } // Wait for something to be sent over serial

  treatSize = Serial.parseInt(); // Parse the amount of treats requested

  Serial.print(treatSize); // Print the amount of treats requested, this is to ensure signal was recieved as well as for debugging
  
  while(treatSize > 0) {  // While we still have treats to dispense...
    digitalWrite(relayPin, HIGH);  // Turn on the relay/motor
    while (digitalRead(switchPin) == HIGH) { // Wait for the pin to go low...
      delay(10);
    }
    while(digitalRead(switchPin) == LOW) { // Wait for the pin to go high again.  Once the pin has cycled states we know it's dispensed a portion
      delay(10);
    }
    treatSize--; // Decrememnt treat size
  }
  digitalWrite(relayPin, LOW); // Once we've dispnsed the requested amount of treats, turn the motor off
}
