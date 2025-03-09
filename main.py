import gymnasium as gym  # Thư viện mô phỏng CartPole
import keyboard  # Thư viện bắt phím từ người dùng

class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp  # Hệ số Proportional (tỉ lệ)
        self.Ki = Ki  # Hệ số Integral (tích lũy)
        self.Kd = Kd  # Hệ số Derivative (dự đoán)
        self.prev_error = 0
        self.integral = 0

    def compute(self, error, dt):
        self.integral += error * dt  # Tích lũy lỗi
        if dt > 0:
            derivative = (error - self.prev_error) / dt #Dự đoán xu hướng
        else:
            derivative = 0
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative  # Tính giá trị điều khiển
        self.prev_error = error  # Cập nhật lỗi trước đó
        return output


# Khởi tạo môi trường
env = gym.make("CartPole-v1", render_mode="human")

# Tăng số bước tối đa
env._max_episode_steps = 10000  #tăng số lượng bước tối đa lên 10000, mặc định của nó là 500

pid = PIDController(Kp=3.0, Ki=0.1, Kd=0.2)

observation, _ = env.reset()
dt = 0.02  

print("Nhấn 'q' để kết thúc trò chơi.")
# Reset để lấy trạng thái ban đầu

observation, _ = env.reset()

while True:
    env.render()
    
    theta = observation[2]  # Lấy góc nghiêng của gậy (rad) theo phương x;
    
    # Tính toán PID
    action_value = pid.compute(theta, dt)

    if action_value > 0:
        action = 1
    else:
        action = 0
 # Nếu giá trị > 0 thì đi phải, ngược lại đi trái

    # Thực hiện hành động
    observation, _, terminated, truncated, _ = env.step(action)
    done = terminated or truncated
    
    if done:
        observation, _ = env.reset()  # Reset game nếu gậy bị ngã

    if keyboard.is_pressed("q"):  # Nhấn 'q' để thoát game
        print("\nTrò chơi kết thúc bởi người dùng.")
        break

env.close()
