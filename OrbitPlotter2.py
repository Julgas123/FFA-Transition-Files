'''
This file is designed to read in data from a file, parse it, and graph it
'''
import matplotlib.pyplot as plt
import numpy as np

MassP = .938272
KineticEnergy = .150 #MeV
Gamma = KineticEnergy/MassP + 1
Beta = np.sqrt(1 - (1/Gamma)**2)

class Grapher(object):
	
	# This is designed for the output of the REGULAR TWISS loop
	def __init__(self):
		self.file_object = open("AUG17I.LIS","r")
		self.reader()
	
	# This creates lists
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
		while i <= K:
			if i <= 1:
				Linetemp2.append(Linetemp[47:176]) # 176 (the lengths of the cell portions - 2) because for some reason if we don't it doesn't parse correctly
				i = i + 1
			elif i > 1:
				Linetemp2.append(Linetemp[(47+177*i):(176+177*i)]) # This gets each of the data tables; ignores the rest
				i = i + 1
		#print(Linetemp2) # Diagnostics
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
		for l in range(0,len(Linetemp3)):
			Linetemp4.append(Linetemp3[l])
		for m in range(0,len(Linetemp4)): # This takes away extras which arise due to the parsing
			for n in range(0,len(Linetemp4[m])):
				Linetemp4[m][n] = Linetemp4[m][n][:-1]
		for m in range(0,len(Linetemp4)): # This takes away the name of each piece of the cell
			for n in range(0,len(Linetemp4[m])):
				Linetemp4[m][n] = Linetemp4[m][n][1:]
		#Linetemp4[-1]=Linetemp4[-1][:-1]
		#print(Linetemp4[-1])
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
		I = len(passes)/129
		for i in range(0,int(I)): # This creates empty lists
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
				#py[i].append(passes[i*j][15])
		Linetemp3=[]
		Linetemp4=[]
		passes=[]
		self.GraphMaker(s,betax,betay,mvar1,alfx,mux,dx,dpx,x,px,alfy,muy,dy,dpy,y,py)

	def GraphMaker(self,s,betax,betay,mvar1,alfx,mux,dx,dpx,x,px,alfy,muy,dy,dpy,y,py):
		#dpp = []
		#dpplabel = []
		#dpplabel = ["∂p/p=0.5","∂p/p=0.4","∂p/p=0.3","∂p/p=0.2","∂p/p=0.1","∂p/p=0.0","∂p/p=-0.1"]
		#dpplabel2 = []
		#for i in range(0, len(dpplabel)):
		#	dpplabel2.append(dpplabel[-i])
		#for i in range(0, 20):
			#dpp.append(0.5-0.05*i)
			#dpplabel.append("dpp = "+str(dpp[i]))
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
		for i in range(0,len(s)):
			plt.plot(self.s[i], self.betax[i])#, label=dpplabel[i])
		plt.xlabel('S')
		plt.ylabel('Beta X')
		#plt.legend(loc='best')
		plt.show()
		for i in range(0,len(s)):
			plt.plot(self.s[i], self.betay[i])#, label=dpplabel2[i])
		plt.xlabel('S')
		plt.ylabel('Beta Y')
		#plt.legend(loc='best')
		plt.show()
		for i in range(0,len(s)):
			plt.plot(self.s[i], self.mvar1[i])#, label=dpplabel2[i])
		plt.xlabel('S')
		plt.ylabel('Dx')
		#plt.legend(loc='best')
		plt.show()
		for i in range(0,len(s)):
			plt.plot(self.s[i], self.x[i])#, label=dpplabel2[i])
		plt.xlabel('S')
		plt.ylabel('X')
		#plt.legend(loc='best')
		plt.show()
		
G = Grapher()