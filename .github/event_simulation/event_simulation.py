

from collections import deque

class Event:
    def __init__(self, name, expiry_time, priority=0):
        self.name = name
        self.waiting_time = 0
        self.expiry_time = expiry_time
        self.priority = priority

    def tick(self):
        self.waiting_time += 1

    def should_age(self):
        return self.waiting_time % 3 == 0

    def apply_aging(self):
        self.priority += 1

    def is_expired(self):
        return self.waiting_time >= self.expiry_time

    def __str__(self):
        return f"{self.name} (Wait: {self.waiting_time}, Expire: {self.expiry_time}, Priority: {self.priority})"

class EventSimulator:
    def __init__(self):
        self.queue = deque()
        self.tick_count = 0

    def add_event(self, name, expiry_time, priority=0):
        self.queue.append(Event(name, expiry_time, priority))

    def tick(self):
        self.tick_count += 1
        expired_events = []

        for event in list(self.queue):
            event.tick()
            if event.is_expired():
                expired_events.append(event)
            elif event.should_age():
                event.apply_aging()

        for event in expired_events:
            self.queue.remove(event)


        self.queue = deque(sorted(self.queue, key=lambda e: e.priority, reverse=True))

    def get_active_events(self):
        return list(self.queue)

    def __str__(self):
        return "\n".join(str(event) for event in self.queue)



