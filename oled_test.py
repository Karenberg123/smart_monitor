import board
import adafruit_ssd1306
from adafruit_display_text import label
import terminalio
import time
from PIL import Image, ImageDraw, ImageFont


# 初始化 I2C 與 OLED 螢幕
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)

# | 函式 / 屬性                          | 功能說明                                    |
# | -------------------------------- | --------------------------------             |
# | `oled.poweron()`                 | 開啟 OLED 電源                                |
# | `oled.poweroff()`                | 關閉 OLED 電源（節能模式）                      |
# | `oled.contrast(level)`           | 設定對比度，`level` 範圍 0–255                 | 
# | `oled.invert(flag)`              | 反轉顏色（`True`: 白底黑字；`False`: 黑底白字）  |
# | `oled.display()` / `oled.show()` | 同義：刷新顯示緩衝區至螢幕                       |
# | `oled.fill(color)`               | 整螢幕填滿（`0` 或 `1`）                        |
# | `oled.pixel(x, y, color)`        | 設定單一像素                                    |
# | `oled.width`, `oled.height`      | 讀取螢幕寬度、高度                               |

# | 函式                                  | 功能說明                        |
# | ----------------------------------- | ---------------------           |
# | `oled.command(cmd)`                 | 直接傳送單一控制命令（0x00–0xFF）   |
# | `oled.write(data)`                  | 直接寫入原始位元組陣列到顯示緩衝     |
# | `oled.reset_pin.value = True/False` | 手動控制硬體重置腳位               |


# | 函式 / 方法                               | 功能說明                  |
# | ------------------------------------- | --------------------- |
# | `oled.buffer`                         | 底層緩衝區位元組陣列，可直接讀寫像素    |
# | `oled.image(pil_image)`               | 將一個 PIL.Image 物件寫入緩衝區 |
# | `Image.new(mode, (width, height))`    | 建立新的影像畫布（1-bit 黑白）    |
# | `ImageDraw.Draw(image)`               | 在 PIL.Image 上作繪圖      |
# | `ImageFont.load_default()`            | 載入預設字型                |
# | `ImageFont.truetype(font_path, size)` | 載入 TTF 字型，可顯示自定字型     |


# 清空螢幕
oled.fill(0)
oled.show()

# 1. 建立一張和螢幕一樣大的空白黑色畫布 (image)
#    模式 "1" 代表這是一張黑白圖片
image = Image.new("1", (oled.width, oled.height))

# 2. 取得一隻可以在這張畫布上作畫的畫筆 (draw)
draw = ImageDraw.Draw(image)

# 3. (可選) 用畫筆在畫布上畫一個黑色的長方形，確保背景是全黑的
draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)


# 4. 載入一個字型。我們可以使用系統內建的字型讓字體更好看、更大
#    如果這行報錯，可以換成 font = ImageFont.load_default()
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
except IOError:
    font = ImageFont.load_default()

# 5. 使用畫筆，在畫布的指定位置寫上文字
text = "Hello!"
draw.text((40, 22), text, font=font, fill=255) # (x, y)座標, 文字內容, 字型, 顏色(255=白)

# 6. 最後，將我們完成的整張畫布，「貼」到 OLED 螢幕上
oled.image(image)
oled.show()


print("螢幕應該已經顯示 'Hello!'。")
print("程式將在顯示 10 秒後，自動清空螢幕並結束。")

# 讓圖片持續顯示 10 秒
time.sleep(10)

# 結束前再次清空螢幕
oled.fill(0)
oled.show()

print("程式結束。")
