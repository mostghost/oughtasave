# Oughtasave
A replacement for krita's built-in autosave functionality, except this one is meant to simply save your file automatically and will never delete itself in the name of no longer being "_necessary_". It is set up as a docker; however, you do not need to keep the docker visible if you enable autostart in the settings tab.  

# Installation
Step 1: Download the file from either 'releases' or from the code tab to the upper left (hit 'download zip' at the bottom)   
Step 2: Disable Krita's built in autosave (not strictly required but every time krita saves there is a performance hit so there's no reason to do it twice as much as necessary)  
  
  **AUTOMATIC**  
Step 3: Tools > Scripts > Import Python Plugin from File  
Step 4: Select your .zip file  
Step 5: Restart Krita  
  
  **MANUAL**    
Step 3: Settings > Manage Resources  
Step 4: Hit 'Open Resource Folder' in the bottom right to open your resources library  
Step 5: Unzip your .zip into the 'pykrita' folder  
Step 6: Settings > Configure Krita, and then 'Python Plugin Manager' at the bottom of the list of tabs  
Step 7: Enable Oughtasave  
Step 8: Restart Krita  
  
# How to Use
It should be pretty self explanatory, hit the big button that says 'Click to start Oughtasave' to start Oughtasave. But a few things to note:  

_Settings will be saved, so once you've configured Oughtasave as you want it and have Autostart enabled, you can get rid of the docker and not worry about it. It will still run in the background. If you are working on a new file that hasn't been saved yet, Oughtasave will prompt you for a file name the first time it runs. Otherwise it'll stay out of your way._  

_By default, it will save to the same file. Krita can be set to create 1 backup of your file at a time when saving to a new file- if you want more backups then that, enable 'incremental saves'. However Oughtasave won't delete these automatically, so it's up to you to manage them and keep track of just how many are being saved. Otherwise you might find your hard drive being filled up with dozens of backup saves for every file._  

_'Minutes' seem like an approximation and the time between saves may actually be slightly off from that. It shouldn't be a problem unless you set it to some huge number like over an hour or two._  
