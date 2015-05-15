// Project Jarvis
// Author:	 Ryan Wright
// Last Updated: 2 April 2013
// Project Description:
//
//	Version 1.0
//	  Sends a signal on a button push
//
//	Version 0.5
//	  Converted code from Python to C. Because I understand C.
//
//	Version 0.0
//	  Turns a light on and off. Super accomplishment right?

#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>

#define LIGHTS_ON 	1
#define LIGHTS_OFF	0
#define LIGHTS_ERROR	-1

int lightsOn(int lightStatus);
int lightsOff(int lightStatus);
int lightsChange(int lightStatus);
void lightStatus(int currentStatus);

const int lightPin = 7;
int lightsAre;

int main (int argv, char *argc[])
{
  int i;
  printf("Project Jarvis Version 1\n");

  if(wiringPiSetup() == -1)
  {
    exit(1);
  }

  pinMode(lightPin, OUTPUT);

  lightStatus(LIGHTS_ON);
	
  //Turning lights off
  printf("   LightsAre: %d\n", lightsAre);
  lightStatus(lightsChange(lightsAre));
  sleep(5);

  //Turning lights on
  printf("   LightsAre: %d\n", lightsAre);
  lightStatus(lightsChange(lightsAre));
  sleep(5);

  printf("Process ended\n");

  return 0;
}

// Sends lights on signal and changes status
// INP: lightStatus
// OUT: lightStatus (-1 for error)
int lightsOn(int lightStatus)
{
	//Lights are already on
	if(lightStatus == LIGHTS_ON)
	{
		//Do nothing the lights are already on
		printf("Lights are already on\n");
	}
	//Lights are off
	else if(lightStatus == LIGHTS_OFF)
	{
		//Turn lights on and change lightStatus
		lightStatus = LIGHTS_ON;
		digitalWrite(lightPin, 1);
		sleep(.5);
		digitalWrite(lightPin, 0);
		sleep(.5);
		printf("Lights turned off\n");
	}
	else //something else
	{
		fprintf(stderr, "Something went wrong: LightsOff\n");
		return(LIGHTS_ERROR);
	}

	return lightStatus;
}

// Sends lights on signal and changes status
// INP: lightStatus
// OUT: lightStatus (-1 for error)
int lightsOff(int lightStatus)
{       
        //Lights are already off
        if(lightStatus == LIGHTS_OFF)
        {       
                //Do nothing the lights are already on
                printf("Lights are already off\n");
        }
        //Lights are on
        else if(lightStatus == LIGHTS_ON)
        {       
                //Turn lights off and change lightStatus
                lightStatus = LIGHTS_OFF;
                digitalWrite(lightPin, 1);
                sleep(.5);
                digitalWrite(lightPin, 0);
                sleep(.5);
                printf("Lights turned on\n");
        }
        else //something else
        {       
                fprintf(stderr,"Something went wrong: funct LightsOff\n");
                return(LIGHTS_ERROR);
        }
        
        return lightStatus;
}

// Changes lights
// INP: lightStatus
// OUT: lightStatus (-1 for error)
int lightsChange(int lightStatus)
{
	int currentStatus = lightStatus;
	
	if(lightStatus == LIGHTS_ON)
	{
		currentStatus = lightsOff(lightStatus);
	}
	else if(lightStatus == LIGHTS_OFF)
	{
		currentStatus = lightsOn(lightStatus);
	}
	else //somethings wrong
	{
		fprintf(stderr, "Something went wrong: funct lightChange");
		return LIGHTS_ERROR;
	}

	//Error checking
	if(currentStatus == LIGHTS_ERROR)
	{
		fprintf(stderr, "Something went wrong: funct lightChange");
		return LIGHTS_ERROR;
	}
	
	return currentStatus;
}

//Changes the light Status
void lightStatus(int currentStatus)
{
	lightsAre = currentStatus;
	printf("lightStatus updated: %d\n", lightsAre);
}
