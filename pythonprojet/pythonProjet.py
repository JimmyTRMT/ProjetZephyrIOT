import serial 
import matplotlib.pyplot as plt 

ser = serial.Serial('/dev/ttyUSB0', 115200) 
data = [] 

for i in range(100): 
    line = ser.readline().decode(errors="ignore").strip() 
    if not line: 
        continue
    try:
        r,ir= map(int, line.split()) 
        data.append(r) 
    except ValueError: 
        continue 

plt.plot(data) 
plt.title('Capteur') 
plt.show()
plt.savefig('ppgg.png')