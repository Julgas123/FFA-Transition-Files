# FFA-Transition-Files
This contains all of the programs to create and test FFA cells and Transitions:

1) FFACalc 1 and 2

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
JGC.MADX and JGC.SEQ are files created specifically for this, so they must be used alongside TransitionCalc2 (which 
actuallycreates them). After running 'JGC.MADX', the new magnet strengths must be copy/pasted from the terminal to the 
'JGC.SEQ' file. Sometimes, it may not match all of the way, and the strengths of the magnets will not have changed from the 
original input. Try identifying a pattern and making an educated guess about what the strengths could/should be and put that 
into 'JGC.SEQ' before running it again. Then, repreat. 


4) OrbitPlotter1 and 2

These are files designed to plot the outputs from JGC.MADX (they're normally called aug17i_"something") - Orbit plotter 1 is 
designed to plot the PTC_TWISS output files, where as OrbitPlotter 2 is designed to output the normal TWISS files. PLEASE 
NOTE: THE PTC_TWISS LOOP IN JGC.MADX MUST BE CHANGED BEFORE ORBIT PLOTTER 1 WILL WORK; inside of the main PTC loop, the 
'PTC_TWISS' table must be changed to 'PTC_TWISS_SUMMARY'


5) FF Gantries and Adiabatic Transitions (PDF)

This is the slideshow that was presented at the 2017 Fixed-Field Accelerator conference at Cornell. 


6) SingleCell

This file is that which was created to find and test the periodic conditions of a unit cell. It contains methods to vary the 
quadrupole and dipole K strengths as well as methods to test the stability over the entire range of momenta desired (see 
OrbitPlotter 1 and 2).  


7) JGC.MADX and JGC.SEQ

This is the main file to be run with MADX. It should be placed in the same directory as the 'madx' executable along with all of 
the necessary input files (which in its raw, unedited state should simply be 'JGC.SEQ'). By uncommenting some of the blocks, 
different outputs are created which can be used by the 'OrbitPlotter' programs. Currently, it's set up such that the output it 
would provide after one run is that which is used as the Acclerator-to-Gantry transition in the slideshow. The SEQ file can be written by the TransitionCalc programs.  


-------------------------------------------------------------------------------------------------------------------------------
If there are any questions/comments/concerns, please contact me at Julgas123@gmail.com and I will try my best to answer them.  
