from event_simulator import EventSimulator
from event import Event
import time

simulator = EventSimulator()

simulator.add_event(Event("Order A", expiry_time=7, priority=1))
simulator.add_event(Event("Order B", expiry_time=10, priority=2))

for _ in range(12):
    simulator.tick()
    time.sleep(1)  # optional delay to simulate real time
