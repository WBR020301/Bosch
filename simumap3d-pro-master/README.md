# SimuMap3D Pro

#### 介绍
SimuMap3D仿真自动驾驶采集数据平台,根据unity3D开发的仿真环境，可以采集输出BEV视角下的，车辆、车道线等数据。

#### 软件架构
软件架构说明

#### 使用说明
QQ交流群：763063996

SimuMap3D支持使用zeroMQ、UDP作为通讯协议，发布输出数据。

方式一：接收数据使用zeroMQ订阅模式。

网络端口 5556
示例："tcp://127.0.0.1:5556"

topic字段：
xx.Subscribe("RoadLaneData")车道线
	
xx.Subscribe("VehicleInfoData")自车信息
	
xx.Subscribe("TrafficLightData")交通信号灯

xx.Subscribe("RoadBoundData")道路区域

方式二：UDP通讯
网络端口：9001
使用EventData类反序列化订阅数据

type是数据message类型字段

payload是序列化后的各类型数据

SimuMap3D数据以阻塞式发布，请求一帧，下发一帧数据

#### 切换通讯模式
更改程序目录下：SimuMap Pro 0.10\SimuMap Pro 0.10_Data\StreamingAssets中network配置文件

#### 车辆控制
开启Vehicle中外部数据控制

通过EventData类上传VehicleMotion数据

代码示例：

```c#

EventData @event = new EventData();
@event.Type = "VehicleMotion";
VehicleMotion vehicleMotion = new VehicleMotion() { SteerAngle = 0.0f, MotorTorque = 30.0f, BrakeTorque = 0.0f };
@event.Payload = MessageExtensions.ToByteString(vehicleMotion);

SocketSend(@event);

```

#### Proto接口

```protobuf
syntax = "proto3";

package Simulation.Data;

message EventData{
 //type ="FrameData";type="FreeSpaceRoadBound";type="TrafficLightInfo";
 string type=1;
 bytes payload=2;
}

message FrameData{
  int32 frameID = 1;
  //trackBoxs:动态障碍物
  repeated TrackBox trackBoxs= 2;
  //lans:车道线
  repeated Lane lans= 3;
  int32 speed = 4;
}

message FreeSpaceRoadBound{
  //boundData 道路区域 256*256*3二值化图像
  bytes boundData = 1;
}

message PointCloudV3Data{
  //pointClouds:点云
  repeated PointCloudV3 pointClouds= 1;
}

message TrafficLightInfo{
  //lightInfo:红绿灯
  repeated TrafficLight lightInfo = 1;
}

message VehicleMotion{
  //前轮转向角度
  float steerAngle = 1;
  //后轮驱动力
  float motorTorque = 2;
  //制动 默认0不制动
  float brakeTorque = 3;
}

message APAData{
   repeated ParkInfo apaParks = 1;
}

message ParkInfo{
  int32 id = 1;
  int32 number = 2;
  OccupyStatus status = 3;
  repeated PointV3 BoundingBoxs = 4;
  TypePark parkType = 5;
  
  enum OccupyStatus{
   //未知状态
   unknown = 0;
   //空闲状态
   free = 1;
   //占用状态
   Occupied = 2;
   //选择可入库状态
   destination = 3;
  }
  enum TypePark{
    unknownPark = 0;
	//垂直库位
    VerticalPark = 1;
	//水平库位
    HorizontalPark = 2;
  }
}

message PointV3{
 float x = 1;
 float y = 2;
 float z= 3;
}
message PointV2{
 float x = 1;
 float y = 2;
}
message PointCloudV3{
  PointV3 coord= 1;
  int32 type = 2;
}

message TrackBox{
  int32 objID= 1;
  //CarType
  int32 type= 2;
  //车辆坐标
  PointV3 centerPos= 3;
  //车辆朝向
  float heading= 4;
  float length= 5;
  float width= 6;
  float height= 7;
}

message Lane{
  // 1 虚车道线，2 行人斑马线，3 道路边界线，4 左右车道中间分界线（黄实线）
  int32 type = 1;
  repeated PointV2 points = 2;
}

message VehicleInfo{
  int32 speed = 1;
  float heading = 2;
  PointV3 VehicleWorldCoordinates= 3;
}

message TrafficLight{
  int32 status = 1;
  float x = 2;
  float y = 3;
  float z = 4;
}
enum CarType
{
    unknown = 0;
    bus = 1;
    car = 2;
    fiat = 3;
    furgao = 4;
    truck = 5;
}
```
#### 参考
https://zeromq.org/