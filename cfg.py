import os
import MemPersistence
import LoadBar

# Cleaning paks to prevent skating
try:
        os.remove("../../Maps/FirstMap/pak/BODPak.dat")
        os.remove("../../Maps/FirstMap/pak/pf.pak")
        print"Pak removed"
except:
        print"Pak NOT removed"
        pass

# Loadscreen
LoadBar.ECTSProgressBar(250,"Blade_progress.jpg")

# Cleaning character data
try:
    Bladex.DeleteStringValue("MainChar")
    props=MemPersistence.Get("MainChar")
    props[2]["Objects"]             = []
    props[2]["Weapons"]             = []
    props[2]["Shields"]             = []
    props[2]["Quivers"]             = []
    props[2]["Keys"]                = []
    props[2]["SpecialKeys"]         = []
    props[2]["Tablets"]             = []
    props[2]["InvLeft"]             = None
    props[2]["InvLeft2"]            = None
    props[2]["InvRight"]            = None
    props[2]["InvLeftBack"]         = None
    props[2]["InvRightBack"]        = None
except:
    pass

execfile("../../Scripts/sys_init.py")
Bladex.ReadLevel("FirstMap.lvl")
execfile("../../Scripts/BladeInit.py")
execfile("DefFuncs.py")
execfile("CutScenes.py")
execfile("enems.py")
execfile("mdoors.py")
execfile("TextureMaterials.py")
execfile("triggers.py")
execfile("antorchas.py")
execfile("pinchos.py")
execfile("MusicEvents.py")