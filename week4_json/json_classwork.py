import json

def splitDict(d):
	for x in d:
		print(x + ':', d[x])

def logMalformedProject(d):
	datafile.write(str(d['id']))
	print('Data written to file')

def AssembleList(d):
	item = d['area']
	l.append(item)
	
l = []
datafile = open('data.txt', 'w')
f = open('cgcapitalprojects_img.geojson.json', 'r')
res = json.load(f)
for p in res['features']:
	splitDict(p['properties'])
	AssembleList(p['properties'])
	if p['properties']['area'] == '':
		logMalformedProject(p['properties'])
uniqueAreaVals = list(set(l))
for x in uniqueAreaVals:
	print(x)