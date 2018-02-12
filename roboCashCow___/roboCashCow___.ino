// This example drives each motor on the Romi forward, then
// backward.  The yellow user LED is on when a motor should be
// running forward and off when a motor should be running
// backward.

#include <Romi32U4.h>
const char fugue[] PROGMEM =
  "! O5 L16 agafaea dac+adaea fa<aa<bac#a dac#adaea f"
  "O6 dcd<b-d<ad<g d<f+d<gd<ad<b- d<dd<ed<f+d<g d<f+d<gd<ad"
  "L8 MS <b-d<b-d MLe-<ge-<g MSc<ac<a ML d<fd<f O5 MS b-gb-g"
  "ML >c#e>c#e MS afaf ML gc#gc# MS fdfd ML e<b-e<b-"
  "O6 L16ragafaea dac#adaea fa<aa<bac#a dac#adaea faeadaca"
  "<b-acadg<b-g egdgcg<b-g <ag<b-gcf<af dfcf<b-f<af"
  "<gf<af<b-e<ge c#e<b-e<ae<ge <fe<ge<ad<fd"
  "O5 e>ee>ef>df>d b->c#b->c#a>df>d e>ee>ef>df>d"
  "e>d>c#>db>d>c#b >c#agaegfe f O6 dc#dfdc#<b c#4";
  
Romi32U4Motors motors;
Romi32U4ButtonA buttonA;
Romi32U4Buzzer buzzer;

int incomingByte = 0;   // for incoming serial data
char cmd  = 'n';
void setup()
{
  Serial.begin(9600); 
}

void loop()
{
  if (Serial.available() > 0) {
        // read the incoming byte:
        incomingByte = Serial.read();

        // say what you got:
        Serial.print("I received: ");
        cmd = char(incomingByte);
        Serial.println(cmd);}
  else cmd = 'n';
  switch(cmd)
  {
  case 'r' : //turn 90 right
    ledYellow(1);
    motors.setLeftSpeed(100);
    motors.setRightSpeed(-100);
    delay(500);
    ledYellow(0);
    motors.setLeftSpeed(0);
    motors.setRightSpeed(0);
    break;
  case 'l':
    ledYellow(1);//turn 90 left
    motors.setLeftSpeed(-100);
    motors.setRightSpeed(100);
    delay(500);
    ledYellow(0);
    motors.setLeftSpeed(0);
    motors.setRightSpeed(0);
    break;
  case 'f': ;//move forward a bit 
    motors.setLeftSpeed(50);
    motors.setRightSpeed(50);
    delay(500);
    motors.setLeftSpeed(0);
    motors.setRightSpeed(0);
    break;
  case 'm': //plays music for 3 seconds
    buzzer.playFromProgramSpace(fugue);
    delay(3000);
    buzzer.stopPlaying();
    break;
  case 's': //stop music
    buzzer.stopPlaying();
    break;
  }

    
}

  

