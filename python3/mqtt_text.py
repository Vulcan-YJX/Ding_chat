import paho.mqtt.client as mqtt
# 任意一个数值即可。只要与你自己的其他设备不重复即可。
Device_id = "1" 

UserName = "公众号获取的username"
Password = "公众号获取的Password"
# MQTT服务器地址
MQTT_BROKER = 'vulcanyjx.top'

# 订阅的主题 用户只能订阅自己UserName下的Topic
# /voice 为关键 key 代表微信语音转文字
MQTT_TOPIC_SUBSCRIBE = UserName + '/voice'
# 发布的主题 用户只能向自己UserName下的Topic发布数据
MQTT_TOPIC_PUBLISH = UserName + '/text'
# 客户端ID
CLIENT_ID = UserName + Device_id

# 当客户端接收到来自服务器的CONNACK响应时，调用此回调函数
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # 订阅主题
    client.subscribe(MQTT_TOPIC_SUBSCRIBE)

# 这是当接收到服务器发送的消息时的回调函数
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic} with QoS {message.qos}")

# 创建MQTT客户端实例并设置客户端ID
client = mqtt.Client(CLIENT_ID)
client.username_pw_set(UserName, Password)
# 设置回调函数
client.on_message = on_message
client.on_connect = on_connect
# 连接到MQTT服务器 (替换为你的服务器地址和端口)
client.connect(MQTT_BROKER, 1883)
# 订阅一个主题
client.subscribe(MQTT_TOPIC_SUBSCRIBE)
# 开始循环以处理网络流量和回调函数，
# 它将一直阻塞直到程序被关闭或者client.loop_stop()被调用
client.loop_forever()