"""Using decorators, add getter and setter methods to your Car class so you can view and change the color of your car. You should also add getter methods that let you view but not modify the car's model and year. Don't forget to write some tests."""

class Car:
    
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self._speed = 0
    
    @staticmethod
    def turn_on():
        print("Car is on")
    
    @color.setter
    def set_color(self, color):
        if type(color) != str:
            print("Color must be a string")
        else:
            self._color = color
    
    @property
    def color(self):
        return self._color
    
    @property
    def year(self):
        return self._year
    
    @property
    def model(self):
        return self._model
    
    def accelerate(self, number):
        self._speed += number
        print(f"You accelerated {number} miles per hour")
    
    def brake(self, number):
        self._speed -= number
        print(f"You decelerated {number} miles per hour")
    
    def turn_off(self):
        self._speed = 0
        print("Car is off")
    
    def get_speed(self):
        print(f"Car speed is {self._speed}")
    
    def spray_paint(self, color):
        self._color = color
        print(f"You spray your car {color}"")
    
    @classmethod
    def car_mileage(cls, miles_traveled, gas burned):
        print(miles_traveled/gas_burned)
        
lumina = Car('chevy lumina', 1997, 'white')

lumina.get_speed()