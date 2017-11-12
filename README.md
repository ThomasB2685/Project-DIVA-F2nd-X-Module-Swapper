# Project DIVA F2nd/X Module Swapper
A python script which has a variety of functions which can be run on Project DIVA F2nd and X model files (.osd, .osi, .txi and .txd).

# PDcodes()
This function creates a TXT file which includes all of the IDs of the .OSI files located in the same location as it. To run, just use the function "PDcodes()" (without quotations) and a TXT file called PDcodes.txt will be created in the same location.

# PDCmod(ver, module_prefix, module_slot)
This function creates a FARC for the module you want to swap. For example if you want Miku's orignal body on Len's orignal body for X, then you would call the function "PDCmod("X", "mikitm001", "lenitm001")" (without quotations) and the function would return the FARC file: lenitm001.farc in the same location.

To use, you will need to change the location to where your model files are located on the variables "path_to_x_models" and "path_to_f2_models" within the script. To swap F2nd models, you need to use "F2" or "f2" as the ver in the PDCmod. Finally you will also need the FARC packer located in the same location as the script. The FARC packer can be found here: 
