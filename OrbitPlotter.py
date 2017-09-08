'''
This file is designed to read in data from a file, parse it, and graph it
'''
import matplotlib.pyplot as plt
import numpy as np

MassP = .938272
KineticEnergy = .150 #GeV
Gamma = KineticEnergy/MassP + 1
Beta = np.sqrt(1 - (1/Gamma)**2)
Pc0 = 0.551345285642 # Corresponds to 150 Mev

class Grapher(object):

	# THhis is designed to take outputs from the PTC_TWISS loop
	def __init__(self):
		self.file_object = open("AUG17I_PTC.LIS","r")
		self.reader()
	
	def reader(self):
		line = self.file_object.readline()
		#length = []
		#alpha_c = []         
		#alpha_c_p = []       
		#alpha_c_p2 = []
		#alpha_c_p3 = []              
		#eta_c = []         
		#gamma_tr = []                
		q1 = [] 
		q2 = []                 
		#dq1 = []                
		#dq2 = []                 
		#qs = []  
		#beta_x_min = []          
		beta_x_max = []          
		#beta_y_min = []          
		beta_y_max = []  
		#beta11min = []           
		#beta11max = []           
		#beta12min = []           
		#beta12max = []  
		#beta13min = []           
		#beta13max = []           
		#beta21min = []          
		#beta21max = []  
		#beta22min = []          
		#beta22max = []           
		#beta23min = []           
		#beta23max = []  
		#beta31min = []           
		#beta31max = []           
		#beta32min = []           
		#beta32max = []  
		#beta33min = []           
		#beta33max = []            
		#disp1min = []            
		disp1max = []  
		#disp2min = []            
		disp2max = []            
		#disp3min = []            
		#disp3max = []  
		#disp4min = []            
		#disp4max = []              
		deltap = []             
		#orbit_x = []  
		#orbit_px = []             
		#orbit_y = []            
		#orbit_py = []            
		#orbit_pt = []  
		#orbit_-cT = []              
		#xcorms = []              
		#ycorms = []             
		#pxcorms = []  
		#pycorms = []              
		#tcorms = []             
		#ptcorms = []              
		xcomax = []  
		ycomax = []             
		#pxcomax = []             
		#pycomax = []              
		#tcomax = []  
		#ptcomax = []              
		#xcomin = []              
		#ycomin = []             
		#pxcomin = []  
		#pycomin = []              
		#tcomin = []             
		#ptcomin = []  
		Linetemp = []
		Linetemp2 = []
		Linetemp3 = []
		lspl = line.split("    ")
		for line in self.file_object:
			Linetemp.append(line)
		K = int((len(Linetemp)-1)/9)
		#print(Linetemp)
		i = 1 
		while i < K:
			if i <= 1:
				Linetemp2.append(Linetemp[7])
				i = i + 1
			elif i > 1:
				Linetemp2.append(Linetemp[(7+9*i)])
				i = i + 1
		for j in range(0,len(Linetemp2)):
			Linetemp3.append([j])
			Linetemp3[j] = Linetemp2[j].split()
		#print(Linetemp3)
		for k in range(0,len(Linetemp3)):
			#length.append(float(Linetemp3[k][0]))
			#alpha_c.append(float(Linetemp3[k][1]))
			#alpha_c_p.append(float(Linetemp3[k][2]))    
			#alpha_c_p2.append(float(Linetemp3[k][3]))
			#alpha_c_p3.append(float(Linetemp3[k][4]))            
			#eta_c.append(float(Linetemp3[k][5]))      
			#gamma_tr.append(float(Linetemp3[k][6]))
			q1.append(float(Linetemp3[k][7]))
			q2.append(float(Linetemp3[k][8]))                
			#dq1.append(float(Linetemp3[k][9]))              
			#dq2.append(float(Linetemp3[k][10]))                
			#qs.append(float(Linetemp3[k][11]))
			#beta_x_min.append(float(Linetemp3[k][12]))      
			beta_x_max.append(float(Linetemp3[k][13]))
			#beta_y_min.append(float(Linetemp3[k][14]))     
			beta_y_max.append(float(Linetemp3[k][15]))
			#beta11min.append(float(Linetemp3[k][16]))         
			#beta11max.append(float(Linetemp3[k][17]))     
			#beta12min.append(float(Linetemp3[k][18]))
			#beta12max.append(float(Linetemp3[k][19]))
			#beta13min.append(float(Linetemp3[k][20]))
			#beta13max.append(float(Linetemp3[k][21]))  
			#beta21min.append(float(Linetemp3[k][22]))
			#beta21max.append(float(Linetemp3[k][23]))
			#beta22min.append(float(Linetemp3[k][24]))
			#beta22max.append(float(Linetemp3[k][25]))
			#beta23min.append(float(Linetemp3[k][26]))
			#beta23max.append(float(Linetemp3[k][27]))
			#beta31min.append(float(Linetemp3[k][28]))  
			#beta31max.append(float(Linetemp3[k][29])) 
			#beta32min.append(float(Linetemp3[k][30]))
			#beta32max.append(float(Linetemp3[k][31]))
			#beta33min.append(float(Linetemp3[k][32]))
			#beta33max.append(float(Linetemp3[k][33]))
			#disp1min.append(float(Linetemp3[k][34]))
			disp1max.append(Beta*float(Linetemp3[k][35]))
			#disp2min.append(float(Linetemp3[k][36]))
			disp2max.append(Beta*float(Linetemp3[k][37]))
			#disp3min.append(float(Linetemp3[k][38]))  
			#disp3max.append(float(Linetemp3[k][39]))
			#disp4min.append(float(Linetemp3[k][40])) 
			#disp4max.append(float(Linetemp3[k][41]))
			deltap.append(float(Linetemp3[k][42]))
			#orbit_x.append(float(Linetemp3[k][43]))
			#orbit_px.append(float(Linetemp3[k][44]))  
			#orbit_y.append(float(Linetemp3[k][45]))
			#orbit_py.append(float(Linetemp3[k][46]))
			#orbit_pt.append(float(Linetemp3[k][47]))
			#orbit_-cT.append(float(Linetemp3[k][48]))    
			#xcorms.append(float(Linetemp3[k][49]))
			#ycorms.append(float(Linetemp3[k][50])) 
			#pxcorms.append(float(Linetemp3[k][51]))
			#pycorms.append(float(Linetemp3[k][52]))
			#tcorms.append(float(Linetemp3[k][53]))    
			#ptcorms.append(float(Linetemp3[k][54]))   
			xcomax.append(float(Linetemp3[k][55]))
			ycomax.append(float(Linetemp3[k][56]))
			#pxcomax.append(float(Linetemp3[k][57])) 
			#pycomax.append(float(Linetemp3[k][58]))
			#tcomax.append(float(Linetemp3[k][59]))
			#ptcomax.append(float(Linetemp3[k][60]))
			#xcomin.append(float(Linetemp3[k][61]))
			#ycomin.append(float(Linetemp3[k][62]))
			#pxcomin.append(float(Linetemp3[k][63]))
			#pycomin.append(float(Linetemp3[k][64]))   
			#tcomin.append(float(Linetemp3[k][65]))    
			#ptcomin.append(float(Linetemp3[k][66]))
		#print(deltap)
		self.GraphMaker(q1,q2,beta_x_max,beta_y_max,disp1max,disp2max,deltap,xcomax,ycomax)
		
	def GraphMaker(self,q1,q2,betx,bety,D1,D2,dpp,xco,yco):
		self.q1 = q1
		self.q2 = q2
		self.beta_x_max = betx
		self.beta_y_max = bety
		self.disp1max = D1
		self.disp2max = D2
		self.deltap = dpp
		self.momentum = []
		self.KE = []
		for i in range(0,len(self.deltap)):
			self.momentum.append(Pc0-self.deltap[i]*Pc0)
			self.KE.append(1000*(-MassP+np.sqrt(MassP**2+self.momentum[i]**2)))
		self.KE.reverse()
		self.xcomax = xco
		self.ycomax = yco
		plt.plot(self.KE, self.q1, 'r-', label='q1')
		plt.plot(self.KE, self.q2, 'b-', label='q2')
		plt.xlabel('Kinetic Energy (MeV)')
		plt.ylabel('q1 and q2')
		plt.legend(loc='best')
		plt.show()
		plt.plot(self.KE, self.beta_x_max, 'r-', label='Beta x Max')
		plt.plot(self.KE, self.beta_y_max, 'b-', label='Beta y Max')
		plt.xlabel('Kinetic Energy (MeV)')
		plt.ylabel('Beta x and y max')
		plt.legend(loc='best')
		plt.show()
		plt.plot(self.KE, self.disp1max, 'r-', label='X Dispersion Max')
		plt.xlabel('Kinetic Energy (MeV)')
		plt.ylabel('Disp1max')
		plt.legend(loc='best')
		plt.show()
		plt.plot(self.KE, self.xcomax, 'r-', label='xcomax')
		plt.plot(self.KE, self.ycomax, 'b-', label='ycomax')
		plt.xlabel('Kinetic Energy (MeV)')
		plt.ylabel('xcomax and ycomax')
		plt.legend(loc='best')
		plt.show()

G = Grapher()
