#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Curso de Elementos de Sistemas
# Desenvolvido por: Renan Trevisoli <renantd@insper.edu.br>
#
# Data de criação: 01/2022


######################################################################
# Tools
######################################################################
import os.path 
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home()) + '/Z01-Tools/VHDL-gui/')

import vhdl_gui

pwd = os.path.dirname(os.path.abspath(__file__))
rtl = os.path.join(pwd,'src/')
tst = os.path.join(pwd,'tmp/')
proj = os.path.dirname(pwd)

if not os.path.isdir(tst):
    os.makedirs(tst) 
    
print("===================================================")
print("Starting GUI")

if len(sys.argv) < 2:
    print("Wrong number of arguments!")
else:
    vhdl_gui.run(sys.argv[1],rtl,tst,proj)


print("===================================================")
