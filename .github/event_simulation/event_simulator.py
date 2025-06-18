from event import Event

class EventSimulator:
    def __init__(self):
        self.events = []
        self.tick_count = 0

    def add_event(self, event):
        self.events.append(event)

    def tick(self):
        self.tick_count += 1
        print(f"\nTick {self.tick_count}")

        for event in self.events[:]:
            event.tick()
            if event.is_expired():
                print(f"❌ Event expired: {event.name}")
                self.events.remove(event)
            elif event.should_age():
                event.apply_aging()
                print(f"⚠️ Aging applied: {event.name} -> Priority: {event.priority}")

        # Optional: Sort by priority (highest first)
        self.events.sort(key=lambda e: e.priority, reverse=True)

        self.print_state()

    def print_state(self):
        print("📦 Active Events:")
        for event in self.events:
            print(f" - {event}")
