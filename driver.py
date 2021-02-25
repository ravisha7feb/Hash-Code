from car import Car
from street import Street

def read_car_details(file, street_no):
    cars = []
    
    for line in file.readlines()[street_no + 1:]:
        no_of_paths, routes = int(line.split(' ')[0]), line.split(' ')[1:]
        cars.append(Car(routes)) 
        
    return cars

def read_street_details(file, streets_no):
    streets = []
    
    for line in file.readlines()[1: streets_no + 1]:
        start, end, name, travel_time = line.split(' ')
        streets.append(Street(name, start, end, travel_time))
        
    return streets

def read_misc_data(file):
    simulation_dur, intersection_no, streets_no, cars_no, bonus = file.readlines()[0].split(' ')

    return simulation_dur, intersection_no, streets_no, cars_no, bonus

if __name__ == '__main__':
    simulation_dur, intersection_no, streets_no, cars_no, bonus = read_misc_data("input1.txt")
    streets = read_street_details("input1.txt", streets_no)
    cars = read_car_details("input1.txt", streets_no)
    