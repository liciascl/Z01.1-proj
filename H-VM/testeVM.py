#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Curso de Elementos de Sistemas
# Desenvolvido por: Renan Trevisoli <renantd@insper.edu.br>
#
# Adaptado de :     Rafael Corsi <rafael.corsi@insper.edu.br>
#                   Pedro Cunial   <pedrocc4@al.insper.edu.br>
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
from testeVHDL_cocotb import *
from assembler import compileAll, clearbin
from vmtranslator import vmtranslator

class tstLogiComb(object):
    def __init__(self):
        self.pwd = os.path.dirname(os.path.abspath(__file__))
        vmDir = [self.pwd+"/src/vm/", self.pwd+"/src/examples/"]
        nasm = self.pwd+"/bin/nasm/"
        hack = self.pwd+"/bin/hack/"
        clearbin(nasm)
        clearbin(hack)
        print("------------------------------")
        print("- Translating src files       ")
        print("- to H-VM/bin/nasm/ ")
        print("------------------------------")
        vmtranslator(False, vmDir, nasm)

        print("-------------------------")
        print("- Assembling files .... " )
        print("-------------------------")
        error, log = compileAll(ASSEMBLER_JAR, [nasm], hack)

        self.rtl = os.path.join(self.pwd,'src/')
        self.tst = os.path.join(self.pwd,'teste_cocotb/')
        self.proj = os.path.dirname(self.pwd)
        self.work = vhdlScript_cocotb(self.rtl,self.tst,self.proj)

        if not os.path.isdir(self.tst):
            os.makedirs(self.tst) 

    def addTst(self, work):
        if work.runTstConfigFile(self.pwd + '/') is False:
            sys.exit(1)

    def show_results(self, work):
        work.show_results()

if __name__ == "__main__":
    tstLogiComb = tstLogiComb()
    tstLogiComb.addTst(tstLogiComb.work)   

    print("\n\n===================================================")
    print("H - VM")
    print("===================================================")
    tstLogiComb.show_results(tstLogiComb.work)
    print("===================================================\n")

