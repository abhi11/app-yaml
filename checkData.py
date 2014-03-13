#!/usr/bin/python
#Reads the .desktop files and converts into an YAML equivalent

import sys, glob, yaml

def notcomment(line):
        line = line.strip()
        try:
                if line[0]=="#":
                        return None
                else:
                        #when there's a comment inline
                        if "#" in line:
                                line = line[0:line.find("#")]
                        return line
        except:
                return None

def read_desktop(fname):
        '''Convert a .desktop file into a dict'''
        contents = {}
        fobj = open(fname)
        for line in fobj:
                #first check if line is a comment
                line = notcomment(line)
                if line:
                        #if order is important we have to use some approach to keep the dict ordered using ordererd dict is not a good idea
                        tray = line.split("=",1)
                        try:
                                contents[tray[0].strip()] = tray[1].strip()
                        except:
                                pass
        #print contents
        fobj.close()
        return contents

i=0
ofile = open("Components.yml","w")

#writing the dicts into yaml
for filename in glob.glob("menu-data/*.desktop"):
        dic = read_desktop(filename)
        
        #i=i+1
        #if i==2:
        #        break

        data = yaml.dump(dic,default_flow_style=False,explicit_start=True)
        #data = data.replace("--- !!python/object/apply:collections.OrderedDict","---")
        ofile.write(data)
        ofile.write("\n")
ofile.close

