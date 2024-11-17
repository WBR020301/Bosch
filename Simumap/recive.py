import zmq
from simulation_pb2 import TrafficLightInfo

# 创建 ZMQ 上下文
context = zmq.Context()

# 创建订阅者套接字
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://127.0.0.1:5556")

# 订阅交通信号灯主题
subscriber.setsockopt_string(zmq.SUBSCRIBE, "TrafficLightData")

print("Waiting for messages...")

while True:
    try:
        # 接收消息
        topic, msg = subscriber.recv_multipart()
        topic = topic.decode('utf-8')  # 解码主题
        print(f"Received topic: {topic}")

        if topic == "TrafficLightData":
            traffic_light_info = TrafficLightInfo()
            traffic_light_info.ParseFromString(msg)  # 反序列化消息
            for light in traffic_light_info.lightInfo:
                print(f"Traffic Light Status: {light.status}, Position: ({light.x}, {light.y}, {light.z})")

    except KeyboardInterrupt:
        print("Exiting...")
        break

    except Exception as e:
        print(f"Error: {e}")

# 关闭套接字和上下文
subscriber.close()
context.term()