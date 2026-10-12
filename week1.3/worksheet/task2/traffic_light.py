"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: George Leighton
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

time = 0
while time <= maxtime:
    """ for i in range (maxtime):
        if i <= 3:
            state = red
        elif """
    if time <= 3:
        state = red
    elif time > 3 and time <= 6:
        state = red_amber
    elif time > 6 and time <= 1
    print(f"Time {systime:03} State {state}")
    systime += 1
    time += 1
    


# At the end of each step you should output the time and state using the statement on line 14