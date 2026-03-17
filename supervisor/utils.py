from functools import wraps
import time


def raise_not_implemented(obj):
	"""Raise NotImplementedError"""

	@wraps(obj)
	def __inner(*args, **kwargs):
		raise NotImplementedError("{0.__name__} '{1.__name__}' not implemented!".format(type(obj), obj))

	return __inner

def time_machine(frame_time):
	"""Create a frame timer"""
	last_frame = time.time()

	while True:
		current_time = time.time()
		delta_time = current_time - last_frame

		if delta_time < frame_time:
			time_to_sleep = frame_time - delta_time
			# Fix the bug caused by time backward adjustment that makes delta_time negative,
			# which would cause time_to_sleep to become a very large number and make the program sleep too long
			time_to_sleep = min(time_to_sleep, frame_time)
			time.sleep(time_to_sleep)

		last_frame = time.time()
		yield