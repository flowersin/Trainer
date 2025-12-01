# Import os to retriever and write stats
import os
import datetime # For date and time in log files

class Logger:
    def __init__(self, filename):
        global logfile
        logfile = filename
        with open(logfile, "r") as file:
            log = file.read()
            
    def create_entry(self, caller, message):
        message = str(datetime.datetime.now()) + " - " + str(caller) + " - " + str(message)
        print(message)
        with open(logfile, "a") as file:
            file.write(message + "\n") 
