# CIS 3680 - Assessment #1

# Ask for input
islandName = input("Enter Island Nation: ")
population = input("Enter population: ")
lifeExpectancy = float(input("Enter life expectancy: "))
avgAgeInfection = float(input("Average Age of Infection: "))

# Calculate the Reproduction: Avg Life Expectancy / Avg Age of Infection
def ReproductionCalc():
    return lifeExpectancy / avgAgeInfection

# Calculate Herd Immunity Threshold: 1 - (1/Reproduction)
def HerdImmunityCalc(reproduction):
    return (1 - (1 / reproduction))

# Calculate the estimated number of doses: Herd Immunity * Population Size
def DosesCalc(immunity, population):
    return (immunity * float(population))

# call functions to calculate
reproduction = ReproductionCalc()
herdImmunity = HerdImmunityCalc(reproduction)
doses = DosesCalc(herdImmunity, population)

# Print output
print(f"Base Reproduction Number: {reproduction:.4f}")
print(f"Herd Immunity Threshold: {herdImmunity:.8f}")
print(f"Doses Required for {islandName}: {doses:.2f}")
