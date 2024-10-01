from logic import *

# 1 Define symbols for the conditions
rain = Symbol("rain")          # Weather: raining
HeavyTraffic = Symbol("HeavyTraffic")  # Traffic: heavy traffic
EarlyMeeting = Symbol("EarlyMeeting")  # Meetings: early meeting
Strike = Symbol("Strike")      # Public Transport Strike

# 2 Define symbols for commuting options
WFH = Symbol("WFH")                  # Work From Home
Drive = Symbol("Drive")              # Drive to work
PublicTransport = Symbol("PublicTransport")  # Take public transport

# 3 Define the knowledge base (rules)
knowledge = And(
    # Rule 1: If it's raining or there's an early meeting, work from home
    Implication(Or(rain, EarlyMeeting), WFH),

    # Rule 2: If it's not raining and there's no heavy traffic, drive to work
    Implication(And(Not(rain), Not(HeavyTraffic)), Drive),

    # Rule 3: If there's no strike and it's not raining, take public transport
    Implication(And(Not(Strike), Not(rain)), PublicTransport)
)

# 4 Define conditions
    # You can modify the True/False values to change the scenario

conditions = And( rain,     # It's raining (True)
    Not(HeavyTraffic), # There's no heavy traffic (False)
    Not(EarlyMeeting), # No early meeting (False)
    Not(Strike)        # No public transport strike (False)
)

    # Combine the facts with the rules
knowledge = And(conditions, knowledge)

# 5 Queries to check with the knowledge base

print("Should you work from home?", model_check(knowledge, WFH))
print("Should you drive?", model_check(knowledge, Drive))
print("Should you take public transport?", model_check(knowledge, PublicTransport))
