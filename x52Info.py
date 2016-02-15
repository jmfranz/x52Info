import time
import psutil
import math

from mfd import X52ProMFD
from speedfan.speedFan import SFMemory

mfd = X52ProMFD()
myMem = SFMemory()

try:
    while True:
        temps = myMem.readTempsGpuCpu(0,10)
        fans = myMem.readFanSpeed(1,0)
        cpuPercentage = math.ceil(psutil.cpu_percent())
        ramUsed = math.ceil(psutil.virtual_memory().percent)

        tempsLine = "GPU:" + str(int(temps[0])) +"°"
        tempsLine += " CPU:" + str(int(temps[1])) +"°"
        
        percentageLine = "CPU:" + str(cpuPercentage).zfill(2) + "%"
        percentageLine += " RAM:" + str(ramUsed) +  "%"

        fanLine = "CPU: " + str(fans[0]) + " RPM"

        mfd.display(line1=tempsLine,line2=percentageLine,line3=fanLine)


        time.sleep(1)
except KeyboardInterrupt:
    pass