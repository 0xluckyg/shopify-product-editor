import csv
from tempfile import NamedTemporaryFile


def setAvailability(row):    
    if str(row[6]) == 'true':
        row[6] = 'false'
    return row

def addTag(row, tag):
    if str(row[1]) != '':
        if row[5] != '':
            row[5] = row[5]+','+tag
        else:
            row[5] = tag
    return row

new = NamedTemporaryFile(delete=False)

with open('original.csv', 'rt', encoding='utf8') as original:     
    with open('final.csv', 'w+', encoding='utf8') as new: 
        reader = csv.reader(original,delimiter=',')
        writer = csv.writer(new,delimiter=',')    
        for row in reader:            
            row = setAvailability(row)
            row = addTag(row, 'unoriginal')
            # print(row)
            writer.writerow(row)

# handle = product['handle']              #0
# title = product['title']                #1
# body = product['body_html']             #2
# vendor = product['vendor']              #3
# ptype = product['product_type']         #4
# tags = ','.join(product['tags'])        #5
# published = 'true'                      #6
# option1Name = None #ADD               #7
# option1Value = None #ADD              #8
# option2Name = None #ADD               #9
# option2Value = None #ADD              #10
# option3Name = None #ADD               #11
# option3Value = None #ADD              #12
# vSKU = None                           #13
# vGrams = 0                              #14
# vInventoryTracker = 'shopify'           #15
# vInventoryQuantity = 999999             #16
# vInventoryPolicy = 'deny'               #17
# vFullfillmentService = 'manual'         #18             
# vPrice = 0 #ADD                       #19
# vComparedAtPrice = 0 #ADD             #20
# vRequiresShipping = 'true'              #21
# vTaxable = 'true'                       #22
# vBarcode = None                       #23
# imgSource = None #ADD                 #24
# imgPos = 0 #ADD                       #25
# imgAltText = None                     #26
# giftCard = 'false'                      #27
# seoTitle = None                       #28
# seoDescription = None                 #29
# googleShoppingCategory = None         #30
# googleShoppingGender = None           #31
# googleShoppingAgeGroup = None         #32
# googleShoppingMPN = None              #33
# googleShoppingAdwordsGrouping = None  #34
# googleShoppingAdwordsLabels = None    #35
# googleShoppingCondition = None        #36
# googleShoppingCustomProduct = None    #37
# googleShoppingCustomLabel0 = None     #38
# googleShoppingCustomLabel1 = None     #39
# googleShoppingCustomLabel2 = None     #40
# googleShoppingCustomLabel3 = None     #41
# googleShoppingCustomLabel4 = None     #42
# vImage = None #ADD                    #43
# vWeightUnit = 'lb'                      #44
# vTaxCode = None                       #45