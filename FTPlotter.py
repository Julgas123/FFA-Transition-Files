'''''''''''''''''''''''''''''''''''''''''''''
This is to ease the process for FFAG stuff
'''''''''''''''''''''''''''''''''''''''''''''
import numpy as np
import matplotlib.pyplot as plt




'''''''''''''''''''''''''''''''''
parameters for the FFAG Below
'''''''''''''''''''''''''''''''''
Massp = 938.27208	# Mass of a Proton (MeV/c^2)
e = 1.602177E-19	# Elementary Charge
clight = 299792458	# Speed of Light
G = 52.6	# Gradient


'''''''''''''''''''''''''''''''''''''''''''''
This bit creates the Lists and opens the files
'''''''''''''''''''''''''''''''''''''''''''''
Nt = 16
Ft = []
KL = []
b = []
PL = []
PL2 = []
#PL3 = []
#PL4 = []
#PL5 = []
#PL6 = []
#PL7 = []
q = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
	"AA","BB","CC","DD","EE","FF","GG","HH","II","JJ","KK","LL","MM","NN","OO","PP","QQ","RR","SS","TT","UU","VV","WW","XX","YY","ZZ"]	
for i in range(0,int(Nt)):
	k = i/(Nt+1)
	b.append(k-k**2)
	KL.append(k)




'''''''''''''''''''''''''''''''''''''''
The snippet below is the equation Ft(x)
'''''''''''''''''''''''''''''''''''''''
for i in range(0,len(KL)):
	#Ft.append(0.5 + (KL[i] - 0.5)*(1 + 0.894*2*(b[i]) + 0.659*6*(b[i]**2) + 0.329*20*(b[i]**3)))
	Ft.append(np.sin((np.pi/2)*KL[i])**2)
	#Ft.append(KL[i])
	#Ft.append(1-np.exp(-5*(KL[i])**2))
	#Ft.append(-(2.7*KL[i])**(37/10)+(3.7*KL[i])**(27/10))

MagnetF1 = []
MagnetD1 = []
MagnetF2 = [34.13557756,33.93129417,33.53816077,32.98436706,32.30642228,31.54428325,30.73716883,29.9206418,29.12503102,28.37494511,27.68952818,27.08313012,26.56614248,26.14583753,25.82711726,25.58595001]
MagnetD2 = [-23.0199042,-22.90903594,-22.69465829,-22.39039668,-22.01429413,-21.58670095,-21.12834656,-20.65885535,-20.19578817,-19.75415936,-19.34632206,-18.98210178,-18.66907083,-18.41288137,-18.21759847,-18.06925416]
for i in range(0,16):
	MagnetF1.append(i)
	MagnetD1.append(i)
	MagnetF1[i]=34.13557756
	MagnetD1[i]=-23.0199042
for i in range(0,16):	
	MagnetF2[i]=MagnetF2[i]
	MagnetD2[i]=MagnetD2[i]
List=[]
for i in range(1,17):
	List.append(i)

'''''''''''''''''''''''''''''''''''''''
The snippet below varies the parameters
'''''''''''''''''''''''''''''''''''''''	
BetXi=0.69
BetYi=0.66
BetXf=1.035
BetYf=0.99
AlfXi=0
AlfYi=0
AlfXf=0
AlfYf=0
Xi=0.0000
Xf=0.0
DXi=0.0
DXf=0.0
DPXi=0.0
DPXf=0.0
for i in range(0,len(Ft)):
	PL.append((1-Ft[i])*BetXi+Ft[i]*BetXf)	# BetaX
	PL2.append((1-Ft[i])*BetYi+Ft[i]*BetYf)	# BetaY
	#PL3.append((1-Ft[i])*AlfXi+Ft[i]*AlfXf)	# AlphaX
	#PL4.append((1-Ft[i])*AlfYi+Ft[i]*AlfYf)	# AlphaY
	#PL5.append((1-Ft[i])*Xi+Ft[i]*Xf)
	#PL6.append((1-Ft[i])*DXi+Ft[i]*DXf)
	#PL7.append((1-Ft[i])*DPXi+Ft[i]*DPXf)
	
plt.plot(KL,PL)
plt.xlabel("x")
plt.ylabel("Ft(x)")
plt.show()

f, (axa, axb, axc) = plt.subplots(3, 1, sharex=True)
axa.plot(List,PL,'r o')
axa.plot(List,PL2,'g s')
axb.plot(List,MagnetF1,'r o')
axb.plot(List,MagnetF2,'b ^')
axc.plot(List,MagnetD1,'r o')
axc.plot(List,MagnetD2,'b ^')
plt.show()

f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
plt.ylabel('Quadrupole K')
ax1.plot(List, MagnetF2, 'g s')
ax1.set_title('Cell')
ax2.plot(List, MagnetD2, 'r o')
plt.show()


'''
ax1 = plt.plot(List,MagnetF2, 'g s')
plt.xlabel("Cell")
plt.ylabel("Focusing Quadrupole K")
plt.grid(True)
#plt.show()

ax2 = plt.subplot(List,MagnetD2, 'r o',share = ax1)
plt.xlabel("Cell")
plt.ylabel("Defocusing Quadrupole K")
plt.grid(True)
plt.gcf()
'''