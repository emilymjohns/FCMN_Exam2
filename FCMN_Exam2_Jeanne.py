import math

# Constants
R = 8.314    # J/(mol*K), universal gas constant
T = 310      # K, body temperature
F = 96485    # C/mol, Faraday's constant
# Given concentrations
K_in = 120.0  # mM

# Function to calculate Nernst potential in mV given inside and outside K+ concentrations
def nernst_potential(K_out, K_in):
    # Nernst equation (in volts):
    # E = (R*T / F) * ln([K_out]/[K_in])
    E = (R * T / F) * math.log(K_out / K_in)
    # Convert to mV
    return E * 1000

# Calculate E_K for 3 mM and 4 mM
E_K_3mM = nernst_potential(3.0, K_in)
E_K_4mM = nernst_potential(4.0, K_in)

# Calculate the difference
difference = E_K_4mM - E_K_3mM

print(f"E_K at K_out=3 mM: {E_K_3mM:.2f} mV")
print(f"E_K at K_out=4 mM: {E_K_4mM:.2f} mV")
print(f"Difference (4 mM - 3 mM): {difference:.2f} mV")
