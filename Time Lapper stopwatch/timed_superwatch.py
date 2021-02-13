import time
print("ENTER to Begin. Afterwards, press ENTER to 'click' the stopwatch.Press Ctrl+C to quit")

input()
print("Started")
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
	while True:
		input()
		laptime = round(time.time() - lastTime , 2)
		totalTime = round(time.time() - startTime, 2)
		print("Lap #%s: %s (%s)" % (lapNum , totalTime , laptime) , end="")
		lapNum += 1
		lastTime = time.time()
except KeyboardInterrupt:
		print("\nDone")