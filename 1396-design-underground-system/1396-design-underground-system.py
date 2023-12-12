class UndergroundSystem:

    def __init__(self):
        # Dictionary to store total travel time and count for each (start_station, end_station) pair
        self.average = defaultdict(list)

        # Dictionary to store check-in information with customer_id as key and (start_station, check_in_time) as value
        self.checkin = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkin:
            start_station, check_in_time = self.checkin.pop(id)
            travel = (start_station, stationName)
            travel_time = t - check_in_time

            self.average[travel].append(travel_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = (startStation, endStation)
        travel_times = self.average[travel]

        return sum(travel_times) / len(travel_times) if travel_times else 0.0

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)