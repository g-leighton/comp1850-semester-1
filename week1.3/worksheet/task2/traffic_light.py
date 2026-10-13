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

while systime <= maxtime:
    
    for clock in range (states["red"] + states["red_amber"] + states["green"] + states["amber"]):
        print(f"Clock: {clock}")
        if clock <= (states["red"] - 1):
            state = "red"
            print(f"Time {systime:03} State {state}")
            clock += 1
        
        elif clock > (states["red"] - 1) and clock <= (states["red"] + states["red_amber"] - 1):
            state = "red_amber"
            print(f"Time {systime:03} State {state}")
            clock += 1

        elif clock > (states["red"] + states["red_amber"] - 1) and clock <= (states["red"] + states["red_amber"] + states["green"] - 1):
            state = "green"
            print(f"Time {systime:03} State {state}")
            clock += 1
        
        elif clock > (states["red"] + states["red_amber"] + states["green"] - 1) and clock <= (states["red"] + states["red_amber"] + states["green"] + states["amber"] - 1):
            state = "amber"
            print(f"Time {systime:03} State {state}")

            if clock == (states["red"] + states["red_amber"] + states["green"] + states["amber"] - 1):
                clock = 0
                print(f"Clock: {clock}")

            else:
                clock += 1
        
        systime += 1
    
    


""" for time in range (maxtime):
    timer = 0
    while systime < maxtime: 
        print(f"Time {systime:03} State {state}")
    
        systime += 1

    state = states[timer] !!
    time += 1 """
    


# At the end of each step you should output the time and state using the statement on line 14