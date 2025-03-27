import random

class TrafficSignal:
    def __init__(self, roads, config={}):
        # Initialize roads
        self.roads = roads
        # Set default configuration
        self.set_default_config()

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)
        # Calculate properties
        self.init_properties()

    def set_default_config(self):
        # Ciclo del semaforo con semafori opposti attivati insieme
        self.cycle = [
            (True, False, True, False),  # Nord e Sud verdi, Est e Ovest rossi
            (False, True, False, True)   # Est e Ovest verdi, Nord e Sud rossi
        ]
        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 12
        self.cycle_length = 2  

        self.current_cycle_index = 0
        self.last_t = 0

        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 12
        self.cycle_length = 5  

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
        # Cambia fase ogni 'cycle_length' secondi
        k = int(sim.t // self.cycle_length) % len(self.cycle)
        self.current_cycle_index = k




