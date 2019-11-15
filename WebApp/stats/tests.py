from django.test import TestCase
import datetime
from .models import *
from .views import importLog
from datetime import datetime
from datetime import date

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
		d = date(2019, 11, 15)
		log1 = StatsLog(event = 1, roomID = "311", timeStamp = d)
		log1.save()
		afterLogs1 = importLog("311", datetime.now(), "day")
		print(afterLogs1[len(afterLogs1)-1].timeStamp.day)
