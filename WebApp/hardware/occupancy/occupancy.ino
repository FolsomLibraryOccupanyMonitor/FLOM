#include <stdlib.h>
#include <unistd.h>

#include <hive_map.h>

#define PIR = 2; //connect PIR sensor to pin 2 of arduino
#define LED = 13; //connect LED for testing

int PIR_STATE = LOW;
int val = 0;

typedef struct Occupancy_Space { //creating an occupancy space
    HiveMapSpaceId space;
    bool isOccupied;
} Occupancy_Space;

HiveMapNode(Occupancy_Space) node; //room defined by occupancy space

void setup(){
    pinMode(LED, OUTPUT);
    pinMode(PIR, INPUT);
    Serial.begin(9600);
}

void loop(){
    node.loc = 10; //room number
    node.goal_loc = 1; //floor number
    node.state_received = NULL;
    val = digitalRead(PIR);
    if (val == HIGH) {            // check if the input is HIGH
        digitalWrite(LED, HIGH);  // turn LED ON
        if (PIR_STATE == LOW) {
            Serial.println("Motion detected!");
            pirState = HIGH;
            node.isOccupied = true;
        }
    } 
    else {
        digitalWrite(ledPin, LOW); // turn LED OFF
        if (pirState == HIGH){
            Serial.println("Motion ended!");
            pirState = LOW;
            node.isOccupied = false;
        }
    }
}





