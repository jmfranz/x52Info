import time
from speedfan.speedFan import SFMemory

myMem = SFMemory()

try:
    while True:
        print (str(myMem.readTempsGpuCpu(0,10)))
        time.sleep(1)
except KeyboardInterrupt:
    pass

