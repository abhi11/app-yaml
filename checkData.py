#!/usr/bin/python
#Reads the .desktop files and converts into an YAML equivalent

import sys, glob, textwrap,yaml
from collections import OrderedDict
import fileinput

def read_desktop(fname):
        '''Convert a .desktop file into a dict'''
        fobj = open(fname)
        #if oreder is important we must use this or some other approach to keep the dict ordered
        contents = OrderedDict([k.strip().split("=", 1) for k in fobj if "=" in k and k[0] != "#" ])    
        fobj.close()
        return contents

files = {}
i=0
ofile = open("Components.yml","w")

#writing the dicts into yaml
for filename in glob.glob("menu-data/*.desktop"):
        dic = read_desktop(filename)
        
        #i=i+1
        #if i==2:
        #        break

        data = yaml.dump(dic,default_flow_style=False,explicit_start=True)
        data = data.replace("--- !!python/object/apply:collections.OrderedDict","---")
        ofile.write(data)

ofile.close

