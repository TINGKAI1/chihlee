import network

nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('KAI','88888888')

max_wait = 10
while max_wait > 0:
    max_wait -= 1
    time.sleep(1)

while not nic.isconnected() and nic.status() >= 0:
    print("等待連線")
    
    
print("有可能沒有wifi主機")
print("已經連線成功")

print(nic.ifconfig())