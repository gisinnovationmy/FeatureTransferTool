#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Compile resources for PyQt6
"""

import os
import sys
import subprocess

def compile_resources():
    """
    Compile the resources.qrc file to resources.py for PyQt6
    """
    qrc_file = "resources.qrc"
    output_file = "resources.py"
    
    if not os.path.exists(qrc_file):
        print(f"Error: {qrc_file} not found!")
        return False
    
    try:
        subprocess.run(["pyrcc6", "-o", output_file, qrc_file], check=True)
        print(f"Successfully compiled with PyQt6 to {output_file}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: pyrcc6 not found! Please install PyQt6 tools.")
        return False

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    success = compile_resources()
    sys.exit(0 if success else 1)