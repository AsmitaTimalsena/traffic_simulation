import random

class TrafficSignal:
    def __init__(self, roads, config={}):
        self.roads = roads
        self.set_default_config()
        self.init_properties()

    def set_default_config(self):
        self.cycle = [
            (False, False, False, True),  # Green for North-South (3.75 seconds)
            (False, False, True, False),  # Yellow for North-South (3.75 seconds)
            (False, True, False, False),  # Red for North-South, Green for East-West (3.75 seconds)
            (True, False, False, False)   # Yellow for East-West (3.75 seconds)
        ]
        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 12
        self.cycle_length = 15  # Set cycle length to 15 seconds

        self.current_cycle_index = 0
        self.last_t = 0

    def init_properties(self):
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self, i)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]

    def update(self, sim):
        cycle_length = self.cycle_length
        # randomize the cycle length after every cycle
        if sim.t % cycle_length == 0:
            cycle_length = random.randint(15, 30)  # Randomize between 15 and 30 seconds
        k = (sim.t // cycle_length) % 4
        self.current_cycle_index = int(k)
        if len(self.roads) < 4:
            self.current_cycle_index = 3