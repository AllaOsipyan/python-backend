from random import randint
dictionary = {}
class Car:
    def __init__(self, name, max_speed, drag_coef, time_to_max):
        self._name = name
        self._max_speed = max_speed
        self._drag_coef = drag_coef
        self._time_to_max = time_to_max

class Weather:
    def __init__(self, wind_speed):
        self._wind_speed = wind_speed
    @property
    def get_wind_speed(self):
        return self._wind_speed

class Competition(object):
    def __init__(self, value):
        self.value = value
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Competition,  cls).__new__(cls)
            return cls.instance
        else:
            raise Exception('Нельзя создавать более одного экземпляра класса')
def start(competitors, weather, distances):
    for car in competitors:
        competitor_time = 0
        for distance in range(distances.value):
            _wind_speed = randint(0, weather.get_wind_speed)
            if competitor_time == 0:
                _speed = 1
            else:
                _speed = (competitor_time / car._time_to_max) * car._max_speed
                if _speed > _wind_speed:
                    _speed -= (car._drag_coef * _wind_speed)

            competitor_time += float(1) / _speed
        dictionary[car._name] = competitor_time

competitors = (Car('ferrary', 340, 0.324, 26),
               Car('bugatti', 407, 0.39, 32),
               Car('toyota', 180,0.25,40),
               Car('lada', 180,0.32,56),
               Car('sx4', 180,0.33,44))
distances = Competition(10000)
weather = Weather(20)
start(competitors,  weather, distances)
k=1
for el in sorted(dictionary.items(), key=lambda x: x[1]):
    print("Place: %d Car: <%s> Result: %f" % (k, el[0], el[1]))
    k+=1