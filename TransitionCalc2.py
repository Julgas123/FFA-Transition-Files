'''''''''''''''''''''''''''''''''''''''''''''''''''
This is to ease the process for Transition stuff
'''''''''''''''''''''''''''''''''''''''''''''''''''
import numpy as np
import matplotlib.pyplot as plt




'''''''''''''''''''''''''''''''''
parameters for the FF Below
'''''''''''''''''''''''''''''''''
Massp = 938.27208	# Mass of a Proton (MeV/c^2)
e = 1.602177E-19	# Elementary Charge
clight = 299792458	# Speed of Light
BETREL=0.371258910505  # Corresponds to 150 MeV 

'''''''''''''''''''''''''''''''''''''''''''''
This bit creates the Lists and opens the files
'''''''''''''''''''''''''''''''''''''''''''''
Nt = float(input("Please input a value for the number of cells in the transition: "))
file_object = open("JGC.seq","w")
#file_object2 = open("TROBVP.SEQ","w")
Ft = []
KL = []
b = []
PL = []
PL2 = []
PL3 = []
PL4 = []
PL5 = []
PL6 = []
PL7 = []
q = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
	"AA","BB","CC","DD","EE","FF","GG","HH","II","JJ","KK","LL","MM","NN","OO","PP","QQ","RR","SS","TT","UU","VV","WW","XX","YY","ZZ"]	
for i in range(0,int(Nt+1)):
	k = i/(Nt+1)
	b.append(k-k**2)
	KL.append(k)




'''''''''''''''''''''''''''''''''''''''
The snippet below is the equation Ft(x)
'''''''''''''''''''''''''''''''''''''''
for i in range(0,len(KL)):
	#Ft.append(0.5 + (KL[i] - 0.5)*(1 + 2*(b[i]) + 6*(b[i]**2) + 20*(b[i]**3)))    #CBETA Solution
	Ft.append(np.sin((np.pi/2)*KL[i])**2)    # Julian's Solution (can be Taylor expanded with adjusted coefficients for flexibility
	#Ft.append(KL[i])    # Linear Solution
	#Ft.append(1-np.exp(-5*(KL[i])**2))    # Gaussian Solution
	#Ft.append(-(2.7*KL[i])**(37/10)+(3.7*KL[i])**(27/10))    # Smallest derivative for (1-n)*x^n + n*x^(n-1)



'''''''''''''''''''''''''''''''''''''''
The snippet below is the parameters
'''''''''''''''''''''''''''''''''''''''	
BetXi=1.2
BetYi=1.2
BetXf=0.875
BetYf=0.55
AlfXi=0
AlfYi=0
AlfXf=0
AlfYf=0
Drifti=0.09
Driftf=0.03
DXi=0
DXf=0.081
DPXi=0.0
DPXf=0.0
Anglei=0.0
Anglef=5.625/2
for i in range(0,len(Ft)):
	PL.append((1-Ft[i])*BetXi+Ft[i]*BetXf)	# BetaX
	PL2.append((1-Ft[i])*BetYi+Ft[i]*BetYf)	# BetaY
	PL3.append((1-Ft[i])*AlfXi+Ft[i]*AlfXf)	# AlphaX
	PL4.append((1-Ft[i])*AlfYi+Ft[i]*AlfYf)	# AlphaY
	PL5.append((1-Ft[i])*Drifti+Ft[i]*Driftf)
	PL6.append((1-Ft[i])*DXi+Ft[i]*DXf)
	PL7.append((1-Ft[i])*Anglei+Ft[i]*Anglef)
	
	
'''''''''''''''''''''''''''''''''''''''
The snippet below is the Cell Creator 
'''''''''''''''''''''''''''''''''''''''
J = 0
K = 0
I = 0
L = 0
Q = 0
Counter = 0
Counter2 = 0
Counter3 = 0

# These are the initial conditions for each cell
while Counter < Nt:
	file_object.write("KBD"+str(q[Counter])+"=-2.30961e+01; \n"+
					  "KQF1"+str(q[Counter])+"=3.16245e+01; \n \n")
	Counter = Counter + 1
file_object.write(" \n \n")
file_object.write("M: MARKER;")
file_object.write(" \n \n")

# This creates the Combined Function Dipoles
while Counter2 < Nt:
	file_object.write("BD"+str(q[Counter2])+": SBEND, L=0.1, ANGLE="+str(PL7[Counter2])+"*DEGREE, K1:=KBD"+str(q[Counter2])+"; \n")
	Counter2 = Counter2 + 1
file_object.write("\n \n")

# This creates the Quadrupoles
while Counter3 < Nt+1:
	file_object.write("QF1"+str(q[Counter3])+": QUADRUPOLE, L=0.075, K1:=KQF1"+str(q[Counter3])+"; \n")
	Counter3 = Counter3 + 1
file_object.write("\n \n")
QL = 0.075
DL = 0.1
Lengths = []

# This outputs the entire cell in a MADX friendly format
while K < Nt:	
	file_object.write("DCELL"+str(q[K])+": SEQUENCE, REFER=ENTRY, L="+str(2*QL+2*PL5[K]+2*DL)+"; \n"
    		 	 "		QF"+str(1+2*K)+":    QF1"+str(q[K])+",     AT=0.00; \n"+
    		 	 "		BD"+str(1+2*K)+":    BD"+str(q[K])+",     AT="+str(QL+PL5[K])+"; \n"+
    		 	 "		BD"+str(2+2*K)+":    BD"+str(q[K])+",     AT="+str(QL+PL5[K]+DL)+"; \n"+
    		 	 "		QF"+str(2+2*K)+":    QF1"+str(q[K])+",     AT="+str(QL+2*PL5[K]+2*DL)+"; \n"+
			 	 "ENDSEQUENCE; \n \n \n")
	print(str(K)+": Making a Cell...")
	Lengths.append(2*QL+2*PL5[K]+2*DL)
	K = K + 1
file_object.write("TRANSITION: SEQUENCE,REFER=ENTRY,L="+str(sum(Lengths))+"; \n")

# This names everything
while J < Nt:
	file_object.write("   DCELL"+str(q[J])+", AT="+str(sum(Lengths[:J]))+"; \n")
	print(str(J)+": Making Transition...")
	J = J + 1
file_object.write("ENDSEQUENCE; \n \n \n")

# This loop creates observation points for PTC (not written into the cell) 
'''''''''
while I < Nt*9:
	file_object2.write("PTC_OBSERVE, PLACE=M"+str(I+1)+"; \n")
	print(str(I)+": Making an observation point...")
	I = I + 1
file_object2.close()
'''''''''

# This creates the constraints (the heart of this method)
while L < Nt:
	if L < 1:
		file_object.write("USE,SEQUENCE=DCELL"+str(q[L])+"; \n"+
						  "MATCH, SEQUENCE=DCELL"+str(q[L])+", SLOW=TRUE; \n"+
					 	  "CONSTRAINT, SEQUENCE=DCELL"+str(q[L])+",RANGE=#S,BETX="+str(BetXi)+",BETY="+str(BetYi)+",DX="+str(DXi/BETREL)+"; \n"+
					 	  "CONSTRAINT, SEQUENCE=DCELL"+str(q[L])+",RANGE=#E,BETX="+str(PL[L+1])+",BETY="+str(PL2[L+1])+",DX="+str(PL6[L+1]/BETREL)+"; \n"+
						  "VARY,NAME=KBD"+str(q[L])+",STEP=1E-6; \n"+
						  "VARY,NAME=KQF1"+str(q[L])+",STEP=1E-6; \n"+
						  "LMDIF,CALLS=5000,TOLERANCE=1E-20; \n"+
						  "ENDMATCH; \n \n \n")
		L=L+1
	elif L >= 1 and L < Nt - 1:
		file_object.write("USE,SEQUENCE=DCELL"+str(q[L])+"; \n"+
						  "MATCH, SEQUENCE=DCELL"+str(q[L])+", SLOW=TRUE; \n"+
					 	  "CONSTRAINT, SEQUENCE=DCELL"+str(q[L])+",RANGE=#S,BETX="+str(PL[L])+",BETY="+str(PL2[L])+",DX="+str(PL6[L]/BETREL)+"; \n"+
					 	  "CONSTRAINT, SEQUENCE=DCELL"+str(q[L])+",RANGE=#E,BETX="+str(PL[L+1])+",BETY="+str(PL2[L+1])+",DX="+str(PL6[L+1]/BETREL)+"; \n"+
						  "VARY,NAME=KBD"+str(q[L])+",STEP=1E-6; \n"+
						  "VARY,NAME=KQF1"+str(q[L])+",STEP=1E-6; \n"+
						  "LMDIF,CALLS=5000,TOLERANCE=1E-20; \n"+
						  "ENDMATCH; \n \n \n")
		L=L+1
	else:
		file_object.write("USE,SEQUENCE=DCELL"+str(q[L])+"; \n"+
						  "MATCH, SEQUENCE=DCELL"+str(q[L])+", SLOW=TRUE; \n"+
					 	  "CONSTRAINT, SEQUENCE=DCELL"+str(q[L])+",RANGE=#S,BETX="+str(PL[L])+",BETY="+str(PL2[L])+",DX="+str(PL6[L]/BETREL)+"; \n"+
					 	  "CONSTRAINT, SEQUENCE=DCELL"+str(q[L])+",RANGE=#E,BETX="+str(BetXf)+",BETY="+str(BetYf)+",DX="+str(DXf/BETREL)+"; \n"+
						  "VARY,NAME=KBD"+str(q[L])+",STEP=1E-6; \n"+
						  "VARY,NAME=KQF1"+str(q[L])+",STEP=1E-6; \n"+
						  "LMDIF,CALLS=5000,TOLERANCE=1E-20; \n"+
						  "ENDMATCH; \n \n \n")
		L=L+1

# This finishes up
file_object.write(" \n \n LTransition:="+str(sum(Lengths))+";")
file_object.close()
