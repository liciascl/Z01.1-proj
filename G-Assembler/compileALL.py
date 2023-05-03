#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Curso de Elementos de Sistemas
# Desenvolvido por: Rafael Corsi <rafael.corsi@insper.edu.br>
#
# Adaptado de :     Pedro Cunial   <pedrocc4@al.insper.edu.br>
#                   Luciano Soares <lpsoares@insper.edu.br>
# Data de criação: 07/2017

######################################################################
# Tools
######################################################################
from os.path import join, dirname
import sys, subprocess
from pathlib import Path

sys.path.insert(0, str(Path.home()) + '/Z01-Tools/scripts/')
from config import *
from assembler import assemblerAll, clearbin, compileAll, compileAllNotify


pwd = os.path.dirname(os.path.abspath(__file__))

nasm = [pwd+"/../F-Assembly/src/", pwd+"/../F-Assembly/src/examples/"]
hack = pwd+"/bin/hack/"

print("-------------------------")
print("-  Inicio      ")
print("-------------------------")
error, log = compileAll(pwd+"/Assembler/Z01-Assembler.jar", nasm, hack)

if error > 0:
    print("Finalizado com erro")
else:
    print("Finalizado sem erros de compilação")
