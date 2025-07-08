from gpiozero import LED
from time import sleep

# gpiozero 函式庫非常聰明，它知道 "LED" 這個特殊名稱代表的就是主機板上內建的活動燈 (ACT)
led = LED(17)

print("程式開始... 請觀察你的樹莓派上的綠色燈。")
print("按下鍵盤的 Ctrl+C 可以中斷程式。")

# 建立一個無限迴圈，讓燈持續閃爍
try:
    while True:
        led.on()    # 開燈
        # print("燈亮") # 你可以取消這兩行的註解，在終端機看到更多訊息
        sleep(1)    # 等待 1 秒
        led.off()   # 關燈
        # print("燈暗")
        sleep(1)    # 等待 1 秒

# 當我們按下 Ctrl+C 時，程式會在這裡被攔截，並執行下面的程式碼
except KeyboardInterrupt:
    print("\n程式已結束。")
