#Problem: Implement an exponential backoff strategy that doubles the wait time between retries,
# starting from 1 second, but stops after 5 retries.

import time     #telling Python to use the time module,which has a function called sleep() that pauses the program.

wait_time = 1       

for retry in range(1,6):            #This loop will run 5 times: retry = 1, 2, 3, 4, 5.

    print(f"retry count goes: {retry} , waiting time {wait_time} seconds")

    time.sleep(wait_time)           #This tells Python: "Wait for this many seconds" before going to the next retry..

    wait_time = wait_time * 2           #This doubles the wait time each time: