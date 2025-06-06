class Car():
  """A simple attempt to represent a car."""

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    long_name = str(self.year) + ' ' + self.make + self.model
    return long_name.title()

  def read_odometer(self):
    print("This car has " + str(self.odometer_reading) + " miles on it.")

  def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back the odometer!")

  def increment_odometer(self, miles):
    self.odometer_reading += miles


class ElectricCar(Car):
  """Represent aspects of a car, specific to electric vehicles."""

  def __init__(self, make, model, year):
    """Initialize attributes of the parent class."""
    super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model 3', 2019)
print(my_tesla.get_descriptive_name())


