import os 
def PathControl():
    #logs folder control
    if os.path.exists("logs") is True:
        os.chdir("logs")    #change directory
    else:
        os.mkdir("logs")    #create logs folder
        os.chdir("logs")    #change directory

#-----------------------------------------------------------------------------------------------------------------