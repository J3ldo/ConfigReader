# ConfigReader
A simple config reader to read config files.

## What it has
* Read config files such as .ini files
* Set a custom variable to split the config with such as = or : 
* Converting the config to a python dictionary

## How to use
Step 1: Install the repository by cloning it  
Step 2: Drag the ConfigReader.py in to the same directory as your script.
Step 3: Open your prefered python editor  
Step 4:  
```python
import ConfigReader

config = ConfigReader.ConfigReader().readfile("config.ini")
```
