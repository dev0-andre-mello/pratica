x_km = int(input('Enter the distance traveled in kilometers: '))
y_fuel = float(input('Enter the amount of fuel consumed in liters: '))

consumption = x_km / y_fuel
print(f"{consumption:.3f} km/l")
