import threading
lock = threading.Lock()

from xr_motor import RobotDirection
go = RobotDirection()

import xr_config as cfg

from xr_ultrasonic import Ultrasonic 
ultrasonic = Ultrasonic()

from xr_infrared import Infrared

inf = Infrared()

import time

def avoid_walls():
	while True:  
		distance = ultrasonic.get_distance()
		if int(distance) < 20 and distance != 0:
			print(distance)
			lock.acquire()
			go.stop()
			cfg.LEFT = 30
			cfg.RIGHT = 30
			go.back()
			time.sleep(0.35)
			go.left()
			time.sleep(0.2)
			go.stop()
			lock.release()
		l, r = inf.get_lr()
		if not l and not r:
			lock.acquire()
			go.stop()
			cfg.LEFT = 30
			cfg.RIGHT = 30
			go.back()
			time.sleep(0.35)
			go.stop()
			lock.release()
		if l and not r:
			lock.acquire()
			go.stop()
			cfg.LEFT = 30
			cfg.RIGHT = 30
			go.back()
			time.sleep(0.30)
			go.right()
			time.sleep(0.2)
			go.stop()
			lock.release()
		if r and not l:
			lock.acquire()
			go.stop()
			cfg.LEFT = 30
			cfg.RIGHT = 30
			go.back()
			time.sleep(0.30)
			go.left()
			time.sleep(0.2)
			go.stop()
			lock.release()
		time.sleep(0.05)		
