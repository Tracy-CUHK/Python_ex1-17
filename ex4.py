cars = 100 # assign value to car
space_in_a_car = 4 # assign value to space_in_a_car
drivers = 30 # assign value to drivers
passengers = 90 # assign value to passengers
cars_not_driven = cars - drivers # compute cars_not_driven
cars_driven = drivers # compute cars_driven
carpool_capacity = cars_driven * space_in_a_car # compute carpool_capacity
average_passengers_per_car = passengers / cars_driven #c compute average_
# passengers_per_car


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."