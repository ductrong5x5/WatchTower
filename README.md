# Project: Watchtower


## Group members - GithubID 
- Duc Trong Nguyen  - ductrong5x5
- Clayton Gilmer    - cgilmer2
- Clayton Tucker    - CTucker01
- Sam Sui           - SamJSui
- Ryan Franqui      - RJFranqui
- Jacob Curlin      - jtcurlin

## -- Graphic about product --

### - Website (Homepage)   [link](https://watchtower1.000webhostapp.com/)
![Alt text](https://cdn.discordapp.com/attachments/1088861818438557840/1106285484713459773/image.png)
### - Website (data page)
![Alt text](https://cdn.discordapp.com/attachments/1072668307460735046/1104874050519572611/Screen_Shot_2023-05-07_at_4.54.46_PM.png)

### - Desktop app (Window)
![Alt text](https://cdn.discordapp.com/attachments/1088861818438557840/1106286136646713514/image.png)

![Alt text](https://cdn.discordapp.com/attachments/1088861818438557840/1106286373167710259/image.png)

![Alt text](https://cdn.discordapp.com/attachments/1088861818438557840/1106286464293150802/image.png)

### - Logo
![Alt text](https://cdn.discordapp.com/attachments/1072668307460735046/1083507595416977438/IMG_0393.PNG)

## -- Description --
Watchtower continuously collecting data  of user's computer by a sensor which was written in RUST. Afterthat, the data will be sent to SQL server in backend which was written in Python and using Flask. Then, the website will fetch the data from SQL server and show it to user.This website is written in HTML, CSS and PHP. User can install the desktop app to see their computer information from their own machine. The application is written in Python.
## -- Instructions about how to download, install, and run the product --
- For sensor: Go [here](watchtower-sensor/README.md).
- For backend:
  - *DEMO PURPOSES: The backend does not need to be configured*
  - On a designated machine to run the backend and host the server:
    - `cd backend`
    - `python3 app.py`
    - This will accept incoming traffic from the sensors that are on the network and have the target IP configured to this server

- For desktop app : 
  - Requirement: This UI required using python3 and pyQT5.
    - Make sure install these library for python3: Pyside2, pandas, qt_material, platform, pynvml, psutil, PySide2extn, shutil, pyopencl, wmi.
  - How to install:
    - Pull files in watchtower-ui into your computer (windows)
  - How to run:
    - Run `main.py` file.
- For website:
  - This require using XAMPP ( or similar software)
  - After instal XAMPP,  pull all files in `frontend/Jacky-practice` into `htdocs` folder of XAMPP.
  - Open  XAMPP Control Panel and `Start` Apache.
  - Go to browser and type `http://localhost/` or click `Admin` next to `Start`

## -- Instructions on how to use the product --
- Install/run the sensor on relevant computers.
- [Windows](https://cdn.discordapp.com/attachments/1072668307460735046/1105160819978813440/WatchtowerSensorInstall.exe).
- [macOS](https://github.com/utk-cs340-spring23/Watchtower/blob/sprint5/watchtower-sensor/macos_installer.pkg).

- Install the file, a note will pop up. 
- Put `http://64.226.104.86:5000/` as the hostname (or another designated server) and change interval time as needed (default is `5` secs).
  - Connecting a personal backend will allow you to see the debug outputs for the sensors and set a target SQL database.
- Check if the app is running
- ![Alt text](https://cdn.discordapp.com/attachments/1088861818438557840/1106293556391456798/21321.png)
- Go to this [website](https://watchtower1.000webhostapp.com/) to check your device's information. 
- If you already have the desktop app installed, run main.py to see your device's information.
## -- [License](https://github.com/utk-cs340-spring23/Watchtower/blob/main/License.txt)--
 
MIT License

Copyright (c) 2023 Watchtower

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

##  [Presentation link](https://docs.google.com/presentation/d/10DlnmvYG0Ka8SKQckTU7E_1qwQ_HGXzVESHBFP13zs0/edit?usp=sharing)
