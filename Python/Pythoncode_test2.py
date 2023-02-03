import serial
from tkinter import *
import time

ser = serial.Serial('COM3',115200) #serial port ini
window = Tk() #tkinter 實例化
data = 0.0
def turnonLED():
    ser.write(b't')
    time.sleep(0.1)
    while ser.in_waiting:         # 若收到序列資料…
        data_raw = ser.readline()  # 讀取一行
        data = data_raw.decode().split()  # 用預設的UTF-8解碼
        print(data)
        var.set(data)

    

def turnoffLED():
    ser.write(b'h')
    time.sleep(0.1)
    while ser.in_waiting:         # 若收到序列資料…
        data_raw1 = ser.readline()  # 讀取一行
        data1 = data_raw1.decode().split()   # 用預設的UTF-8解碼
        print(data1)
        var1.set(data1)

def blinkLED():
    buf=[]
    ser.write(b'b')
    time.sleep(0.5)
    while ser.in_waiting:         # 若收到序列資料…
        data_raw2 = ser.readline()  # 讀取一行
        data2 = data_raw2.decode()   # 用預設的UTF-8解碼
        buf = data2.split()
        print(buf[0],buf[1])

        var.set(buf[0])
        var1.set(buf[1])
        

window.title('Read T/H GUI')
btn_on = Button(window,text='Read Temperature',command=turnonLED)
btn_on.grid(row=0,column=0)

btn_off = Button(window,text='Read Humidity',command=turnoffLED)
btn_off.grid(row=0,column=1)

btn_both = Button(window,text='Read Both',command=blinkLED)
btn_both.grid(row=0,column=2)

temperatureLabel = Label(window,text="Temperature")
temperatureLabel.grid(row=2,column=0)
var = StringVar()
temperatureLabel2 = Label(window,textvariable=var,bg='yellow',fg = 'green')
temperatureLabel2.grid(row=2,column=1)

temperatureLabe3 = Label(window,text="Humidity")
temperatureLabe3.grid(row=3,column=0)
var1 = StringVar()
temperatureLabel4 = Label(window,textvariable=var1,bg='yellow',fg = 'green')
temperatureLabel4.grid(row=3,column=1)

window.geometry('500x350')

window.mainloop()

