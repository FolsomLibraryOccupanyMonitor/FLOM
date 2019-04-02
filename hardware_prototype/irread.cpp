// FLOM get IR values

#include <iostream>
#include <unistd.h>				//Needed for I2C port
#include <fcntl.h>				//Needed for I2C port
#include <sys/ioctl.h>			//Needed for I2C port
#include <linux/i2c-dev.h>		//Needed for I2C port
include "MLX90640_I2C_Driver.cpp"
include "MLX90640_API.cpp"
include "MLX90640_SWI2C_Driver.cpp"
#include "MLX90640_API.h"
#include "MLX90640_I2C_Driver.h"

using namespace std;

uint16_t grid [24];
uint16_t xvals [36];
int freq = 1000;
int stopread = 0;

int main(){
	// initialise grid for processing
	//for(unsigned int x=0; x<(sizeof(grid)-1); x++){
	//	grid[x] = xvals;
	//}
	MLX90640_I2CInit();
	while(stopread > -1){
		stopread = MLX90640_I2CRead(0x33, 0x00, 0x00, grid);
	}
	//readdata();
	//visualise(grid);
}

// function to output visualisation of the sensor array
void visualise(int map[]){
	
}

int occupied(int map[], int lastmap[], int lastocc){
	// process the image and determine how many hotspots there are
	
	// Take last value of how many people are in the room
	// If there are more hotspots, check if it could be a person
	// Do this by seeing if it's close to another hotspot and if a hotspot
	// recently entered the map
	
	// Return the value of how many people are occupying the room
}

void readdata(){
	// Code to read data from the sensor using I2C

	// Put output data into the grid variable
	
}
