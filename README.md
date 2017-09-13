# FFAG-Transition-Files
This contains all of the programs to create and test FFAG cells and Transitions:

1) FFAGCalc 1 and 2

These files are the original files I used to create input files for MADX; they're a good way to get an idea of how a cell must 
be generated in order to use PTC_TRACK


2) GammaCalc 

This file is used primarily to calculate values for gamma, beta, and PC based on a user inputed KE; there is a problem when 
inputting 'Y' or 'N' when the user is prompted for the momentum - this works when it's run in a terminal created by 
textwrangler (which I believe uses python 3.6??) - otherwise, one must change 'input' to 'raw_input' 


3) TransitionCalc 1 and 2

These are my babies.  I'm so proud :') Anyway, these are used to create a transition. The first file uses Dejan Trbojevic's 
patented unit cell from his carbon gantry and changes it over a user-inputted number of cells. The second file is what I used 
for my transition presented in the FFAG'17 workshop at Cornell - it can be used as an example to test the transition... 
JGC.MADX and JGC.SEQ are files created specifically for this, so they must be downloaded to run TransitionCalc2


4) OrbitPlotter1 and 2

These are files designed to plot the outputs from JGC.MADX - Orbit plotter 1 is designed to plot the PTC_TWISS output files, 
where as OrbitPlotter 2 is designed to output the normal TWISS files.  PLEASE NOTE: THE PTC_TWISS LOOP IN JGC.MADX MUST BE 
CHANGED BEFORE ORBIT PLOTTER 1 WILL WORK; inside of the main PTC loop, the 'PTC_TWISS' table must be changed to 
'PTC_TWISS_SUMMARY'


5) FFAG Gantries and Adiabatic Transitions (PDF)

This is the slideshow that was presented at the 2017 Fixed-Field Accelerator conference at Cornell. 


6) SingleCell

This file is that which was created to find and test the periodic conditions of a unit cell. It contains methods to vary the 
quadrupole and dipole K strengths as well as methods to test the stability over the entire range of momenta desired (see 
OrbitPlotter 1 and 2).  


7) AccToGantry.SEQ

This is the input file for JGC.MADX.  To get it to run, change the input file in JGC to the name of this file.  Moreover, the initial conditions for the twiss parameters must be entered to match that which would come out of the Linac/Synchrotron/Cyclotron. In this case, BetX0=BetY0=1.2, DX=0.0. 


-------------------------------------------------------------------------------------------------------------------------------
If there are any questions, please contact me and I will try my best to answer them.  
