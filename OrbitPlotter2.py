#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#This file is designed to read in data from a file, parse it, and graph it#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
import matplotlib.pyplot as plt
import numpy as np



##################################
#These are the initial parameters#
##################################

MassP = .938272
KineticEnergy = .150 #MeV
Gamma = KineticEnergy/MassP + 1
Beta = np.sqrt(1 - (1/Gamma)**2)



##############################################
#This only works with the STANDARD TWISS LOOP#
##############################################

class Grapher(object):
	
	
	
	############################################
	#This constructor opens the file to read it#
	############################################
	
	def __init__(self):
		self.file_object = open("AUG17I.LIS","r")
		self.reader()
	
	
	
	
	##########################################
	#This function creates the relevant lists#
	##########################################
	
	def reader(self):
		line = self.file_object.readline()
		s = []
		betax = []
		betay = []
		mvar1 = []
		alfx = []
		mux = []
		dx = []
		dpx = []
		x = []
		px = []
		alfy = []
		muy = []	
		dy = []
		dpy = []
		y = []
		py = []
		Linetemp = []
		Linetemp2 = []
		Linetemp3 = []
		Linetemp4 = []
		lspl = line.split("    ")
		# This is where the magic happens
		for line in self.file_object:
			Linetemp.append(line)
		# The 47 and 177 comes from the length of the cell portions of the data lists from the output file
		K = int((len(Linetemp)-1)/177) # It was discovered that the first line of the file is ignored (hence the -1)
		i = 0
		#print(Linetemp)
		
		
		
		#################################################################################################
		#This loop appends the data for each energy (NUMBERS MUST BE CHANGED IF NUMBER OF CELLS CHANGES)#
		#################################################################################################
		while i <= K :
			if i < 1:
				Linetemp2.append(Linetemp[47:176]) # 176 (the lengths of the cell portions - 2) because for some reason if we don't it doesn't parse correctly
				i = i + 1
			elif i >= 1:
				Linetemp2.append(Linetemp[(47+177*i):(176+177*i)]) # This gets each of the data tables; ignores the rest
				i = i + 1
		#print(Linetemp2) # Diagnostics
		
		
		
		#########################################################
		#This loop effectively gets rid of one layer of brackets#
		#########################################################
		
		for j in range(0,len(Linetemp2)):
			Linetemp3.append([j])
			Linetemp3[j] = []
			for k in range(0,len(Linetemp2[j])):
				Linetemp3[j].append([k])
				Linetemp3[j][k] = []
				Linetemp3[j][k] = Linetemp2[j][k].split()
		Linetemp1 = []
		Linetemp2 = []
		#print(Linetemp3[0])
		
		
		
		######################################################
		#This loop gets rid of extras and cleans up the lists#
		######################################################
		
		for l in range(0,len(Linetemp3)):
			Linetemp4.append(Linetemp3[l])
		for m in range(0,len(Linetemp4)): # This takes away the name of each piece of the cell
			for n in range(0,len(Linetemp4[m])):
				Linetemp4[m][n] = Linetemp4[m][n][1:]
		passes = []
		for i in range(0,len(Linetemp4)):
			for k in range(0,len(Linetemp4[i])):
				passes.append(Linetemp4[i][k]) # This takes away one level of brackets
		counter1=0
		I = len(passes)
		while counter1 < I:
			if passes[counter1] == []:
				del passes[counter1]	# This takes away extras
				I = I - 1
				counter1=counter1+1
			else:
				counter1=counter1+1
		counter2=0 
		#print(passes)
		
		
		
		#####################################################
		#This loop appends the relevant variable to its list#
		#####################################################
	
		I = len(passes)/130 #(177-47)
		for i in range(0,int(I+1)): # This creates empty lists
			s.append([i])
			betax.append([i])
			betay.append([i])
			mvar1.append([i])
			alfx.append([i])
			mux.append([i])
			dx.append([i])
			dpx.append([i])
			x.append([i])
			px.append([i])
			alfy.append([i])
			muy.append([i])
			dy.append([i])
			dpy.append([i])
			y.append([i])
			py.append([i])
			s[i] = []
			betax[i] = []
			betay[i] = []
			mvar1[i] = []
			alfx[i] = []
			mux[i] = []
			dx[i] = []
			dpx[i] = []
			x[i] = []
			px[i] = []
			alfy[i] = []
			muy[i] = []	
			dy[i] = []
			dpy[i] = []
			y[i] = []
			py[i] = []
			for j in range(0,129): # (177-47)
				s[i].append(float(passes[j+129*i][0]))
				betax[i].append(float(passes[j+129*i][1]))
				betay[i].append(float(passes[j+129*i][2]))
				x[i].append(float(passes[j+129*i][3]))
				px[i].append(float(passes[j+129*i][4]))
				mvar1[i].append(float(passes[j+129*i][5]))
				alfx[i].append(float(passes[j+129*i][6]))
				mux[i].append(float(passes[j+129*i][7]))
				dx[i].append(float(passes[j+129*i][8]))
				dpx[i].append(float(passes[j+129*i][9]))
				alfy[i].append(float(passes[j+129*i][10]))
				muy[i].append(float(passes[j+129*i][11]))
				dy[i].append(float(passes[j+129*i][12]))
				dpy[i].append(float(passes[j+129*i][13]))
				y[i].append(float(passes[j+129*i][14]))
		Linetemp3=[]
		Linetemp4=[]
		#passes=[]
		self.GraphMaker(s,betax,betay,mvar1,alfx,mux,dx,dpx,x,px,alfy,muy,dy,dpy,y,py)




	##########################################
	#This function is pretty self explanatory#
	##########################################
	
	def GraphMaker(self,s,betax,betay,mvar1,alfx,mux,dx,dpx,x,px,alfy,muy,dy,dpy,y,py):
		#DPPi = -0.40
		#DPPf = 0.30
		#DPPstep = 0.10
		#DPPlength = int(1+(DPPf-DPPi)/DPPstep)
		#dpp = []
		#dpplabel = []
		#for i in range(0,(DPPlength)+1):
		#	dpp.append(DPPi+i*DPPstep)
		#for i in range(0, len(dpp)):
		#	dpplabel.append("∂p/p="+str(dpp[i]))
		#dpplabel.reverse()
		self.s = s
		self.betax = betax
		self.betay = betay
		self.mvar1 = mvar1
		self.alfx = alfx
		self.mux = mux
		self.dx = dx
		self.dpx = dpx
		self.x = x
		self.px = px
		self.alfy = alfy
		self.muy = muy
		self.dy = dy
		self.dpy = dpy
		self.y = y
		self.py = py
		
		
		
		########################
		#This plots Beta X vs S#
		########################
		for i in range(0,len(s)):
			plt.plot(self.s[i], self.betax[i])#, label=dpplabel[i])
		plt.xlabel('S')
		plt.ylabel('Beta X')
		#plt.legend(loc='best')
		plt.show()
		
		
		
		########################
		#This plots Beta Y vs S#
		########################
		for i in range(0,len(s)):
			plt.plot(self.s[i], self.betay[i])#, label=dpplabel[i])
		plt.xlabel('S')
		plt.ylabel('Beta Y')
		#plt.legend(loc='best')
		plt.show()
		
		
		
		####################################################################
		#This plots mux and muy vs S (higher phase advances @ low energies)#
		####################################################################
		f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
		plt.ylabel('MuY (Bottom) and MuX (Top)')
		for i in range(0,len(s)):
			ax1.plot(self.s[i], self.mux[i])
		ax1.set_title('S(m)')
		for i in range(0,len(s)):
			ax2.plot(self.s[i], self.muy[i])
		plt.show()
		
		
		
		############################
		#This plots Dispersion vs S#
		############################
		for i in range(0,len(s)):
			plt.plot(self.s[i], self.mvar1[i])#, label=dpplabel[i])
		plt.xlabel('S')
		plt.ylabel('Dx')
		#plt.legend(loc='best')
		plt.show()
		
		
		
		#########################################
		#This plots transverse displacement vs S#
		#########################################
		for i in range(0,len(s)):
			plt.plot(self.s[i], self.x[i])#, label=dpplabel[i])
		plt.xlabel('S')
		plt.ylabel('X')
		#plt.legend(loc='best')
		plt.show()
		
G = Grapher()
