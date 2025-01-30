"""
PA 02 - Hunter Wilson 
--------------------------------
An object's momentum is its mass multiplied by its velocity. 
The kinetic energy of an object is defined as 
KE = (1/2)mv2 where m is the object's mass and v is its velocity. 
Write a program that accepts an object's mass (in kilograms) and velocity (in meters per second) 
as inputs and then outputs its momentum and kinetic energy.
"""

# Prompt user for mass and velocity
mass_kg = float(input("Please enter the mass of the object (kilograms) "))
velocity_mps = float(input("Please enter the velocity of the object (meters per second): "))

# Calculate momentum (mass * velocity)
momentum = mass_kg * velocity_mps

# Calculate kinetic energy (1/2 * mass * velocity^2)
kinetic_energy = (1/2) * mass_kg * (velocity_mps ** 2)

# Output results
print("momentum =", momentum, "kg m/s")
print("kinetic energy =", kinetic_energy, "joules")