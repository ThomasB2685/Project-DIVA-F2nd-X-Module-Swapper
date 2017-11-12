import os
import shutil
from subprocess import *

def PDcodes():
    
    OSItype = ".osi"
    itmtype = "itm"
    modChars = ["mik", "rin", "len", "luk", "kai", "mei", "tet", "ner", "hak", "sak", "ext"]

    with open('PDcodes.txt','ab') as f:

        for i in xrange(0, 11):
            for j in xrange(1, 999):
                if (j > 200 and j < 400):
                    pass
                elif(j < 10):
                    mod_num = '00' + str(j)
                elif(j > 9 and j < 100):
                    mod_num = '0' + str(j)
                else:
                    mod_num = str(j)

                filename = (modChars[i] + itmtype + mod_num)

                try:
                    with open(filename + OSItype, 'rb') as targetOSI:
                        pass
                except IOError:
                    pass
                else:
                    with open(filename + OSItype, 'rb') as targetOSI:
                        targetOSI.read(144)
                        code = filename + " = " + targetOSI.read(8) + '\r\n'
                        print code
                        targetOSI.close()
                        f.write(code)

    f.close()


def PDCmod (ver, module_prefix, module_slot):
    if(ver == 'x' or ver == 'X'):
        lineOSI = 144
        lineOSD = 160
    elif(ver == "f2" or ver == "F2"):
        lineOSI = 112
        lineOSD = lineOSI
    else:
        print("You inputted " + ver + " which isn't a DIVA game?! Try x/X for PDX and f2/F2 for PDF2nd") 
        raise ValueError

    OSDtype = ".osd"
    OSItype = ".osi"
    TXDtype = ".txd"
    TXItype = ".txi"
    path_to_x_models = "C:\Users\Thomas\Desktop\PDX Models"
    path_to_f2_models = "C:\Users\Thomas\Desktop\PDF2nd Models"
    
    if not (os.path.isfile("PDcodes.txt")):
        print("The PDcodes.txt isn't located in the same directory")
        raise IOError
    
    elif not (module_slot in open("PDcodes.txt", 'rb').read()):
        print("The inputted module name " + module + " doesn't exist in PDcodes.txt")
        raise ValueError

    elif os.path.isdir(module_slot):
        print("Folder of same name to module_slot exists already!")
        raise IOError

    elif not (os.path.isfile(module_prefix+OSDtype) and os.path.isfile(module_prefix+OSItype)
    and os.path.isfile(module_prefix+TXDtype) and os.path.isfile(module_prefix+TXItype)):

        if (ver == 'x' or ver == 'X'):
            if (os.path.isfile(path_to_x_models + '/' + module_prefix + OSDtype) and os.path.isfile(path_to_x_models + '/' + module_prefix + OSItype)
            and os.path.isfile(path_to_x_models + '/' + module_prefix + TXDtype) and os.path.isfile(path_to_x_models + '/' + module_prefix + TXItype)):
                need_to_copy_from = True
                
            else:
                print("Can't find the files in specified directory or root! C'mon mate do you even have the files?!")
                raise IOError
        else:
            if (os.path.isfile(path_to_f2_models + '/' + module_prefix + OSDtype) and os.path.isfile(path_to_f2_models + '/' + module_prefix + OSItype)
            and os.path.isfile(path_to_f2_models + '/' + module_prefix + TXDtype) and os.path.isfile(path_to_f2_models + '/' + module_prefix + TXItype)):
                need_to_copy_from = True
                
            else:
                print("Can't find the files in specified directory or root! C'mon mate do you even have the files?!")
                raise IOError
        
    else:
        need_to_copy_from = False

    if need_to_copy_from == True:

        if(ver == 'x' or ver == 'X'):
            shutil.copy(path_to_x_models + '/' + module_prefix + OSDtype, module_prefix + OSDtype)
            shutil.copy(path_to_x_models + '/' + module_prefix + OSItype, module_prefix + OSItype)
            shutil.copy(path_to_x_models + '/' + module_prefix + TXDtype, module_prefix + TXDtype)
            shutil.copy(path_to_x_models + '/' + module_prefix + TXItype, module_prefix + TXItype)

        else:
            shutil.copy(path_to_f2_models + '/' + module_prefix + OSDtype, module_prefix + OSDtype)
            shutil.copy(path_to_f2_models + '/' + module_prefix + OSItype, module_prefix + OSItype)
            shutil.copy(path_to_f2_models + '/' + module_prefix + TXDtype, module_prefix + TXDtype)
            shutil.copy(path_to_f2_models + '/' + module_prefix + TXItype, module_prefix + TXItype)
    
    with open("PDcodes.txt", 'rb') as PDcodes:
        content = PDcodes.read().index(module_slot)
        PDcodes.seek(0)
        PDcodes.read(content + 12)
        code = PDcodes.read(8)
        PDcodes.close()

    with open((module_prefix + OSItype), 'r+b') as OSI:
        part1 = OSI.read(lineOSI)
        OSI.read(8)
        part2 = OSI.read()
        OSI.seek(0)
        OSI.write(part1 + code + part2)
        OSI.close()

    with open((module_prefix + OSDtype), 'r+b') as OSD:
        part1 = OSD.read(lineOSD)
        OSD.read(4)
        part2 = OSD.read()
        OSD.seek(0)
        OSD.write(part1 + code[0:4] + part2)
        OSD.close()

    os.makedirs(module_slot)

    os.rename(module_prefix + OSDtype, module_slot + '/' + module_prefix + OSDtype)
    os.rename(module_prefix + OSItype, module_slot + '/' + module_prefix + OSItype)
    os.rename(module_prefix + TXDtype, module_slot + '/' + module_prefix + TXDtype)
    os.rename(module_prefix + TXItype, module_slot + '/' + module_prefix + TXItype)        
            
    p = Popen(["FarcPack.exe", module_slot])
    output, errors = p.communicate()
    p.wait()

    shutil.rmtree(module_slot)
    
