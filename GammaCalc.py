#+++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#This is to calculate the value for one's gamma and beta#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++#
import numpy as np



##################################
#These are the initial parameters#
##################################

Massp = 938.27208	# Mass of a Proton (MeV/c^2)
e = 1.602177E-19	# Elementary Charge
clight = 299792458	# Speed of Light
Gx = 150



###############################################################################
#This function prints the values of the relativistic beta, gamma, and momentum#
###############################################################################

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
