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

#Define the string indicator for a PDF in the source code
PDFstring = "/track/pdf"

#Create empty global array to hold PDF references from all multiple pages
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


def getPDFList():
    for i in range (1,numPages+1):
        sanityCheck = 0
        linkStart = 0
        nextPosition = 0
        PDFSource = BMCPH+"&page=%s"%(i)   #the %s is like a pointer which is replaced by i; done here because cannot concatenate integer to string  
        print (PDFSource)
        res = requests.get(PDFSource)
        while linkStart != -1:
            sanityCheck = sanityCheck + 1
            linkStart = res.text.find(PDFstring, nextPosition)
            if sanityCheck > 9999 or linkStart == -1:  
                break   
            linkEnd = res.text.find('"',linkStart)
            PDFList.append (res.text[linkStart:linkEnd])
            nextPosition = linkEnd
            
            
        #PDFList.extend (getPDFList(res.text))
        #print (PDFSource)

    #return PDFList

getPDFList()
print (len(PDFList))


#def getPDFs(PDFList):
#    testfile = urllib.URLopener()
#   
#   testfile.retrieve("http://randomsite.com/file.gz", "file.gz")


#folder_location = r'E:\webscraping'
#if not os.path.exists(folder_location):os.mkdir(folder_location)    
    
    
    















