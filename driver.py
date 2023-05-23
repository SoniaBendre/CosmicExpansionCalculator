from CosmicExpansionCalculator import CosmicExpansionCalculator

data = {
    "Cancer": {
        "Redshift": 0.016,
        "Radial velocity (km/s)": 4800
    },
    "Coma": {
        "Redshift": 0.022,
        "Radial velocity (km/s)": 6700
    },
    "Corona Borealis": {
        "Redshift": 0.072,
        "Radial velocity (km/s)": 21600
    },
    "Fornax": {
        "Redshift": 0.005,
        "Radial velocity (km/s)": 1400
    },
    "Hercules": {
        "Redshift": 0.034,
        "Radial velocity (km/s)": 10300
    },
    "Leo": {
        "Redshift": 0.065,
        "Radial velocity (km/s)": 19500
    },
    "Pegasus I": {
        "Redshift": 0.013,
        "Radial velocity (km/s)": 3700
    },
    "Ursa Major II": {
        "Redshift": 0.137,
        "Radial velocity (km/s)": 41000
    }
}

# Dictionary to store instances of CosmicExpansionCalculator
expansion_calculators = {}

for key in data:
    # Create an instance of the CosmicExpansionCalculator class
    expansion_calculators[key] = CosmicExpansionCalculator(f"{key} cluster")
    expansion_calculators[key].getImageFromTarget()

