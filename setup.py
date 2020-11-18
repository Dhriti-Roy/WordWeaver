import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] =r"C:\Users\Dhriti\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"   
os.environ['TK_LIBRARY'] =r"C:\Users\Dhriti\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("my_editor.py", base=base , icon="icon.ico") ]

cx_Freeze.setup(
    name = "My Editor",
    options={"build_exe":{"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll','icons2','images']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
)