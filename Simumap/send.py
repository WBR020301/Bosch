import socket
import time
from simulation_pb2 import EventData, VehicleMotion

# 设置 UDP 地址和端口
UDP_IP = "127.0.0.1"
UDP_PORT = 9001

# 创建 UDP 套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def publish_vehicle_motion(speed, steer_angle):
    vehicle_motion = VehicleMotion()
    vehicle_motion.steerAngle = steer_angle
    vehicle_motion.motorTorque = speed
    vehicle_motion.brakeTorque = 0.0

    # 序列化车辆运动数据
    payload = vehicle_motion.SerializeToString()

    # 创建 EventData
    event_data = EventData()
    event_data.type = "VehicleMotion"
    event_data.payload = payload

    # 序列化 EventData
    serialized_data = event_data.SerializeToString()

    # 发送数据
    sock.sendto(serialized_data, (UDP_IP, UDP_PORT))
    print(f"Sent EventData: Type={event_data.type}, Speed={speed}, SteerAngle={steer_angle}")

# 模拟车辆移动
speed = 0.0
steer_angle = 0.0

try:
    while True:
        speed += 5.0
        if speed > 60:
            speed = 0

        publish_vehicle_motion(speed, steer_angle)
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

# 关闭套接字
sock.close()