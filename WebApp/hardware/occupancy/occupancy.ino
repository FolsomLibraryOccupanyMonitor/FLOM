#include "hive_map.h"
#include "hive_map.c"

#define PIR 2 //connect PIR sensor to pin 2 of arduino
#define LED 13 //connect LED for testing

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
    node.loc = 10; //room number
    node.goal_loc = 1; //floor number
    node.state_received = NULL;
    Serial.begin(9600);
}

void loop(){
    val = digitalRead(PIR);
    if (val == HIGH) {            // check if the input is HIGH
        digitalWrite(LED, HIGH);  // turn LED ON
        if (PIR_STATE == LOW) {
            Serial.println("Motion detected!");
            PIR_STATE = HIGH;
            node.state.isOccupied = true;
            update_node(&node, sizeof(node)); //update node
        }
    } 
    else {
        digitalWrite(LED, LOW); // turn LED OFF
        if (PIR_STATE == HIGH){
            Serial.println("Motion ended!");
            PIR_STATE = LOW;
            node.state.isOccupied = false;
            update_node(&node, sizeof(node));
        }
    }
    // while(1) {
    //     delay(1000);
    //     cycle_node(&node, sizeof(node));
    // }
}





