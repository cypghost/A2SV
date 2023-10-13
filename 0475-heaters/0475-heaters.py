class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        radius = 0

        for house in houses:
            left_heater_index = bisect.bisect_right(heaters, house) - 1
            right_heater_index = bisect.bisect_left(heaters, house)

            left_heater = heaters[left_heater_index] if left_heater_index >= 0 else float('-inf')
            right_heater = heaters[right_heater_index] if right_heater_index < len(heaters) else float('inf')

            dist_left = house - left_heater
            dist_right = right_heater - house

            radius = max(radius, min(dist_left, dist_right))

        return radius
