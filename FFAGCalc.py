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
DOL = 0.02		# Outside Drift length space
DIL = 0.03		# Inside Drift length space
BDL = 0.122+2.549849e-04	# Bending Dipole length (rectangular)
QFL = 0.133		# Length of the Quadrupole
TOTL = (DOL+QFL+DIL+BDL+DOL)	# Total length




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
for i in range(0,len(Ft)):
	PL.append((1-Ft[i])*0.008+Ft[i]*0.005)	# Drift Space
	PL2.append((1-Ft[i])*11.25+Ft[i]*5)	# Angles
	PL3.append((1-Ft[i])*45+Ft[i]*80.2651)	# Focusing Quadrupole strength
	PL4.append((1-Ft[i])*(-23)+Ft[i]*(-80.4773))	# Defocusing Quadrupole strength
	PL5.append((1-Ft[i])*(0.2)+Ft[i]*(0.133))	# Quad Length
	PL6.append((1-Ft[i])*(0.3)+Ft[i]*(0.122))	# Dipole Length
	
'''''''''''''''''''''''''''''''''''''''
The snippet below is the Cell Creator 
'''''''''''''''''''''''''''''''''''''''
Lengths = []
Angles = []
J = 0
K = 0
I = 0
Q = 0
Counter = 0
Counter2 = 0
Counter3 = 0
while Counter < Nt:
	file_object.write("DO"+str(q[Counter])+": DRIFT, L="+str(PL[Counter])+"; \n"+
						"DI"+str(q[Counter])+": DRIFT, L="+str(PL[Counter])+"; \n")
	Counter = Counter + 1
file_object.write(" \n \n")
while Counter2 < Nt:
	file_object.write("BD"+str(q[Counter2])+": RBEND, L="+str(PL6[Counter2])+", ANGLE="+str(PL2[Counter2])+"*DEGREE, K1="+str(PL4[Counter2])+"; \n")
	Counter2 = Counter2 + 1
file_object.write("\n \n")
while Counter3 < Nt:
	file_object.write("QF"+str(q[Counter3])+": QUADRUPOLE, L="+str(PL5[Counter3])+", K1:="+str(PL3[Counter3])+"; \n")
	Counter3 = Counter3 + 1
file_object.write("\n \n")
while K < Nt:	
	BDL = PL6[K]+4.824567e-04
	QFL = PL5[K]
	file_object.write("JCELL"+str(K+1)+": SEQUENCE,REFER=ENTRY,L="+str(2*PL[K]+QFL+2*PL[K]+BDL)+"; \n"+
            	                   "    DO"+str(1+2*K)+":    DO"+str(q[K])+",     AT=0.0; \n"+
                	               "    M"+str(1+4*K)+":   MARKER, AT="+str(PL[K])+"; \n"+
                    	           "    QF"+str(1+K)+":    QF"+str(q[K])+",     AT="+str(PL[K])+"; \n"+
                        	       "    M"+str(2+4*K)+":   MARKER, AT="+str(PL[K]+QFL)+"; \n"+
    	                           "    DI"+str(1+K)+":    DI"+str(q[K])+",     AT="+str(PL[K]+QFL)+";  \n"+
        	                       "    M"+str(3+4*K)+":   MARKER, AT="+str(PL[K]+QFL+2*PL[K])+"; \n"+
            	                   "    BD"+str(1+K)+":    BD"+str(q[K])+",     AT="+str(PL[K]+QFL+2*PL[K])+"; \n"+
            	                   "    M"+str(4+4*K)+":   MARKER, AT="+str(PL[K]+QFL+2*PL[K]+BDL)+"; \n"+
                    	           "    DO"+str(2+2*K)+":    DO"+str(q[K])+",     AT="+str(PL[K]+QFL+2*PL[K]+BDL)+"; \n"+
                            	   "ENDSEQUENCE; \n \n")
	Lengths.append(2*PL[K]+QFL+2*PL[K]+BDL)
	Angles.append(PL2[K])
	print(str(K)+": Making a Cell...")
	K = K + 1
file_object.write("TRANSITION: SEQUENCE,REFER=ENTRY,L="+str(sum(Lengths))+"; \n")
while J < Nt:
	file_object.write("   JCELL"+str(J+1)+", AT="+str(sum(Lengths[:J]))+"; \n")
	print(str(J)+": Making Transition...")
	J = J + 1
while I < Nt*4:
	file_object2.write("PTC_OBSERVE, PLACE=M"+str(I+1)+"; \n")
	print(str(I)+": Making an observation point...")
	I = I + 1
file_object.write("ENDSEQUENCE; \n")
file_object2.close()

file_object3 = open("JGC2.seq","w")
while Q < 201:
	file_object3.write("DPP"+str(Q)+"="+str(0.50-0.005*Q)+"; \n"+
						"PTC_CREATE_UNIVERSE; \n"+
						"PTC_CREATE_LAYOUT,MODEL=2,TIME=FALSE, METHOD=4,EXACT; \n"+
						"PTC_TWISS,SUMMARY_TABLE, ICASE=5,DELTAP=DPP"+str(Q)+", SUMMARY_FILE='PTC.LIS'; \n"+
						"PTC_START, X= 1E-6, PX=0, Y= 1E-6, PY=0; \n"+
						"CALL,FILE='TROBVP.SEQ'; \n"+
						"VALUE, CLIGHT; \n"+
						"PTC_TRACK, ICASE=4, ELEMENT_BY_ELEMENT=TRUE,TURNS=2,CLOSED_ORBIT=FALSE,ONETABLE=TRUE,DUMP=TRUE,FFILE=1;//,FILE='ParticleTrack"+str(Q)+"'; \n"+
						"PLOT, FILE='DEJAN_CELL',TABLE=TRACK,HAXIS=X,VAXIS=PX,PARTICLE=1, COLOUR=1000, MULTIPLE, SYMBOL=3; \n"+
						"SYSTEM,'RM PTC.LIS'; \n"+ 
						"WRITE,TABLE=PTC_TWISS_SUMMARY,FILE='PTC.LIS'; \n"+
						"SYSTEM,'CAT PTC.LIS >> AUG17I_PTC.LIS'; \n"+
						"PTC_END; \n \n \n")
	print(str(Q)+": Writing to the file...")
	Q = Q + 1
file_object3.close()
print("The new length of the cell is: "+str(sum(Lengths))+" meters.")
print("Net angle traversed over the distance is: "+str(sum(Angles))+" degrees.")
