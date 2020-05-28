import requests
import ScreenClear
import Title
import PathControl
import Writer
import sys

#-----------------------------------------------------------------------------------------------------------------
def Selection():
    while True:
        try:
            x = int(input("\nSelect your Output\n\n1-)JSON\n2-)CSV\n3-)Exit\n: "))
            if x == 1:
                break
            elif x == 2:
                break
            elif x == 3:
                sys.exit()
            else:
                print("Incorrect Entry , Please enter 1 - 2 or 3")
        except ValueError:
            print("Incorrect Entry , Please enter 1 - 2 or 3")
    
    return x
        
#-----------------------------------------------------------------------------------------------------------------

def CollectIOC(outFormat):
    url = "https://otx.alienvault.com/api/v1/pulses/activity"
    while True:     # page loop
        header = {
            'X-OTX-API-KEY' : '<----------------API-KEY---------------------->' # Write API Key
            }


        r = requests.get(url=url,headers=header)
        result = r.json()
        if r.status_code == 200:
            
            for i in range(0,len(result["results"])):   # results loop
                
                indicatorsLength = len(result["results"][i]["indicators"])      # indicators loop
                for j in range(0,indicatorsLength):
                    
                    if outFormat == 1:
                        Writer.jsonWriter(i,j,result)      # json output
                    else:
                        Writer.csvWriter(i,j,result)      # csv output

            if r.json()["next"] is None: #next page control 
                print("IOC Hunter Finished")    #finish
                break
            else:
                url = r.json()["next"]  # go to next page
                        
        else:
            print("IOC Hunter Finished")    #finish
            break
#-----------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    ScreenClear.clear()
    Title.ScreenStarter()
    outFormat = Selection()
    PathControl.PathControl()
    CollectIOC(outFormat)