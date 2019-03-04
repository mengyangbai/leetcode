import heapq
class BestSolution:
    def minRefuelStops(self, target, start_fuel, stations):
        stations.append([target, 0])
        pq_passed_stations = []
        tank = start_fuel
        ret = 0

        for mile, gas in stations:
            while pq_passed_stations and tank < mile:
                tank += -heapq.heappop(pq_passed_stations)
                ret += 1

            if tank < mile:
                return -1

            heapq.heappush(pq_passed_stations, -gas)

        return ret

# using heapq will accerate
class MySolution:
    def minRefuelStops(self, target: int, startFuel: int, stations: [[int]]) -> int:
        # Last station status
        # distance, fuel contained, stops
        previous_status_stack = [[0,startFuel,0]]

        stations.append([target,0])

        # station by station
        for station in stations:
            
            new_status_stack=[]

            #from previous to new
            for previous_status in previous_status_stack:

                # can reach
                if previous_status[1] - station[0] + previous_status[0]>= 0:
                    # add fuel
                    status1 = [station[0],previous_status[1] - station[0] + previous_status[0]+station[1], previous_status[2]+1]
                    # no add fuel
                    status2 = [station[0],previous_status[1] - station[0] + previous_status[0],previous_status[2]]

                    new_status_stack.append(status1)
                    new_status_stack.append(status2)

            
            if len(new_status_stack) == 0:
                return -1

            previous_status_stack = new_status_stack

        result = min(stack[2] for stack in previous_status_stack)

        return result


a = BestSolution()
print(a.minRefuelStops(100,10, [[10,60],[20,30],[30,30],[60,40]]))
                    


