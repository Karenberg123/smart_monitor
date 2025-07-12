import time
import board
import adafruit_ahtx0

# 1. 初始化 I2C 與感測器 (這部分已經幫你寫好)
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

print("準備開始讀取 AHT20 感測器數據...")
time.sleep(2) # 等待 2 秒讓感測器穩定

# 2. 建立一個無限迴圈
try:
    while True:
        # --- 你的程式碼寫在這裡 ---
        
        # 任務 A: 讀取溫度，並把它存到一個叫做 temp 的變數中
        # (提示: 使用 sensor.temperature)
        temp = sensor.temperature

        # 任務 B: 讀取濕度，並把它存到一個叫做 humidity 的變數中
        # (提示: 使用 sensor.relative_humidity)
        humidity = sensor.relative_humidity

        # 任務 C: 使用 f-string 把溫度和濕度格式化後印出來
        # (提示: print(f"溫度: {temp:.1f} C, 濕度: {humidity:.1f} %") )
        #         :.1f 代表格式化到小數點後一位
        print(f"溫度：'{temp:.1f} C', 濕度:'{humidity:.1f} %'")


        # 任務 D: 讓程式暫停 2 秒
        # (提示: 使用 time.sleep() )
        time.sleep(2)
        
        # -------------------------
        
        pass # 這是暫時的佔位符，請把它換成你自己的程式碼

except KeyboardInterrupt:
    print("\n程式結束")