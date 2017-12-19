import threading
import time
import ctypes
import inspect

class timer(threading.Thread):  # The timer class is derived from the class threading.Thread
	def __init__(self, num, interval):
		threading.Thread.__init__(self)
		self.thread_num = num
		self.interval = interval
		self.thread_stop = False

	def run(self):  # Overwrite run() method, put what you want the thread do here
		while not self.thread_stop:
			print 'Thread Object(%d), Time:%s\n' % (self.thread_num, time.ctime())
			time.sleep(self.interval)

	def stop(self):
		self.thread_stop = True

# def _async_raise(tid, exctype):
# 	"""raises the exception, performs cleanup if needed"""
# 	tid = ctypes.c_long(tid)
# 	if not inspect.isclass(exctype):
# 		exctype = type(exctype)
# 	res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
# 	if res == 0:
# 		raise ValueError("invalid thread id")
# 	elif res != 1:
# 		# """if it returns a number greater than one, you're in trouble,
# 		# and you should call it again with exc=NULL to revert the effect"""
# 		ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
# 		raise SystemError("PyThreadState_SetAsyncExc failed")
#
# def stop_thread(thread):
# 	_async_raise(thread.ident, SystemExit)

def test():
	thread1 = timer(1, 1)
	thread2 = timer(2, 2)
	thread1.start()
	thread2.start()
	time.sleep(10)
	# stop_thread(thread1)
	# stop_thread(thread2)
	thread1.stop()
	thread2.stop()
	return

if __name__ == '__main__':
	test()