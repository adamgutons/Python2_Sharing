"""
This script is a test to collect unique asset, status, and area values from the
json file
"""
import json

def AssembleAreaList(d):
	item = d['area']
	areaList.append(item)

def AssembleStatusList(d):
	item = d['status']
	statusList.append(item)

def AssembleList(d):
	item = d['asset_type']
	assetList.append(item)

areaList = []	
assetList = []
statusList = []
datafile = open('data.txt', 'w')
f = open('cgcapitalprojects_img.geojson.json', 'r')
res = json.load(f)
for p in res['features']:
	AssembleList(p['properties'])
	AssembleStatusList(p['properties'])
	AssembleAreaList(p['properties'])

uniqueAreaVals = list(set(areaList))
uniqueAssestTypeVals = list(set(assetList))
uniqueStatusVals = list(set(statusList))
for x in uniqueAssestTypeVals:
	print('asset_type:', x)
for x in uniqueStatusVals:
	print('status:', x)
for x in uniqueAreaVals:
	print('area:', x)