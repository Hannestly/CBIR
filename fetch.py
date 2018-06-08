import json

filename = input('Enter file number:    ')
filename = filename + '.png'


jsonFile = open('barcode.json','r')
imgdata = json.load(jsonFile)

def search(filename,barcode):
    closefilename = ""
    closeirmaNum = ""
    closebarcode = []
    closehemming = 9999999
    for data in imgdata:
        if data["filename"] == filename:
            pass
        else:
            #hemming distance
            hemming = 0
            hitbarcode = data["barcode"]
            for i in range(0,len(barcode)):
                if barcode[i] != hitbarcode[i]:
                    hemming += 1
            if hemming < closehemming:
                closehemming = hemming
                closefilename = data["filename"]
                closeirmaNum = data["irmaNum"]
                closebarcode = data["barcode"]
    closeHit = [closefilename,closeirmaNum,closebarcode,closehemming]
    return closeHit

    
        

for data in imgdata:
    if data["filename"] == filename:
        print('Searching for:')
        print('filename: \t {}'.format(data["filename"]))
        print('IRMA code: \t {}'.format(data["irmaNum"]))
        print('barcode: \t {}'.format(data["barcode"]))
        
        closeHit = search(data["filename"],data["barcode"])
        print('Closest hit: ')
        print('filename: \t {}'.format(closeHit[0]))
        print('IRMA code: \t {}'.format(closeHit[1]))
        print('barcode: \t {}'.format(closeHit[2]))
        print('hemming distance: \t {}'.format(closeHit[3]))
        break



