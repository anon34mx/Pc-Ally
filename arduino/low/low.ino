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

// PARA LA PARTE TACTIL
// ALL Touch panels and wiring is DIFFERENT
// copy-paste results from TouchScreen_Calibr_native.ino
const int XP=8,XM=A2,YP=A3,YM=9; //240x400 ID=0x7793
//const int TS_LEFT=891,TS_RT=132,TS_TOP=57,TS_BOT=930;
const int TS_LEFT=880,TS_RT=132,TS_TOP=57,TS_BOT=930;
TouchScreen ts = TouchScreen(XP, YP, XM, YM, 300);
Adafruit_GFX_Button on_btn;
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
    // Serial.print(pixel_x);
    // Serial.print(" - ");
    // Serial.println(pixel_y);
  }
  return pressed;
}

//aaron
bool startMenu;


void setup()
{
  uint16_t ID;
  Serial.begin(9600);
  ID = tft.readID();
  Serial.println(ID, HEX);
  if (ID == 0x0D3D3) ID = 0x9481;
  tft.begin(ID);
  tft.fillScreen(BLUE);
  tft.setTextColor(0xFFFF, 0x0000);
  tft.setRotation(1);
  
  on_btn.initButton(&tft, 16, 224, 30, 30, WHITE, CYAN, BLACK, "ON", 1);
  on_btn.drawButton(true);
  tft.fillRect(30, 211, 370, 29, BLACK);
  startMenu=0;
}
void loop(){
  bool down = Touch_getXY();
  on_btn.press(down && on_btn.contains(pixel_x, pixel_y));
  if (on_btn.justPressed()) {
    startMenu=!startMenu;
    Serial.println(startMenu);
      if(startMenu==false){
        // on_btn.drawButton(true);
        tft.fillRect(0, 0, 80, 210, BLUE);
      }else{
        tft.fillRect(0, 0, 80, 210, BLACK);
      }
  }
  // String incomingByte=Serial.readString();
    // tft.setCursor(0, 0);
    // tft.println(incomingByte);
    // if(incomingByte=="hola"){
    //   Serial.println("responder saludo");
    // }else{
    //   Serial.println(incomingByte);
    // }
    initMouse();
    while (true) {
      mouse();
    }
}

Adafruit_GFX_Button left_click;
Adafruit_GFX_Button right_click;
Adafruit_GFX_Button middle_click;
void initMouse(){
  delay(10);
  tft.fillRect(0, 0, 360, 240, RED);
  tft.fillRect(360, 0, 40, 90, GREEN);
  tft.fillRect(360, 90, 40, 60, YELLOW);
  tft.fillRect(360, 150, 40, 90, BLUE);

  left_click.initButton(&tft, 380, 45, 40, 90, WHITE, CYAN, BLACK, "[L]", 1);
  left_click.drawButton(true);  

  middle_click.initButton(&tft, 380, 120, 40, 60, WHITE, CYAN, BLACK, "[M]", 1);
  middle_click.drawButton(true);

  right_click.initButton(&tft, 380, 194, 40, 90, WHITE, CYAN, BLACK, "[R]", 1);
  right_click.drawButton(true);
}
int last_mouse_x=0;
int last_mouse_y=0;
float deltaTime=0;
float speed=0.05;
int mouse_action=0;
// 0 none
// 1 left click
// 2 right click
// 3 middle click
// 4 scroll up
// 5 scroll down

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
    // Serial.println("R_down");
  }
  if (right_click.justReleased()){
    rClickState=false;
    // Serial.println("R_up");
  }
  if(currentTime - lastDebounce > debounceDelay){
    if(isPressed!=down){
      isPressed=down;
      if(isPressed){
        if(lClickState==true){
          Serial.println((String) "{method:'mousepad',data:{click:'L_pressed'}}");
        }
        if(rClickState==true){
          Serial.println((String) "{method:'mousepad',data:{click:'R_pressed'}}");
        }
        if(mClickState==true){
          Serial.println((String) "{method:'mousepad',data:{click:'M_pressed'}}");
        }
      }else{
        Serial.println((String) "{method:'mousepad',data:{click:'released'}}");
      }
    }
  }else{}// no presionado
  lastState = down;
  if(mClickState){
    Serial.println((String) "{method:'mousepad',data:{scroll:y:"+(last_mouse_y - pixel_y)*-(deltaTime*speed)+"}}");
  }
  if(pixel_x<360 && (last_mouse_x!=pixel_x || last_mouse_y!=pixel_y)){
    Serial.println((String) "{method:'mousepad',data:{x:"+(last_mouse_x - pixel_x)*-(deltaTime*speed)+",y:"+(last_mouse_y - pixel_y)*-(deltaTime*speed)+"}}");
  }
  last_mouse_x=pixel_x;
  last_mouse_y=pixel_y;
  deltaTime=currentTime;
}