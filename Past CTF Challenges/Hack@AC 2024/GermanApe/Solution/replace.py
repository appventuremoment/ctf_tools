rep = '5,10,4,11,{22,7,5,12,_7,13,10,9,20,19,16,11,2,13,_9,11,19}'
rep = rep.replace('_', '_,').replace('{', '{,').replace('}', ',}').split(',')
out = "".join([chr(65 + int(i)) if i.isnumeric() else i for i in rep])
print(out)