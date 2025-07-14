import time
import adafruit_ahtx0
import board
import adafruit_ssd1306
from adafruit_display_text import label
import terminalio
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

now = datetime.now()

# 初始化 I2C 與 OLED 螢幕
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)
sensor = adafruit_ahtx0.AHTx0(i2c)

print("準備開始讀取 AHT20 感測器數據...")
time.sleep(2) # 等待 2 秒讓感測器穩定


# 清空螢幕
oled.fill(0)
oled.show()

font_date = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)


# 2. 建立一個無限迴圈
try:
    while True:

        temp = sensor.temperature
        humidity = sensor.relative_humidity

        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

        try:
            font_temp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
            font_humi = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
        except IOError:
            font_temp = ImageFont.load_default()
            font_humi = ImageFont.load_default()
        
        # --- 準備要顯示的文字 ---
        temp_text = f"{temp:.1f} C"
        humi_text = f"{humidity:.1f} %"
        date_text = now.strftime("%Y-%m-%d")


        # --- 計算文字位置使其置中 ---
        temp_text_width = draw.textlength(temp_text, font=font_temp)
        humi_text_width = draw.textlength(humi_text, font=font_humi)
        date_text_width = draw.textlength(date_text, font=font_date) # 假設日期用 font_date


        temp_x = (oled.width - temp_text_width) // 2
        humi_x = (oled.width - humi_text_width) // 2
        date_x = (oled.width - date_text_width) // 2
        

        # --- 在畫布上寫字 ---
        draw.text((temp_x, 2), temp_text, font=font_temp, fill=255)      # 溫度顯示在上面
        draw.text((humi_x, 30), humi_text, font=font_humi, fill=255)   # 濕度顯示在下面
        draw.text((date_x, 50), date_text, font=font_date, fill=255) # 把日期放在最下面



# 6. 最後，將我們完成的整張畫布，「貼」到 OLED 螢幕上
        oled.image(image)
        oled.show()

        print(f"溫度：'{temp:.1f} C', 濕度:'{humidity:.1f} %'")

        time.sleep(2)


except KeyboardInterrupt:
    print("\n程式結束")
    # 結束前再次清空螢幕

oled.fill(0)
oled.show()