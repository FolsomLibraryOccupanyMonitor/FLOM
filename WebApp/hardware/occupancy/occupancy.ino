#define PIR_PIN 2 //connect pir sensor to pin 2 of Arduino

void setup_pins(){
    pinMode(PIR_PIN, INPUT);
}

void setup(){
    Serial.begin(9600); //begin serial monitor
}

void loop(){
    int val = digitalRead(PIR_PIN);
    Serial.println(val);
    if (val == 1) {
        Serial.println("Motion detected");
    }
    else {
        Serial.println("No motion");
    }


}