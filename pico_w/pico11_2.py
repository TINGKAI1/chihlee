import network

nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('KAI','88888888')

max_wait = 10

#處理正在連線
while max_wait > 0:
    max_wait -= 1
    status = nic.status()
    if status < 0 or status >=3:
        break
    print("等待連線")
    time.sleep(1)


#沒有wifi的處理
if nic.status() != 3:
    #連線失敗,重新開機
    #wdt = WDT(timeout=2000)
    #wdt.feed()
    raise RuntimeError("連線失敗")
    
else:
    print("連線成功")
    print(nic.ifconfig())