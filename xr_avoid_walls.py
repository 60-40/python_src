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
		if int(ultrasonic.get_distance()) < 20:
			lock.acquire()
			go.stop()
			cfg.LEFT = 30
			cfg.RIGHT = 30
			go.backward()
			time.sleep(0.15)
			go.left()
			time.spleep(0.1)
			go.stop()
			lock.release()
		l, r = inf.get_lr()
		if not l and not r:
			lock.acquire()
			go.stop()
			cfg.LEFT = 30
			cfg.RIGHT = 30
			go.backward()
			time.sleep(0.15)
			go.stop()
			lock.release()
		if l and not r:
			lock.acquire()
			go.stop()
			cfg.LEFT = 30
			cfg.RIGHT = 30
			go.right()
			time.sleep(0.15)
			go.stop()
			lock.release()
		if r and not l:
			lock.acquire()
			go.stop()
			cfg.LEFT = 30
			cfg.RIGHT = 30
			go.left()
			time.sleep(0.15)
			go.stop()
			lock.release()
		time.sleep(0.05)		
