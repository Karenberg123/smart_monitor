import random
import time

def read_mock_data():
    """
    這是一個模擬函數，用來產生假的溫濕度數據。
    """
    # 產生一個 20.0 到 30.0 之間的隨機溫度，並四捨五入到小數點後兩位
    mock_temperature = round(random.uniform(20.0, 30.0), 2)

    # 產生一個 40.0% 到 60.0% 之間的隨機濕度，並四捨五入到小數點後兩位
    mock_humidity = round(random.uniform(40.0, 60.0), 2)

    return mock_temperature, mock_humidity

# --- 主程式從這裡開始 ---
print("啟動模擬感測器... 每 2 秒讀取一次數據。")
print("按下 Ctrl+C 可以中斷程式。")

try:
    while True:
        # 呼叫我們的模擬函數來取得數據
        temp, humidity = read_mock_data()

        # 使用 f-string 格式化輸出，讓版面更美觀
        print(f"讀取成功: 溫度 = {temp}°C, 濕度 = {humidity}%")

        # 等待 2 秒
        time.sleep(2)

except KeyboardInterrupt:
    print("\n程式已結束。")
