# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simulation.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10simulation.proto\x12\x0fSimulation.Data\"*\n\tEventData\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\"~\n\tFrameData\x12\x0f\n\x07\x66rameID\x18\x01 \x01(\x05\x12,\n\ttrackBoxs\x18\x02 \x03(\x0b\x32\x19.Simulation.Data.TrackBox\x12#\n\x04lans\x18\x03 \x03(\x0b\x32\x15.Simulation.Data.Lane\x12\r\n\x05speed\x18\x04 \x01(\x05\"\'\n\x12\x46reeSpaceRoadBound\x12\x11\n\tboundData\x18\x01 \x01(\x0c\"F\n\x10PointCloudV3Data\x12\x32\n\x0bpointClouds\x18\x01 \x03(\x0b\x32\x1d.Simulation.Data.PointCloudV3\"D\n\x10TrafficLightInfo\x12\x30\n\tlightInfo\x18\x01 \x03(\x0b\x32\x1d.Simulation.Data.TrafficLight\"M\n\rVehicleMotion\x12\x12\n\nsteerAngle\x18\x01 \x01(\x02\x12\x13\n\x0bmotorTorque\x18\x02 \x01(\x02\x12\x13\n\x0b\x62rakeTorque\x18\x03 \x01(\x02\"6\n\x07\x41PAData\x12+\n\x08\x61paParks\x18\x01 \x03(\x0b\x32\x19.Simulation.Data.ParkInfo\"\xcd\x02\n\x08ParkInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06number\x18\x02 \x01(\x05\x12\x36\n\x06status\x18\x03 \x01(\x0e\x32&.Simulation.Data.ParkInfo.OccupyStatus\x12.\n\x0c\x42oundingBoxs\x18\x04 \x03(\x0b\x32\x18.Simulation.Data.PointV3\x12\x34\n\x08parkType\x18\x05 \x01(\x0e\x32\".Simulation.Data.ParkInfo.TypePark\"D\n\x0cOccupyStatus\x12\x0b\n\x07unknown\x10\x00\x12\x08\n\x04\x66ree\x10\x01\x12\x0c\n\x08Occupied\x10\x02\x12\x0f\n\x0b\x64\x65stination\x10\x03\"A\n\x08TypePark\x12\x0f\n\x0bunknownPark\x10\x00\x12\x10\n\x0cVerticalPark\x10\x01\x12\x12\n\x0eHorizontalPark\x10\x02\"*\n\x07PointV3\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"\x1f\n\x07PointV2\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"E\n\x0cPointCloudV3\x12\'\n\x05\x63oord\x18\x01 \x01(\x0b\x32\x18.Simulation.Data.PointV3\x12\x0c\n\x04type\x18\x02 \x01(\x05\"\x94\x01\n\x08TrackBox\x12\r\n\x05objID\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12+\n\tcenterPos\x18\x03 \x01(\x0b\x32\x18.Simulation.Data.PointV3\x12\x0f\n\x07heading\x18\x04 \x01(\x02\x12\x0e\n\x06length\x18\x05 \x01(\x02\x12\r\n\x05width\x18\x06 \x01(\x02\x12\x0e\n\x06height\x18\x07 \x01(\x02\">\n\x04Lane\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12(\n\x06points\x18\x02 \x03(\x0b\x32\x18.Simulation.Data.PointV2\"h\n\x0bVehicleInfo\x12\r\n\x05speed\x18\x01 \x01(\x05\x12\x0f\n\x07heading\x18\x02 \x01(\x02\x12\x39\n\x17VehicleWorldCoordinates\x18\x03 \x01(\x0b\x32\x18.Simulation.Data.PointV3\"?\n\x0cTrafficLight\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x12\t\n\x01z\x18\x04 \x01(\x02*I\n\x07\x43\x61rType\x12\x0b\n\x07unknown\x10\x00\x12\x07\n\x03\x62us\x10\x01\x12\x07\n\x03\x63\x61r\x10\x02\x12\x08\n\x04\x66iat\x10\x03\x12\n\n\x06\x66urgao\x10\x04\x12\t\n\x05truck\x10\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'simulation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CARTYPE']._serialized_start=1397
  _globals['_CARTYPE']._serialized_end=1470
  _globals['_EVENTDATA']._serialized_start=37
  _globals['_EVENTDATA']._serialized_end=79
  _globals['_FRAMEDATA']._serialized_start=81
  _globals['_FRAMEDATA']._serialized_end=207
  _globals['_FREESPACEROADBOUND']._serialized_start=209
  _globals['_FREESPACEROADBOUND']._serialized_end=248
  _globals['_POINTCLOUDV3DATA']._serialized_start=250
  _globals['_POINTCLOUDV3DATA']._serialized_end=320
  _globals['_TRAFFICLIGHTINFO']._serialized_start=322
  _globals['_TRAFFICLIGHTINFO']._serialized_end=390
  _globals['_VEHICLEMOTION']._serialized_start=392
  _globals['_VEHICLEMOTION']._serialized_end=469
  _globals['_APADATA']._serialized_start=471
  _globals['_APADATA']._serialized_end=525
  _globals['_PARKINFO']._serialized_start=528
  _globals['_PARKINFO']._serialized_end=861
  _globals['_PARKINFO_OCCUPYSTATUS']._serialized_start=726
  _globals['_PARKINFO_OCCUPYSTATUS']._serialized_end=794
  _globals['_PARKINFO_TYPEPARK']._serialized_start=796
  _globals['_PARKINFO_TYPEPARK']._serialized_end=861
  _globals['_POINTV3']._serialized_start=863
  _globals['_POINTV3']._serialized_end=905
  _globals['_POINTV2']._serialized_start=907
  _globals['_POINTV2']._serialized_end=938
  _globals['_POINTCLOUDV3']._serialized_start=940
  _globals['_POINTCLOUDV3']._serialized_end=1009
  _globals['_TRACKBOX']._serialized_start=1012
  _globals['_TRACKBOX']._serialized_end=1160
  _globals['_LANE']._serialized_start=1162
  _globals['_LANE']._serialized_end=1224
  _globals['_VEHICLEINFO']._serialized_start=1226
  _globals['_VEHICLEINFO']._serialized_end=1330
  _globals['_TRAFFICLIGHT']._serialized_start=1332
  _globals['_TRAFFICLIGHT']._serialized_end=1395
# @@protoc_insertion_point(module_scope)