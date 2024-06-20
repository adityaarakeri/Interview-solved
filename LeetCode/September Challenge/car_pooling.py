"""
Car Pooling
-----------
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)
Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.
Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 
 
Example 1:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Example 3:
Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true

Example 4:
Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
"""

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        time = []
        
        for trip in trips:
            time.append([trip[1], trip[0]])
            time.append([trip[2], - trip[0]])
            
        time.sort()

        total_passengers_at_a_time = 0
        
        for ele in time:
            total_passengers_at_a_time+=ele[1]
            if total_passengers_at_a_time > capacity:
                return False
            
        return True
        