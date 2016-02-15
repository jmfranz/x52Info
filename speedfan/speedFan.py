from ctypes import * 
import mmap

class SFMemory(Structure): 
	_pack_ = 1 
	_fields_ = [ 
		('version', c_short), 
		('flags', c_short), 
		('MemSize', c_int), 
		('handle', c_int), 
		('NumTemps', c_short), 
		('NumFans', c_short), 
		('NumVolts', c_short), 
		('temps', c_int*32), 
		('fans', c_int*32), 
		('volts', c_int*32), 
	]

	def __init__(self):
		self.size = sizeof(SFMemory)
		self.buf = mmap.mmap(0, self.size, "SFSharedMemory_ALM", mmap.ACCESS_READ)

	def readTempsGpuCpu(self,gpuIDX,cpuIDX):
		self.buf.seek(0)
		mem = self.buf.read(self.size)
		sfm = cast(mem, POINTER(SFMemory)).contents
		assert(sfm.version == 1)
		assert(sfm.MemSize == self.size)

		temps = list(map(lambda t: t / 100.0, sfm.temps[:sfm.NumTemps]))

		return (temps[gpuIDX],temps[cpuIDX])

	def readFanSpeed(self, gpuIDX,cpuIDX):
		self.buf.seek(0)
		mem = self.buf.read(self.size)
		sfm = cast(mem, POINTER(SFMemory)).contents
		assert(sfm.version == 1)
		assert(sfm.MemSize == self.size)

		fans = list(map(lambda t: t, sfm.fans[:sfm.NumFans]))
		return (fans[gpuIDX],fans[cpuIDX])





# size = sizeof(SFMemory)
# buf = mmap.mmap(0, size, "SFSharedMemory_ALM", mmap.ACCESS_READ)

# buf.seek(0)
# mem = buf.read(size)
# sfm = cast(mem, POINTER(SFMemory)).contents

# print ("Version: %u Flags: %u, MemSize: %u, Handle: 0x%08X" % (sfm.version, sfm.flags, sfm.MemSize, sfm.handle))

# assert(sfm.version == 1)
# assert(sfm.MemSize == size)

# temps = list(map(lambda t: t / 100.0, sfm.temps[:sfm.NumTemps]))

# print ("Temps: " + str(temps))