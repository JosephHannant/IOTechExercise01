import json
#import numpy as np

# Prompts the user for the location of the file to be opened
filePath = input("Please enter the path to the file:")
with open(filePath, 'r') as f:
  jsonData = json.load(f)

jsonUuid = []

payloads =[]
#Extracts the payload for each device and adds them together and returns them
for deviceN in range(len(jsonData['Devices'])):
    payN = 0
    for sensorN in range(len(jsonData['Devices'][deviceN]['Sensors'])):
        payN += jsonData['Devices'][deviceN]['Sensors'][sensorN]['Payload']
    payloads.append(payN)

payCount = 0
jsonDict = {}

arr = []
# This compiles the required data into a directory to be passed into an array to be sorted
for item in jsonData['Devices']: 
    bigDict = {}
    jsonUuid = item['Info']
    bigDict['Name']=item["Name"]
    bigDict['Type']=item["Type"]
    bigDict['Info']=item['Info']
    bigDict['uuid']  = (jsonUuid[jsonUuid.find("uuid:")+5:jsonUuid.find(",")])  
    bigDict['PayloadTotal']=payloads[payCount]

    
    payCount = payCount+1  
    arr.append(bigDict)
# This sorts the array into the required format and alphabetises the file    
arr.sort(key=lambda d: d['Name'].lower())
finalDict = {
    'properties':{
        'Devices':{
            'items':arr
        }
    }
}
'''
This takes input from the user for the filepath then writes the new data 
into a json file
'''
finalPath = input('Enter file path for new json file:')
with open(finalPath, 'w') as fp:
    json.dump(finalDict, fp, sort_keys=True, indent=4)