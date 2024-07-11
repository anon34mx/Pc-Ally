// MCUFRIEND UNO shields have microSD on pins 10, 11, 12, 13
// The official <SD.h> library only works on the hardware SPI pins
// e.g. 11, 12, 13 on a Uno  (or STM32 Nucleo)
//
// copy all your BMP files to the root directory on the microSD with your PC
// (or another directory)
#include <TouchScreen.h>
#define MINPRESSURE 200
#define MAXPRESSURE 1000
#define BLACK   0x0000
#define BLUE    0x001F
#define RED     0xF800
#define GREEN   0x07E0
#define CYAN    0x07FF
#define MAGENTA 0xF81F
#define YELLOW  0xFFE0
#define WHITE   0xFFFF

#include <SPI.h>            // f.k. for Arduino-1.5.2
#include <Adafruit_GFX.h>   // Hardware-specific library
#include <MCUFRIEND_kbv.h>
MCUFRIEND_kbv tft;

#if defined(ESP32)
#define SD_CS     5
#else
#define SD_CS     10
#endif

#include <ArduinoJson.h>

// PARA LA PARTE TACTIL
// ALL Touch panels and wiring is DIFFERENT
// copy-paste results from TouchScreen_Calibr_native.ino
const int XP=8,XM=A2,YP=A3,YM=9; //240x400 ID=0x7793
//const int TS_LEFT=891,TS_RT=132,TS_TOP=57,TS_BOT=930;
const int TS_LEFT=880,TS_RT=132,TS_TOP=57,TS_BOT=930;
TouchScreen ts = TouchScreen(XP, YP, XM, YM, 300);
int pixel_x, pixel_y;     //Touch_getXY() updates global vars

bool Touch_getXY(void)
{
  TSPoint p = ts.getPoint();
  pinMode(YP, OUTPUT);      //restore shared pins
  pinMode(XM, OUTPUT);      //because TFT control pins
  bool pressed = (p.z > MINPRESSURE && p.z < MAXPRESSURE);
  if (pressed) {
    // pixel_x = map(p.x, TS_LEFT, TS_RT, 0, tft.width()); //.kbv makes sense to me
    // pixel_y = map(p.y, TS_TOP, TS_BOT, 0, tft.height());
    pixel_y = map(p.x, TS_LEFT, TS_RT, tft.height(), 0);
    pixel_x = map(p.y, TS_TOP, TS_BOT, 0, tft.width());
  }
  return pressed;
}

//aaron


void setup()
{
  uint16_t ID;
  Serial.begin(9600);
  ID = tft.readID();
  Serial.println(ID, HEX);
  if (ID == 0x0D3D3) ID = 0x9481;
  tft.begin(ID);
  tft.setTextColor(0xFFFF, 0x0000);
  tft.setRotation(1);
  
}
void loop(){
  // String incomingByte=Serial.readString();
    // tft.setCursor(0, 0);
    // tft.println(incomingByte);
    // if(incomingByte=="hola"){
    //   Serial.println("responder saludo");
    // }else{
    //   Serial.println(incomingByte);
    // }
    while (true) {
      mouse();
    }
}


// boolean state = false;
boolean lastState=false;
long lastDebounce=0;
int debounceDelay=100;
bool isPressed=false;
bool lClickState=false;
bool mClickState=false;
bool rClickState=false;
void mouse(){
  double currentTime = millis();
  deltaTime=(currentTime - deltaTime);
  bool down = Touch_getXY();

  if(down != lastState){
    lastDebounce=currentTime;
  }
  middle_click.press(down && middle_click.contains(pixel_x, pixel_y));
  if (middle_click.justPressed()){
    mClickState=true;
  }
  if (middle_click.justReleased()){
    mClickState=false;
  }
  left_click.press(down && left_click.contains(pixel_x, pixel_y));
  if (left_click.justPressed()){
    lClickState=true;
  }
  if (left_click.justReleased()){
    lClickState=false;
  }
  right_click.press(down && right_click.contains(pixel_x, pixel_y));
  if (right_click.justPressed()){
    rClickState=true;
  }
  if (right_click.justReleased()){
    rClickState=false;
  }
  if(currentTime - lastDebounce > debounceDelay){
    if(isPressed!=down){
      isPressed=down;
      if(isPressed){
        if(lClickState==true){
          obj["method"]="mouse_click";
          obj["data"]="L_pressed";
          Serial.println("");
          serializeJson(doc, Serial);
          obj.clear();
        }
        if(rClickState==true){
        }
        if(mClickState==true){
        }
      }else{
        lastState=false;
        isPressed=false;
        // drawMousepad();
      }
    }else{
      //puede ser aqui
    }
  }else{
    // Serial.println("NO");
  }// no presionado
  lastState = down;
  if(mClickState){
    // Serial.println((String) "{\"method\":\"mousepad\",\"data\":{\"scroll_y\":"+(last_mouse_y - pixel_y)*-(deltaTime*speed)+"}}");
    
  }
  if(pixel_x<360 && (last_mouse_x!=pixel_x || last_mouse_y!=pixel_y)){
  }
  last_mouse_x=pixel_x;
  last_mouse_y=pixel_y;
  deltaTime=currentTime;
}