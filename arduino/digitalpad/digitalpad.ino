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

const int XP=8,XM=A2,YP=A3,YM=9; //240x400 ID=0x7793
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


void setup() {
  uint16_t ID;
  Serial.begin(9600);
  ID = tft.readID();
  Serial.println(ID, HEX);
  if (ID == 0x0D3D3) ID = 0x9481;
  tft.begin(ID);
  tft.setTextColor(0xFFFF, 0x0000);
  tft.setRotation(1);
  tft.fillScreen(BLACK);
}

void loop() {
  // put your main code here, to run repeatedly:
  if("numpad"=="numpad"){
    Adafruit_GFX_Button btn_0, btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9;
    Adafruit_GFX_Button btn_bloqNum, btn_slash, btn_asterisk, btn_minus, btn_plus, btn_dot, btn_enter;
    // initButton(TFT, x, y, w, h, outline, fill, text_color, label, text_size);
    btn_0.initButton(&tft, 200, 200, 80, 30, WHITE, CYAN, BLACK, "0", 1);
    btn_0.drawButton(true);
    
    while(true){
      digitalpad(btn_0);
    }
  }
}

void digitalpad(Adafruit_GFX_Button btn_0){
  bool down = Touch_getXY();

  btn_0.press(down && btn_0.contains(pixel_x, pixel_y));
  if(btn_0.justPressed()){
    Serial.println("btn_0_down");
  }
  if(btn_0.justReleased()){
    Serial.println("btn_0_UP");
  }
}
