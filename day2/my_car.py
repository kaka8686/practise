from day2.car import Car

"""

Version: 0.1
Author: Spike

"""


# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.update_odometer(21)
# my_new_car.read_odometer()
print("This is a hello new method ")

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(-100)
my_used_car.read_odometer()