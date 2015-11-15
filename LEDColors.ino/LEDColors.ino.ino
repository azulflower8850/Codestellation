//#include <SoftwareSerial.h>
#include <Adafruit_GFX.h>
#include <Adafruit_NeoPixel.h>
#include <Adafruit_NeoMatrix.h>


#define PIN 6

//SoftwareSerial bleShield(8, 9);

double feels = .7;
double newfeels=0;
const int MaxChars = 3;
char strValue[MaxChars+1];
int index = 0;

Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(5, 8,1,1, PIN,
  NEO_MATRIX_TOP     + NEO_MATRIX_RIGHT +
  NEO_MATRIX_COLUMNS + NEO_MATRIX_PROGRESSIVE,
  NEO_GRB           + NEO_KHZ800);

void setup()
{
Serial.begin(9600);
matrix.begin();
 matrix.setBrightness(10);
}

void serialEvent()
{
  while(Serial.available())
  {
   
    char value = Serial.read();
    if (index<MaxChars)
    {
      strValue[index] = value;
      index++;
    }
  }

  newfeels = atoi(strValue);
  newfeels=newfeels/1000;
  Serial.print("newfeels: ");
  Serial.println(newfeels);
 

}

void loop()
{
    serialEvent();
    index=0;
    

  if(newfeels!=feels)
  {
       if (newfeels <= .25) {
           matrix.fillScreen(matrix.Color(255,floor(255*(newfeels)),floor(255*(newfeels)))); // Red
      }
      else if (newfeels >.25 && newfeels <=.50){
           matrix.fillScreen(matrix.Color(255,floor(255*(newfeels*2)),floor(255*newfeels)));// Yellow to orange
      }
      else if (newfeels >.5 && newfeels <=.70){
            matrix.fillScreen(matrix.Color(floor(255*(newfeels/5)),floor(255*(newfeels*.5)),floor(255*newfeels*1.4)));// Yellow to orange
      }
    
      else if (newfeels >.7 && newfeels <=.75){
            matrix.fillScreen(matrix.Color(floor(255*(newfeels*.25)),floor(255*(newfeels*1.3)),floor(255*(newfeels*1.3))));// Blue
      }
      else if(newfeels >.75){
            matrix.fillScreen(matrix.Color(floor(255*(1-newfeels)),255,floor(255*(1-newfeels))));// Green

      }

    feels=newfeels;
  }
  
matrix.show();
}

