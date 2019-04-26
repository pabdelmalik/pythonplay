# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:37:54 2019

@author: pabde
"""

import webbrowser
import requests
import bs4
import urllib

#Define your keyword of interest
keyword = "influenza"

#Define global variables
PDFList = []

#Retrieve the results page of a search on the keyword from BMC Public Health
BMCPH = "https://bmcpublichealth.biomedcentral.com/articles?query=" +keyword

#Open the page in a browser to check it
#webbrowser.open(BMCPH)

#Put the text of the defined page into the variable 'res'
res = requests.get(BMCPH)
type(res)
res.status_code == requests.codes.ok
len(res.text)
#print(res.text[:250])

#Get the number of pages
pageText = "Page 1 of "
startPages = res.text.find(pageText) + len(pageText)
endPages = res.text.find("<",startPages)
numPages = int(res.text[startPages:endPages])

#Page string in URL is &page=
#print(numPages)

#Create an array of PDF links


def getPDFList(inputText):
    notEndoflist = True
    PDFList = []
    sanityCheck = 0
    PDFstring = "/track/pdf"
    nextPosition = 0
    while notEndoflist:
        sanityCheck = sanityCheck + 1
        linkStart = inputText.find(PDFstring, nextPosition)
        if sanityCheck > 9999 or linkStart == -1:  
            break   
        linkEnd = inputText.find('"',linkStart)
        PDFList.append (inputText[linkStart:linkEnd])
        nextPosition = linkEnd
        
    return PDFList


for i in range (1,numPages+1):
    PDFSource = BMCPH+"&page=%s"%(i)   #the %s is like a pointer which is replaced by i; done here because cannot concatenate integer to string 
    #print (PDFSource)
    res = requests.get(PDFSource)
    PDFList.extend (getPDFList(res.text))


print (len(PDFList))

#def getPDFs(PDFList):
#    testfile = urllib.URLopener()
#   
#   testfile.retrieve("http://randomsite.com/file.gz", "file.gz")


#folder_location = r'E:\webscraping'
#if not os.path.exists(folder_location):os.mkdir(folder_location)    
    
    
    















