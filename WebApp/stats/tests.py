from django.test import TestCase
#import datetime
from .models import *
from .views import *
from datetime import datetime as dt
import pytz

class RoomUsageModelTest(TestCase):

# 	def testDefaultValues(self) {
# 		'''
# 		Tests the RoomUsage model with defualt values
# 		'''
# 		room = Room(roomID = '302-A', occupied = False, lastEntered = datetime.now(), lastExited = datetime.now(), roomType = 'Group')
# 		occupancy = OccupancyStats(totalOccupancy = 0)
# 		roomUsage = RoomUsage(room = room, occupancyStats = occupancy, currentDate = datetime.now())
# 		# test string representation of models
# 		self.assertEqual(str(room), 'Room: ' + roomUsage.room.roomID)
# 		self.assertEqual(str(occupancy), 'Total Occupancy: ' + str(roomUsage.occupancyStats.totalOccupancy))
# 		self.assertEqual(str(roomUsage), 'Usage for ' + roomUsage.room.roomID)
# 		# test default total occupancy
# 		self.assertEqual(roomUsage.occupancyStats.totalOccupancy, 0)
# 	}
	@classmethod
	def setUpTestData(cls):
		print("SET UP")
		# assert(False == True)
		# print(beforeLog1.timeStamp)
		# day301 = createTimeObject(301, "day", now)
		# month301 = createTimeObject(301, "month", now)
		# year301 = createTimeObject(301, "year", now)
		# day302 = createTimeObject(302, "day", now)
		# month302 = createTimeObject(302, "month", now)
		# year302 = createTimeObject(302, "year", now)

	#test logs are saved properly
	@classmethod
	def testLog(self):
		d1 = dt(2019, 11, 15, 2, 35, 2)
		print("ORIGINAL: ",d1)
		#Creates test events that occurr
		log1 = StatsLog(event = 1, roomID = "311", date = d1)
		log1.save()
		d2 = dt(2019, 11, 15, 2, 40, 3)
		log2 = StatsLog(event = 0, roomID = "311", date = d2)
		log2.save()
		d3 = dt(2019, 11, 15, 3, 30, 4)
		log3 = StatsLog(event = 1, roomID = "311", date = d3)
		log3.save()
		d4 = dt(2019, 11, 15, 4, 37, 23)
		log4 = StatsLog(event = 1, roomID = "311", date = d4)
		log4.save()
		d5 = dt(2019, 11, 15, 8, 23, 12)
		log5 = StatsLog(event = 0, roomID = "311", date = d5)
		log5.save()
		d6 = dt(2019, 11, 15, 0, 20, 5)
		log6 = StatsLog(event = 0, roomID = "311", date = d6)
		log6.save()
		#End of creating test events
		timeObject = Day()
		timeObject.roomID = "311"
		#dt(Year Month Day Hour Minute Seconds)
		timenow = dt(2019, 11, 15, 10, 37, 23)
		#Creates the test day to create statistics for
		timeObject.date = timenow
		duration = "day"
		logList = importLog("311", timenow, duration)
		print(logList)
		#Calculates the statistics for that day and then saves
		timeObject.totalOccupants = getOccupants(logList, duration)
		timeObject.avgOccLength = calcAvgOccLength(logList, duration)
		print(timeObject.avgOccLength)
		timeObject.save()

		"""
		#Testing month statistics
		#Begin creating test events
		month1 = dt(2021, 2, 3, 5, 13, 6)
		logMonth1 = StatsLog(event = 1, roomID = "311", date = month1)
		logMonth1.save()
		month2 = dt(2021, 2, 3, 6, 34, 32)
		logMonth2 = StatsLog(event = 0, roomID = "311", date = month2)
		logMonth2.save()
		month3 = dt(2021, 2, 5, 7, 12, 53)
		logMonth3 = StatsLog(event = 1, roomID = "311", date = month3)
		logMonth3.save()
		month4 = dt(2021, 2, 5, 8, 31, 13)
		logMonth4 = StatsLog(event = 0, roomID = "311", date = month4)
		logMonth4.save()
		#End of creating test events
		timeObject2 = Month()
		timeObject2.roomID = "311"
		#dt(Year Month Day Hour Minute Seconds)
		timenow2 = dt(2021, 2, 15, 12, 32, 9)
		timeObject2.date = timenow2
		duration2 = "month"
		logList2 = importLog("311", timenow2, duration2)
		print(logList2)
		print("Time object2 date:", timeObject2.date)
		timeObject2.totalOccupants = getOccupants(logList2, duration2)
		timeObject2.avgOccLength = calcAvgOccLength(logList2, duration2)
		print(timeObject2.avgOccLength)
		print("Saving time")
		timeObject2.save()
		"""
		