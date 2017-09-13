file_object = open("JGC.seq","w")
file_object2 = open("TROBVP.SEQ","w")
file_object.write("QF: QUADRUPOLE,L=0.1,K1=9.25; \n"+
				  "BD: SBEND,L=0.3,ANGLE=-11.25*DEGREE,K1=-5.555; \n"+
				  "DO: DRIFT, L=0.04;  // D outside the cell \n"+
				  "DI: DRIFT, L=0.08;  // D inside the cell \n"+
				  "M: MARKER; \n \n \n")
file_object.write("DCELL: SEQUENCE, REFER=ENTRY, L=1.24; \n"
    			  "		DO1:    DO,     AT=0.0; \n"+
    			  "		M1:    	M,     AT=0.04; \n"+
    			  "		QF1:    QF,     AT=0.04; \n"+
    			  "		M2:    	M,     AT=0.14; \n"+
    			  "		QF2:    QF,     AT=0.14; \n"+
    			  "		M3:    	M,     AT=0.24; \n"+
    			  "		DI1:    DI,     AT=0.24; \n"+
    			  "		M4:    	M,     AT=0.32; \n"+
    			  "		BD1:    BD,     AT=0.32; \n"+
    			  "		M5:    	M,     AT=0.62; \n"+
    			  "		BD2:    BD,     AT=0.62; \n"+
    			  "		M6:    	M,     AT=0.92; \n"+
    			  "		DI2:    DI,     AT=0.92; \n"+
    			  "		M7:    	M,     AT=1.0; \n"+
    			  "		QF3:    QF,     AT=1.0; \n"+
    			  "		M8:    	M,     AT=1.1; \n"+
    			  "		QF4:    QF,     AT=1.1; \n"+
    			  "		M9:    	M,     AT=1.2; \n"+
   				  "		DO2:    DO,     AT=1.2; \n"+
				  "ENDSEQUENCE; \n")
print("JGC.SEQ has written successfully.")
file_object.close()
I = 1
while I < 10:
	file_object2.write("PTC_OBSERVE, PLACE=M"+str(I)+"; \n")
	print("Writing: TROBVP.SEQ...")
	I = I + 1
file_object2.close()
print("TROBVP.SEQ has written successfully.")
