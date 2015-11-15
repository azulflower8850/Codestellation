//#include <SoftwareSerial.h>
#include <Adafruit_GFX.h>
#include <Adafruit_NeoPixel.h>
#include <Adafruit_NeoMatrix.h>

#define PIN 6

//SoftwareSerial bleShield(8, 9);

double feels = .1;

Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(5, 8,1,1, PIN,
  NEO_MATRIX_TOP     + NEO_MATRIX_RIGHT +
  NEO_MATRIX_COLUMNS + NEO_MATRIX_PROGRESSIVE,
  NEO_GRB           + NEO_KHZ800);

void setup()
{
// bleShield.begin(9600);
 matrix.begin();
 matrix.setBrightness(10);
}

void loop()
{
 if (feels <= .25) {
  matrix.fillScreen(matrix.Color(255,floor(255*(feels)),floor(255*(feels)))); // Red
  }
else if (feels >.25 && feels <=.50){
  matrix.fillScreen(matrix.Color(255,floor(255*(feels*2)),floor(255*feels)));// Yellow to orange
  }
  else if (feels >.5 && feels <=.70){
  matrix.fillScreen(matrix.Color(floor(255*(feels/5)),floor(255*(feels*.5)),floor(255*feels*1.4)));// Yellow to orange
  }

if (feels >.7 && feels <=.75){
  matrix.fillScreen(matrix.Color(floor(255*(feels*.25)),floor(255*(feels*1.3)),floor(255*(feels*1.3))));// Blue
  }
if(feels >.75){
    matrix.fillScreen(matrix.Color(floor(255*(1-feels)),255,floor(255*(1-feels))));// Green

}

matrix.show();
}

