import time
import cv2
import numpy as np
from pyardrone import ARDrone
from pyardrone import at



drone = ARDrone()
drone.send(at.CONFIG("custom:application_id", "2902050D"))
drone.send(at.CONFIG("custom:session_id", "2902150D"))
drone.send(at.CTRL(5,0))

drone.send(at.CONFIG_IDS("2902150D","00000000","2902050D"))
drone.send(at.CONFIG("custom:application_desc", "andet"))
drone.send(at.CTRL(5,0))
drone.send(at.CTRL(4,0))
drone.send(at.CTRL(5,0))

drone.send(at.CONFIG_IDS("2902150D", "00000000", "2902050D"))
drone.send(at.CONFIG("video:video_codec","131"))
drone.send(at.CTRL(5,0))
drone.send(at.CTRL(4,0))
drone.send(at.CTRL(5,0))

drone.send(at.CONFIG_IDS("2902150D", "00000000", "2902050D"))
drone.send(at.CONFIG("video:max_bitrate", "4000"))

drone.navdata_ready.wait()

first = 1
try:
	while True:

		if drone.video_ready.is_set():
			pic = drone.frame
			print("Video Rdy")
			if pic is not None:
				if first == 0:
					if not np.array_equal(pic,lastPic):
						cv2.imshow('image', pic)			
						cv2.waitKey(1)
				lastPic = pic
				first = 0
except KeyboardInterrupt:
	
	cv2.destroyAllWindows()





