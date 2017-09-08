'''
This is to calculate the value for one's gamma and beta
'''
import numpy as np

Massp = 938.27208	# Mass of a Proton (MeV/c^2)
e = 1.602177E-19	# Elementary Charge
clight = 299792458	# Speed of Light
Gx = 150

def Gamma():
		KE = float(input("Please input value for Kinetic Energy (MeV): "))
		Erest = Massp
		Gamma = (KE/(Erest)) + 1
		Etot = Gamma*Massp
		Beta = np.sqrt(1-(1/Gamma))
		print("The value for gamma is: "+str(Gamma))
		print("The value for beta is: "+str(Beta))
		answer = str(input("Would you like to calculate the Momentum? (Y/N): "))
		if answer == "Y":
			P = np.sqrt(Etot**2 - (Massp)**2)
			print("The momentum of the particle is "+str(P)+" MeV/c.")
		elif answer == "N":
			pass
		else: 
			print("Next time, try 'Y' or 'N'.")
Gamma()

def MRig():
    a = float(input("Please input lower value for Kinetic Energy range (MeV): "))
    b = float(input("Please input upper value for Kinetic Energy range (MeV): "))
    c = float(input("Please input number of Kinetic Energies: "))
    KE = np.linspace(a,b,c)
    Erest = Massp
    Gamma = []
    Etot = []
    P = []
    K = []
    for i in range(0,len(KE)):
        Gamma.append((KE[i]/(Erest)) + 1)
        Etot.append(Gamma[i]*Massp/1000)
        P.append(3.3356*np.sqrt(Etot[i]**2 - (Massp/1000)**2))
        K.append(Gx/(P[i]))
    print(P)
    print(K)
#MRig()
