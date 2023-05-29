from CosmicExpansionCalculator import CosmicExpansionCalculator
import matplotlib.pyplot as plt
import numpy as np

data = {
    "Virgo": {
        "Redshift": None,
        "Radial velocity (km/s)": None,
        "Largest diameter (mm)": 3,
    },
    "Cancer": {
        "Redshift": 0.016,
        "Radial velocity (km/s)": 4800,
        "Largest diameter (mm)": 3,
    },
    "Coma": {
        "Redshift": 0.022,
        "Radial velocity (km/s)": 6700,
        "Largest diameter (mm)": 2.5,
    },
    "Corona Borealis": {
        "Redshift": 0.072,
        "Radial velocity (km/s)": 21600,
        "Largest diameter (mm)": 0.8,
    },
    "Fornax": {
        "Redshift": 0.005,
        "Radial velocity (km/s)": 1400,
        "Largest diameter (mm)": 6,
    },
    "Hercules": {
        "Redshift": 0.034,
        "Radial velocity (km/s)": 10300,
        "Largest diameter (mm)": 1.3,
    },
    "Leo": {
        "Redshift": 0.065,
        "Radial velocity (km/s)": 19500,
        "Largest diameter (mm)": 0.5,
    },
    "Pegasus I": {
        "Redshift": 0.013,
        "Radial velocity (km/s)": 3700,
        "Largest diameter (mm)": 4,
    },
    "Ursa Major II": {
        "Redshift": 0.137,
        "Radial velocity (km/s)": 41000,
        "Largest diameter (mm)": 0.2,
    }
}

# Dictionary to store instances of CosmicExpansionCalculator
expansion_calculators = {}

distances = [0]
velocities = [0]

for key in data:
    # Create an instance of the CosmicExpansionCalculator class
    expansion_calculators[key] = CosmicExpansionCalculator(f"{key} cluster")
    expansion_calculators[key].getImageFromTarget()
    # Calculate the distance to the cluster
    data[key]["Cluster Distance (Mpc)"] = expansion_calculators[key].calculateDistance(
        data["Virgo"]["Largest diameter (mm)"], data[key]["Largest diameter (mm)"])
    if key != "Virgo":
        distances.append(data[key]["Cluster Distance (Mpc)"])
        velocities.append(data[key]["Radial velocity (km/s)"])
    print("Calculated distance for", key, "cluster:",
          data[key]["Cluster Distance (Mpc)"])


print(data)
#calculate the slope of the regression line using least squares method
slope = np.sum(np.array(distances) * np.array(velocities)) / np.sum(np.array(distances) ** 2)
regression_line = slope * np.array(distances)

# Plot the data
plt.scatter(distances, velocities, label='Data')
plt.plot(distances, regression_line, color='red', label='Regression Line')
plt.xlabel("Distance (Mpc)")
plt.ylabel("Recessional Velocity (km/s)")
plt.title("Hubble's Law")
plt.grid(True)


# Calculate Age of Universe from Hubbles Constant
Hubbles_Constant = slope
print(f"Hubbles_Constant: {Hubbles_Constant} km/s/Mpc")

Hubble_age_in_pc = Hubbles_Constant / (10**6)
print(
    f"Hubbles Constant km/s/pc = Hubbles_Constant / (10^6) = {Hubble_age_in_pc} km/s/pc")

Hubble_age_per_second = Hubble_age_in_pc / (3*(10**13))
print(
    f"Hubble age per second = Hubble age in pc / (3 x (10^13)) = {Hubble_age_per_second}")

Hubble_age_per_year = Hubble_age_per_second * (3.1*(10**7))
print(
    f"Hubble age per year = Hubble age per second x 3.1 x (10^7) = {Hubble_age_per_year}")

age_of_universe = 1 / Hubble_age_per_year
print(f"Age of Universe = 1 / Hubble age per year = {age_of_universe} years")

# Display the plot
plt.show()
