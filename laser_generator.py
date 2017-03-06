# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 10:39:01 2016

@author: clayton
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 10:39:35 2016

@author: clayton
"""

#This is a script for creating laser text files
import math

def main():
  speed_light = 299792458
  e0 = 8.85418782e-12
  m_e = 9.109382e-31
  fund_charge = 1.602e-19
  h_SI = 6.626e-34
  
  

#Wavelength is in nanometers
  wavelength_nm = 800
  wavelength_m	= wavelength_nm * 1e-9
  frequency_hz = float(speed_light/wavelength_m)
  
#Angular frequency
  frequency_w = float(2 * math.pi * frequency_hz)
  period_s = float(1 / frequency_hz)
  period_fs = float(period_s*(1e15)) 
  
  wavelength2_nm = wavelength_nm / 2
  frequency2_w = 2 * frequency_w
  
  multiplication_factor = 1.20

#max_electric field intensity in atomic units
  max_e_au = multiplication_factor * float(.05)
  max_e_au2 = multiplication_factor * float(.05)

  #Total Timing in femtoseconds
#use 24.017 for the trapezoidal shape, not sure about sin squared one, perhaps 25 fs
#use 27.349 for the slightly lower frequency 911nm sin squared
#
#use 24.0 for 800nm sin squared    
  total_time = 8.0
#time step in fs
  time_step_length = .001

#create and write name for file corresponding to parameters of simulation
  envelope_name = "_sin_squared_short_small_time_step_fwhm4fs_"
  name = (str(int(wavelength_nm)) + 'nm_and_' + str(int(wavelength2_nm)) + 'nm_circular_polarized_laser_pulse_multiplication_factor_' + str(float(multiplication_factor)) + str(envelope_name) + str(int(total_time)) + 'fs.txt')
  file = open(name, 'w')

#looping over times  
  i = float(0)
  iteration = 1 
  while i <= total_time:
      

  #envelope options to uncomment     
  #simple beam envelope   
   #envelope = 1
  
  # trapezoid envelope shape  
   #number of cycles rising    
   #rising_cycle_num = 2.0
   #number of cycles falling 
   #falling_cycle_num = 2.0
   #number of plateu cycles
   #plateau_cycle_num = 5.0    
  #slope of rising edge    
   #slope = float(1 / (rising_cycle_num * period_fs))
 # find where in the overall envelope the wave is    
  
   #remainder = float(i % ((rising_cycle_num + plateau_cycle_num + falling_cycle_num) * period_fs))
   #if remainder < (rising_cycle_num * period_fs):
    #    envelope = remainder * slope
   #elif remainder > ((rising_cycle_num + plateau_cycle_num) * period_fs):
    #    envelope = 1 - ((remainder - ((rising_cycle_num + plateau_cycle_num) * period_fs)) * slope)
   #else: 
        #envelope = 1      
  #sin squared envelope option shape for fwhm of 4 femtoseconds (divide by 16 in denominator) otherwise try divide by 48
       envelope = float(((math.sin(i * 2 * math.pi/16)) ** 2)) 
       e_x = float(envelope * ((max_e_au * math.cos(i*1e-15 * frequency_w)) + (max_e_au2 * math.cos(i*1e-15 * frequency2_w)))) 
       e_y = float(envelope * ((max_e_au * math.sin(i*1e-15 * frequency_w)) - (max_e_au2 * math.sin(i*1e-15 * frequency2_w))))     
       e_z = float(0) 
       
       file.write(str(iteration) + '\t' + str(i) + '\t' + str(e_x) + '\t' + str(e_y) + '\t' + str(e_z) + '\n')
       i = i + time_step_length
       iteration += 1
#closing the file
  file.close()   

main()
