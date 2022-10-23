import subprocess

Bodies=3
M=10000000
VMax=1000
Mass=500000000000000000000000

input=f".\\x64\\Debug\\NBodyVSol.exe {Bodies} {M} {VMax} {Mass} > nbody.dat"

print("Running")
result=subprocess.run(input,shell=True,capture_output=True)
print("Ran")

import visor3D
    
