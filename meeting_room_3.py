'''
Intution

We need sorted values at every turn to make a decision. 

There is one data dstructure which comes into the role whenever
we need something like this that is heap



We need 2 heaps here 

- available room ( to keep track of rooms in sorted order everytime some room becomes available with ascending order priority)
- busy room (at certain time we might need to select a room from the busy room with the least end time
 every time we schdule a new meeting)


1. Pop all the rooms if they are available at certain time 
2. If there is a room available
	- pop from available (min heap)
	- push into the busy (min heap)
3. If not available 
	- pop from the busy (min heap)
	- push the new room to busy room (min heap)


'''
import heapq as hq
# meetings is an array of [start-time, end-time]
def solve(meetings, n):

	# initialize the states (data structures as we require)

	available_rooms = [x for x in range(n)]
	busy_rooms = [] # this will store the tuple (endtime of the room and the room number)

	count = [0]*n

	meetings.sort()

	for start_time, end_time  in meetings:

		while busy_rooms and busy_rooms[0][0]<= start_time:

			# pop this room 
			_end_time , room  = hq.heappop(busy_rooms)
			# push this room to avaialable
			hq.heappush(available_rooms, room)

		if available_rooms:
			room  =hq.heappop(available_rooms)
			hq.heappush(busy_rooms, (end_time, room))

		else: # there is not available room pop from the busy room in sorted way from the latest ending meeting
			#the catch is thart we need to define the endtime with caution
			# new_end_time = popped_end_time - start_time + end_time because popped_end_time > start_time
			popped_end_time , room= hq.heappop(busy_rooms)
			hq.heappush(busy_rooms, ((popped_end_time - start_time + end_time), room))

		count[room] +=1

	return count.index(max(count))


# Time complexity -> sorting + heap insert/delete in n iterations
# O(nlogn) + O(n*logn)
print(solve([[0,10],[1,5],[2,7],[3,4]], 2))