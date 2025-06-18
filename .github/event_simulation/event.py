class Event:
    def __init__(self, name, expiry_time, priority):
        self.name = name
        self.waiting_time = 0
        self.expiry_time = expiry_time
        self.priority = priority

    def tick(self):
        self.waiting_time += 1

    def should_age(self):
        return self.waiting_time > 0 and self.waiting_time % 5 == 0

    def apply_aging(self):
        self.priority += 1

    def is_expired(self):
        return self.waiting_time >= self.expiry_time

    def __repr__(self):
        return f"{self.name} (Wait: {self.waiting_time}, Expire: {self.expiry_time}, Priority: {self.priority})"
