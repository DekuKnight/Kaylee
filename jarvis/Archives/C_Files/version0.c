// Project Jarvis
// Version 0.5
// Author:	 Ryan Wright
// Last Updated: 2 April 2013
// Project Description:
//
//	Version 0.5
//	  Converted code from Python to C. Because I understand C.
//
//	Version 0.0
//	  Turns a light on and off. Super accomplishment right?

#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>

int main (void)
{
  int pin = 7;
  int i;
  printf("Raspberry Pi wiringPi blink test\n");

  if(wiringPiSetup() == -1)
  {
    exit(1);
  }

  pinMode(pin, OUTPUT);

  //Infinite Loop
  for(i=0;i<=50;i++)
  {
    printf("%d LED On\n", i);
    digitalWrite(pin, 1);
    sleep(1);
    printf("%d LED Off\n", i);
    digitalWrite(pin, 0);
    sleep(1);
  }

  return 0;
}
