import simpy
from models import Vehicle

city = simpy.Environment()
vehicle = Vehicle(city)
city.run(until=20)