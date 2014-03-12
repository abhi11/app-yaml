#!/usr/bin/python
#
# Copyright (C) 2010, 2012 Julian Andres Klode <jak@jak-linux.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, glob, textwrap,yaml
from collections import OrderedDict
import fileinput

def read_desktop(fname):
        '''Convert a .desktop file into a dict'''
        fobj = open(fname)
        #if oreder is important we must use this or some other approach to keep the dict ordered
        contents = OrderedDict([k.strip().split("=", 1) for k in fobj if "=" in k])    
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

