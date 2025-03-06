import gymnasium as gym  # Thư viện mô phỏng CartPole
import numpy as np
import keyboard  # Thư viện bắt phím từ người dùng

# Khởi tạo môi trường
env = gym.make("CartPole-v1", render_mode="human")

# Reset để lấy trạng thái ban đầu
observation, _ = env.reset()

while True:  # Chạy liên tục
    if keyboard.is_pressed("q"):  # Kiểm tra nếu người dùng nhấn 'q'
        print("\nTrò chơi kết thúc bởi người dùng.")
        break

    env.render()
env.close()