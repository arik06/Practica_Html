class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
        def add_passengers(self, name):
            if not self.open_seats():
                return False
            self.passengers.append(name)
            return True
        
        def open_seats(self):
            return  self.capacity - len(self.passengers)
        
            flight = Flight(3)
            
            people = ['pepe', 'camila', 'atreus', 'mascara', 'rosa']
            for person in people:
                success = flight.add_passenger(people)
                if success:
                    print(f'{people} added to the flight')
                else:
                    print(f'{people} could not be added to the flight')