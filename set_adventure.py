# Objective: The aim of this assignment is to deepen your understanding and application of Python sets in various scenarios, ranging from basic operations to advanced manipulations and best practices. You will correct given codes, use sets in everyday contexts, and tackle challenges that require creative thinking and problem-solving.

# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Destinations that both airlines fly to.
common_destinations = our_routes.intersection(competitor_routes)

# Destinations unique to your airline.
unique_routes = our_routes.difference(competitor_routes)

# Whether there are any destinations that neither airline shares.
other_routes = our_routes.symmetric_difference(competitor_routes)

print(f'''
Our routes : {our_routes}
Competitor routes: {competitor_routes}

Destinations both airlines fly to:
- {common_destinations}

Destinations only our airlines fly to:
- {unique_routes}

Destinations neither airlines share:
-{other_routes}

''')