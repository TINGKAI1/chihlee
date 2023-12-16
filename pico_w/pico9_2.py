from machine import Timer

def callback1(t):
    print(type(t))
    
time1 = Timer()
time1.init(freq=1,callback=callback1)