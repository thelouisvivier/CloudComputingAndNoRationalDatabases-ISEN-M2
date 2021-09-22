class Station:
    def __init__(self, station_id, name, address, coordinates_x, coordinates_y, capacity, available, available_bikes, available_slots, pos):
        self.station_id = station_id
        self.name = name
        self.address = address
        self.coordinates = [coordinates_x, coordinates_y]
        self.capacity = capacity
        self.available = available
        self.available_bikes = available_bikes
        self.available_slots = available_slots
        self.pos = pos

