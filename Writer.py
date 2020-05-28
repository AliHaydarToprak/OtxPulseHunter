import json

#-----------------------------------------------------------------------------------------------------------------

def jsonWriter(i, j, result):       # Write to json format in file
    values = {
        "name" : result["results"][i]["name"],
        "value" : result["results"][i]["indicators"][j]["indicator"],
    }
    fileName = result["results"][i]["indicators"][j]["type"] + ".log"
    indicator = result["results"][i]["indicators"][j]["indicator"]
    try:
        with open(fileName) as f:
            if indicator in f.read():       # Duplicate controls
                #print("Duplicate Values")
                pass
            else:   #write file
                with open(fileName,"a") as w:   #open file
                    print(values)           # screen follow
                    json.dump(values,w)     # write json
                    w.write("\n")           # new line
                    
        
    except FileNotFoundError:   # if file not exists
        with open(fileName,"a") as w:    #create and open file
            print(values)   # screen follow
            json.dump(values,w)     # write json
            w.write("\n")           # new line

#-----------------------------------------------------------------------------------------------------------------
def csvWriter(i, j, result):       # Write to csv format in file
    name = result["results"][i]["name"]
    fileName = result["results"][i]["indicators"][j]["type"] + ".csv"
    indicator = result["results"][i]["indicators"][j]["indicator"]
    try:
        with open(fileName) as f:
            if indicator in f.read():       # Duplicate controls
                #print("Duplicate Values")
                pass
            else:   #write file
                with open(fileName,"a") as w:   #open file
                    print(name + "-" + indicator)           # screen follow
                    w.write(name+","+indicator+"\n")     # write csv
                    
        
    except FileNotFoundError:   # if file not exists
        with open(fileName,"a") as w:    #create and open file
            print(name + "-" + indicator)           # screen follow
            w.write(name+","+indicator+"\n")     # write csv

#-----------------------------------------------------------------------------------------------------------------