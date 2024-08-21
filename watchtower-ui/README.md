# UI and Python main file

## Summary
This contain UI file and Python code file which will make a basic application for WatchTower. 

## Requirement to use:

### - Main Softwares:
- Sublime text3(or VScode): A shareware text and source code editor. 
- Python 3.10 : Use python for coding functions, getting data and compiling
- PyQt-designer 5.15.2 : Make UI- front-end design for the application
### - Support Resources:
- PySide2: Provides access to the complete Qt 5.12+ framework.
- Qt-material: make application look better ( visual)
- Make sure has these libraries: pandas, qt_material, platform, pynvml, psutil, PySide2extn, shutil, pyopencl, wmi. 

## Function of main files:
- `main.py` : This python file make application for watchtower. Firstly, it make simple functions for the app, then it creates thread worker for each data. Each thread worker will connect to the database and fetch them continuously depend on `sleep()` that user want. After fetching data, it show in proper stack widget in the app
- `ui_interface.py`: This file is auto create by PyQt.
- `interface.ui`: This file must be opened by PyQt. It designes how the app look. User can modify the app design by modify this file.

## - How to run
- Firstly, using Sublime text3 (or any similar software)to open the folder.
- Open `main.py`
- Compile the file or do `Ctrl + B`

