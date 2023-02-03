print("Hello World !")
print("非創建者第一次修改")
print("創建者第二修改")
print("新增Python資料夾並把程式移至新資料夾內")
print("整備去確認練習")
print("整備去確認練習2")
print("new branch test1")
import serial
from tkinter import *
import time

ser = serial.Serial('COM3',115200) #serial port ini
window = Tk() #tkinter 實例化
def turnonLED():
    if blinkState.get() == 1:
        blinkLED()
    else:
        ser.write(b'o')

def turnoffLED():
    ser.write(b'x')

def blinkLED():
    if blinkState.get() == 1:
        ser.write(b'b')
        time.sleep(1)
        delay = userDelay.get()
        ser.write(delay.encode())

blinkState = IntVar()
chkBtn_Blink = Checkbutton(window,text = "Blink", variable = blinkState, command = blinkLED )
chkBtn_Blink.grid(row=0,column=2)

blinkTime = ['50','100','200','400','600','800','1000','1200']
userDelay = StringVar()
delayMenu = OptionMenu(window,userDelay,*blinkTime)
userDelay.set('800')
delayLabel = Label(window,text="Blink (ms)")
delayLabel.grid(row=0,column=3)
delayMenu.grid(row=0,column=4)

window.title('Blink GUI')
btn_on = Button(window,text='Turn On',command=turnonLED)
btn_on.grid(row=0,column=0)

btn_off = Button(window,text='Turn Off',command=turnoffLED)
btn_off.grid(row=0,column=1)


window.geometry('350x350')

window.mainloop()

try:
    while True:
        while ser.in_waiting:          # 若收到序列資料…
            data_raw = ser.readline()  # 讀取一行
            data = data_raw.decode()   # 用預設的UTF-8解碼
            # print('接收到的原始資料：', data_raw)
            if "Temperature: " in data:
                print(data.replace("Temperature: ",'溫度: '))
            else:
                print(data.replace("Humidity: ",'濕度: '))
            # print('接收到的資料：', data)


except KeyboardInterrupt:
    ser.close()    # 清除序列通訊物件
    print('再見！')

