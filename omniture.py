
import json

file_path = '/Users/aarakeri/PythonScripts/Interview/omniture.txt'
with open(file_path, 'r') as f:
    output = f.readlines()

d={}
for val in output:
    sp =  val.strip('\n').split(':')
    d[sp[0]] = sp[1]

# if d['Click Map'] == 'Y':
#     d['Click Map'] = 'True'
# else:
#     d['Click Map'] = 'False'


print 'clickMapEnabled : {}'.format(d['Click Map'])
print 'campaignName    : {}'.format(d['Campaign'])
print 'campaignFamily  : {}'.format(d['Campaign family'])