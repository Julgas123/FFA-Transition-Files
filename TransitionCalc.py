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
Nt = float(input("Please input a value for the number of cells in the transition: "))
file_object = open("JGC.seq","w")
file_object2 = open("TROBVP.SEQ","w")
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
	#Ft.append(0.5 + (KL[i] - 0.5)*(1 + 0.894*2*(b[i]) + 0.659*6*(b[i]**2) + 0.329*20*(b[i]**3)))
	Ft.append(np.sin((np.pi/2)*KL[i])**2)
	#Ft.append(1-np.exp(-5*(KL[i])**2))
	#Ft.append(-(2.7*KL[i])**(37/10)+(3.7*KL[i])**(27/10))



'''''''''''''''''''''''''''''''''''''''
The snippet below varies the parameters
'''''''''''''''''''''''''''''''''''''''	
BetXi=2.0
BetYi=2.0
BetXf=1.65
BetYf=0.5
AlfXi=0
AlfYi=0
AlfXf=0
AlfYf=0
Xi=0.024
Xf=0.0
DXi=0.12
DXf=0.0
DPXi=0.2
DPXf=0.0
for i in range(0,len(Ft)):
	PL.append((1-Ft[i])*BetXi+Ft[i]*BetXf)	# BetaX
	PL2.append((1-Ft[i])*BetYi+Ft[i]*BetYf)	# BetaY
	PL3.append((1-Ft[i])*AlfXi+Ft[i]*AlfXf)	# AlphaX
	PL4.append((1-Ft[i])*AlfYi+Ft[i]*AlfYf)	# AlphaY
	PL5.append((1-Ft[i])*Xi+Ft[i]*Xf)
	PL6.append((1-Ft[i])*DXi+Ft[i]*DXf)
	PL7.append((1-Ft[i])*DPXi+Ft[i]*DPXf)
	
	
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
while Counter < Nt:
	file_object.write("KBD"+str(q[Counter])+"=-5.555; \n"+
					  "KQF1"+str(q[Counter])+"=9.25; \n"+
					  "KQF2"+str(q[Counter])+"=9.25; \n \n")
	Counter = Counter + 1
file_object.write(" \n \n")
file_object.write("M: MARKER;")
file_object.write(" \n \n")
while Counter2 < Nt:
	file_object.write("BD"+str(q[Counter2])+": SBEND, L=0.3, ANGLE=11.25*DEGREE, K1:=KBD"+str(q[Counter2])+"; \n")
	Counter2 = Counter2 + 1
file_object.write("\n \n")
while Counter3 < Nt:
	file_object.write("QF1"+str(q[Counter3])+": QUADRUPOLE, L=0.1, K1:=KQF1"+str(q[Counter3])+"; \n")
	file_object.write("QF2"+str(q[Counter3])+": QUADRUPOLE, L=0.1, K1:=KQF2"+str(q[Counter3])+"; \n")
	Counter3 = Counter3 + 1
file_object.write("\n \n")
while K < Nt:	
	file_object.write("DCELL"+str(q[K])+": SEQUENCE, REFER=ENTRY, L=1.16; \n"
    			  "		M"+str(1+9*K)+":    	M,     AT=0.00; \n"+
    			  "		QF"+str(1+4*K)+":    QF1"+str(q[K])+",     AT=0.00; \n"+
    			  "		M"+str(2+9*K)+":    	M,     AT=0.10; \n"+
    			  "		QF"+str(2+4*K)+":    QF1"+str(q[K])+",     AT=0.10; \n"+
    			  "		M"+str(3+9*K)+":    	M,     AT=0.20; \n"+
    			  "		M"+str(4+9*K)+":    	M,     AT=0.28; \n"+
    			  "		BD"+str(1+2*K)+":    BD"+str(q[K])+",     AT=0.28; \n"+
    			  "		M"+str(5+9*K)+":    	M,     AT=0.58; \n"+
    			  "		BD"+str(2+2*K)+":   	BD"+str(q[K])+",     AT=0.58; \n"+
    			  "		M"+str(6+9*K)+":    	M,     AT=0.88; \n"+
    			  "		M"+str(7+9*K)+":    	M,     AT=0.96; \n"+
    			  "		QF"+str(3+4*K)+":   	QF2"+str(q[K])+",     AT=0.96; \n"+
    			  "		M"+str(8+9*K)+":    	M,     AT=1.06; \n"+
    			  "		QF"+str(4+4*K)+":    QF2"+str(q[K])+",     AT=1.06; \n"+
    			  "		M"+str(9+9*K)+":    	M,     AT=1.16; \n"+
				  "ENDSEQUENCE; \n \n \n")
	print(str(K)+": Making a Cell...")
	K = K + 1
file_object.write("TRANSITION: SEQUENCE,REFER=ENTRY,L="+str(Nt*1.16)+"; \n")
while J < Nt:
	file_object.write("   DCELL"+str(q[J])+", AT="+str(1.16*J)+"; \n")
	print(str(J)+": Making Transition...")
	J = J + 1
file_object.write("ENDSEQUENCE; \n \n \n")
while I < Nt*9:
	file_object2.write("PTC_OBSERVE, PLACE=M"+str(I+1)+"; \n")
	print(str(I)+": Making an observation point...")
	I = I + 1
file_object2.close()
while L < Nt:
	if L < Nt-1:
		file_object.write("USE,SEQUENCE=DCELL"+str(q[L])+"; \n"+
						  "MATCH, SEQUENCE=DCELL"+str(q[L])+", SLOW=TRUE; \n"+
					 	  "CONSTRAINT, SEQUENCE=DCELL"+str(q[L])+",RANGE=#S,BETX="+str(PL[L])+",BETY="+str(PL2[L])+",X="+str(PL5[L])+",DX="+str(PL6[L])+"; \n"+
					 	  "CONSTRAINT, SEQUENCE=DCELL"+str(q[L])+",RANGE=#S/#E,DPX="+str(PL7[L])+",DX="+str(PL6[L])+"; \n"+
					 	  "CONSTRAINT, SEQUENCE=DCELL"+str(q[L])+",RANGE=#E,BETX="+str(PL[L+1])+",BETY="+str(PL2[L+1])+",X="+str(PL5[L+1])+",DX="+str(PL6[L+1])+"; \n"+
						  "VARY,NAME=KBD"+str(q[L])+",STEP=1E-6; \n"+
						  "VARY,NAME=KQF1"+str(q[L])+",STEP=1E-6; \n"+
						  "VARY,NAME=KQF2"+str(q[L])+",STEP=1E-6; \n"+
						  "SIMPLEX,CALLS=5000,TOLERANCE=1E-20; \n"+
						  "ENDMATCH; \n \n \n")
		L=L+1
	else:
		file_object.write("USE,SEQUENCE=DCELL"+str(q[L])+"; \n"+
						  "MATCH, SEQUENCE=DCELL"+str(q[L])+", SLOW=TRUE; \n"+
					 	  "CONSTRAINT, SEQUENCE=DCELL"+str(q[L])+",RANGE=#S,BETX="+str(PL[L])+",BETY="+str(PL2[L])+",X="+str(PL5[L])+",DX="+str(PL6[L])+"; \n"+
					 	  "CONSTRAINT, SEQUENCE=DCELL"+str(q[L])+",RANGE=#S/#E,DPX="+str(PL7[L])+",DX="+str(PL6[L])+"; \n"+
					 	  "CONSTRAINT, SEQUENCE=DCELL"+str(q[L])+",RANGE=#E,BETX="+str(BetXf)+",BETY="+str(BetYf)+",X="+str(Xf)+",DX="+str(DXf)+"; \n"+
						  "VARY,NAME=KBD"+str(q[L])+",STEP=1E-6; \n"+
						  "VARY,NAME=KQF1"+str(q[L])+",STEP=1E-6; \n"+
						  "VARY,NAME=KQF2"+str(q[L])+",STEP=1E-6; \n"+
						  "SIMPLEX,CALLS=5000,TOLERANCE=1E-20; \n"+
						  "ENDMATCH; \n \n \n")
		L=L+1
file_object.close()